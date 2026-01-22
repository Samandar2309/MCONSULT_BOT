from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from bot.keyboards.inline import contact_keyboard

from bot.keyboards.reply import main_menu
from bot.keyboards.inline import contact_keyboard
from bot.utils.storage import user_languages
from config import PHONE, ADMIN_CONTACT, LOCATION_LAT, LOCATION_LON

router = Router()


# 🏢 BIZ HAQIMIZDA
@router.message(F.text.in_(["🏢 Biz haqimizda", "🏢 О нас"]))
async def about_us(message: Message):
    lang = user_languages.get(message.from_user.id, "uz")

    text_uz = (
        "🏢 *MConsult haqida*\n\n"
        "MConsult — bu biznes uchun kompleks xizmatlar markazi.\n\n"
        "Biz quyidagi yo‘nalishlarda faoliyat yuritamiz:\n"
        "• Buxgalteriya va moliyaviy hisob\n"
        "• IT va avtomatlashtirish yechimlari\n"
        "• Brokerlik xizmatlari\n"
        "• Marketing va sotuvni rivojlantirish\n"
        "• Litsenziya olishga amaliy yordam\n"
        "• Energiya audit xizmatlari\n\n"
        "🎯 Maqsadimiz — biznesingizni tizimli, samarali va barqaror rivojlantirish."
    )

    text_ru = (
        "🏢 *О компании MConsult*\n\n"
        "MConsult — это центр комплексных услуг для бизнеса.\n\n"
        "Основные направления нашей деятельности:\n"
        "• Бухгалтерский и финансовый учет\n"
        "• IT и решения по автоматизации\n"
        "• Брокерские услуги\n"
        "• Маркетинг и развитие продаж\n"
        "• Практическая помощь в получении лицензий\n"
        "• Энергетический аудит\n\n"
        "🎯 Наша цель — системное, эффективное и устойчивое развитие вашего бизнеса."
    )

    await message.answer(
        text_uz if lang == "uz" else text_ru,
        parse_mode="Markdown"
    )


# 📞 BIZ BILAN BOG‘LANISH
@router.message(F.text.in_(["📞 Biz bilan bog'lanish", "📞 Связаться с нами"]))
async def contact_menu(message: Message):
    lang = user_languages.get(message.from_user.id, "uz")

    text = (
        "📞 Biz bilan bog‘lanish uchun qulay usulni tanlang 👇"
        if lang == "uz"
        else "📞 Выберите удобный способ связи 👇"
    )

    await message.answer(
        text,
        reply_markup=contact_keyboard(lang)
    )


# ☎️ TELEFON
@router.callback_query(F.data == "contact_phone")
async def send_phone(callback: CallbackQuery):
    await callback.message.answer(f"☎️ Telefon: {PHONE}")
    await callback.answer()


# 👤 TELEGRAM
@router.callback_query(F.data == "contact_telegram")
async def send_telegram(callback: CallbackQuery):
    await callback.message.answer(
        f"👤 Telegram: {ADMIN_CONTACT}",
        parse_mode=None
    )
    await callback.answer()


# 📍 JOYLASHUV
@router.callback_query(F.data == "contact_location")
async def send_location(callback: CallbackQuery):
    await callback.message.answer_location(
        latitude=LOCATION_LAT,
        longitude=LOCATION_LON
    )
    await callback.answer()


# 🔙 ASOSIY MENYUGA QAYTISH
@router.message(F.text.in_(["🔙 Orqaga", "🔙 Назад"]))
async def back_to_menu(message: Message):
    lang = user_languages.get(message.from_user.id, "uz")
    await message.delete()
    await message.answer(
        "👇 Asosiy menyu",
        reply_markup=main_menu(lang)
    )
@router.callback_query(F.data == "go_main_menu")
async def go_main_menu(callback: CallbackQuery):
    lang = user_languages.get(callback.from_user.id, "uz")

    # 🔥 1. JORIY SAHIFANI BUTUNLAY O‘CHIRADI
    await callback.message.delete()

    # 🔥 2. ASOSIY MENYUNI YANGI MESSAGE SIFATIDA CHIQARADI
    await callback.message.answer(
        "👇 Asosiy menyu" if lang == "uz" else "👇 Главное меню",
        reply_markup=main_menu(lang)
    )

    await callback.answer()