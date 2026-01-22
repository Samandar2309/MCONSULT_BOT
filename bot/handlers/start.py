from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from config import ADMIN_ID
from bot.keyboards.inline import language_keyboard
from bot.keyboards.reply import main_menu, admin_menu
from bot.utils.storage import user_languages
from bot.utils.tickets import ticket_store

router = Router()


# ▶️ /start — BOSHLASH + TIL TANLASH
@router.message(F.text == "/start")
async def start_handler(message: Message):
    text = (
        "Assalomu alaykum!\n\n"
        "👋 MConsult rasmiy botiga xush kelibsiz.\n\n"
        "Biz biznesingizni rivojlantirish uchun professional "
        "va amaliy yechimlarni taklif qilamiz.\n\n"
        "🌐 Davom etish uchun tilni tanlang 👇"
    )

    await message.answer(
        text,
        reply_markup=language_keyboard()
    )


# 🌐 TIL TANLANGACH → ASOSIY MENYU
@router.callback_query(F.data.startswith("lang_"))
async def language_selected(callback: CallbackQuery):
    lang = callback.data.split("_")[1]
    user_languages[callback.from_user.id] = lang

    await callback.message.edit_text("✅ Til tanlandi")

    await callback.message.answer(
        "👇 Asosiy menyu",
        reply_markup=main_menu(lang)
    )
    await callback.answer()


# 🌐 TILNI O‘ZGARTIRISH
@router.message(F.text.in_(["🌐 Tilni o'zgartirish", "🌐 Сменить язык"]))
async def change_language(message: Message):
    await message.answer(
        "🌐 Tilni tanlang / Выберите язык 👇",
        reply_markup=language_keyboard()
    )


# 👑 /admin — ADMIN PANEL
@router.message(F.text == "/admin")
async def admin_panel(message: Message):
    if message.from_user.id != ADMIN_ID:
        await message.answer("⛔ Sizda bu buyruq uchun ruxsat yo‘q")
        return

    total_tickets = len(ticket_store.all())

    text = (
        "📊 <b>ADMIN PANEL</b>\n\n"
        f"📥 <b>Jami murojaatlar:</b> {total_tickets}\n\n"
        "Quyidagi bo‘limlardan birini tanlang 👇"
    )

    await message.answer(
        text,
        reply_markup=admin_menu(),
        parse_mode="HTML"
    )
