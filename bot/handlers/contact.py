import re
import logging
from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext

from config import ADMIN_IDS, OPERATOR_GROUP_ID
from bot.states.contact import ContactState
from bot.keyboards.reply import main_menu
from bot.keyboards.inline import take_ticket_keyboard
from bot.utils.storage import user_languages

from bot.database.session import async_session_maker
from bot.db.repositories.tickets import TicketRepository

router = Router()

# =====================================================
# 🛠 YORDAMCHI KONSTANTALAR
# =====================================================
# Regex: +998, 998 bilan yoki usiz kiritilgan 9 ta raqamni tekshiradi
PHONE_REGEX = re.compile(r"^(\+998|998)?\d{9}$")

CONTACT_TEXTS = {
    "ask_name": {"uz": "👤 Ismingizni kiriting:", "ru": "👤 Введите ваше имя:"},
    "ask_phone": {
        "uz": "📞 Telefon raqamingizni kiriting:\nMasalan: +998 94 707 71 78",
        "ru": "📞 Введите номер телефона:\nНапример: +998 94 707 71 78"
    },
    "invalid_phone": {
        "uz": "❌ Telefon raqam noto‘g‘ri.\nFormat: +998901234567",
        "ru": "❌ Неверный номер телефона.\nФормат: +998901234567"
    },
    "ask_msg": {"uz": "📝 Xabaringizni kiriting:", "ru": "📝 Введите ваше сообщение:"},
    "preview": {"uz": "🧐 <b>Ma'lumotlarni tekshiring:</b>", "ru": "🧐 <b>Проверьте данные:</b>"},
    "confirm_q": {"uz": "Barchasi to'g'rimi?", "ru": "Все верно?"},
    "success": {
        "uz": "✅ Murojaatingiz qabul qilindi. Tez orada mutaxassislarimiz bog'lanadi.",
        "ru": "✅ Ваша заявка принята. Наши специалисты скоро свяжутся с вами."
    },
    "error": {
        "uz": "❌ Texnik xatolik yuz berdi. Keyinroq urinib ko'ring.",
        "ru": "❌ Произошла техническая ошибка. Попробуйте позже."
    },
    "main_menu": {"uz": "🏠 Asosiy menyu", "ru": "🏠 Главное меню"}
}


def get_confirm_keyboard(lang: str) -> InlineKeyboardMarkup:
    texts = {
        "uz": {"yes": "✅ Tasdiqlash", "no": "❌ Qayta kiritish"},
        "ru": {"yes": "✅ Подтвердить", "no": "❌ Заполнить заново"}
    }
    t = texts.get(lang, texts["uz"])
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=t["yes"], callback_data="confirm_yes"),
            InlineKeyboardButton(text=t["no"], callback_data="confirm_no")
        ]
    ])


# =====================================================
# 🔙 FSM DAN CHIQISH
# =====================================================
@router.message(F.text.in_([
    "🏢 Biz haqimizda", "📋 Xizmatlar ro'yxati", "📞 Biz bilan bog'lanish",
    "🌐 Tilni o'zgartirish", "🏢 О нас", "📋 Список услуг",
    "📞 Связаться с нами", "🌐 Сменить язык",
]))
async def cancel_fsm(message: Message, state: FSMContext):
    if await state.get_state() is not None:
        await state.clear()
    lang = user_languages.get(message.from_user.id, "uz")
    await message.answer(CONTACT_TEXTS["main_menu"][lang], reply_markup=main_menu(lang))


# =====================================================
# 📝 MUROJAAT BOSHLASH
# =====================================================
@router.message(F.text.in_(["📝 Murojaat qoldirish", "📝 Оставить заявку"]))
@router.callback_query(F.data == "leave_request")
async def start_contact(event: Message | CallbackQuery, state: FSMContext):
    lang = user_languages.get(event.from_user.id, "uz")
    await state.set_state(ContactState.name)
    text = CONTACT_TEXTS["ask_name"][lang]

    if isinstance(event, Message):
        await event.answer(text)
    else:
        await event.message.answer(text)
        await event.answer()


# =====================================================
# 👤 ISM QABUL QILISH
# =====================================================
@router.message(ContactState.name)
async def get_name(message: Message, state: FSMContext):
    lang = user_languages.get(message.from_user.id, "uz")
    await state.update_data(name=message.text.strip())
    await state.set_state(ContactState.phone)
    await message.answer(CONTACT_TEXTS["ask_phone"][lang])


# =====================================================
# 📞 TELEFON QABUL QILISH (Optimallashtirilgan)
# =====================================================
@router.message(ContactState.phone)
async def get_phone(message: Message, state: FSMContext):
    lang = user_languages.get(message.from_user.id, "uz")

    # Probel, qavs va chiziqchalarni tozalash
    # Masalan: "94 707-71-78" -> "947077178"
    raw_phone = re.sub(r"[\s\-\(\)]", "", message.text)

    if not PHONE_REGEX.match(raw_phone):
        await message.answer(CONTACT_TEXTS["invalid_phone"][lang])
        return

    # Standart formatga keltirish (+998XXXXXXXXX)
    if len(raw_phone) == 9:
        raw_phone = "+998" + raw_phone
    elif raw_phone.startswith("998"):
        raw_phone = "+" + raw_phone
    elif not raw_phone.startswith("+"):
        raw_phone = "+" + raw_phone

    await state.update_data(phone=raw_phone)
    await state.set_state(ContactState.message)
    await message.answer(CONTACT_TEXTS["ask_msg"][lang])


# =====================================================
# 📝 XABAR QABUL QILISH VA TEKSHIRISH
# =====================================================
@router.message(ContactState.message)
async def get_message(message: Message, state: FSMContext):
    await state.update_data(message=message.text.strip())
    data = await state.get_data()
    lang = user_languages.get(message.from_user.id, "uz")

    labels = {
        "name": "Ism" if lang == "uz" else "Имя",
        "phone": "Telefon" if lang == "uz" else "Телефон",
        "msg": "Xabar" if lang == "uz" else "Сообщение"
    }

    preview_text = (
        f"{CONTACT_TEXTS['preview'][lang]}\n\n"
        f"👤 <b>{labels['name']}:</b> {data['name']}\n"
        f"📞 <b>{labels['phone']}:</b> {data['phone']}\n"
        f"📝 <b>{labels['msg']}:</b> {data['message']}\n\n"
        f"{CONTACT_TEXTS['confirm_q'][lang]}"
    )

    await state.set_state(ContactState.confirm)
    await message.answer(preview_text, reply_markup=get_confirm_keyboard(lang), parse_mode="HTML")


# =====================================================
# ✅ TASDIQLASH VA SAQLASH
# =====================================================
@router.callback_query(ContactState.confirm, F.data == "confirm_yes")
async def process_confirm_yes(callback: CallbackQuery, state: FSMContext, bot: Bot):
    data = await state.get_data()
    lang = user_languages.get(callback.from_user.id, "uz")
    username = f"@{callback.from_user.username}" if callback.from_user.username else "yo‘q"

    try:
        async with async_session_maker() as session:
            repo = TicketRepository(session)
            ticket = await repo.create(
                name=data["name"], phone=data["phone"],
                message=data["message"], username=username,
            )

        group_text = (
            "📩 <b>Yangi murojaat</b>\n\n"
            f"🆔 <b>ID:</b> {ticket.id}\n"
            f"👤 <b>Ism:</b> {ticket.name}\n"
            f"📞 <b>Telefon:</b> {ticket.phone}\n"
            f"📝 <b>Xabar:</b>\n{ticket.message}\n"
            f"👤 <b>User:</b> {ticket.username}\n\n"
            "Status: 🟡 <b>Yangi</b>"
        )

        await bot.send_message(OPERATOR_GROUP_ID, group_text, reply_markup=take_ticket_keyboard(ticket.id),
                               parse_mode="HTML")
        await bot.send_message(ADMIN_IDS, group_text, parse_mode="HTML")

        await state.clear()
        await callback.message.edit_text(CONTACT_TEXTS["success"][lang])
        await callback.message.answer(CONTACT_TEXTS["main_menu"][lang], reply_markup=main_menu(lang))

    except Exception as e:
        logging.error(f"❌ DATABASE ERROR: {e}")
        await callback.message.answer(CONTACT_TEXTS["error"][lang])

    await callback.answer()


@router.callback_query(ContactState.confirm, F.data == "confirm_no")
async def process_confirm_no(callback: CallbackQuery, state: FSMContext):
    lang = user_languages.get(callback.from_user.id, "uz")
    await state.set_state(ContactState.name)
    await callback.message.edit_text(CONTACT_TEXTS["ask_name"][lang])
    await callback.answer()