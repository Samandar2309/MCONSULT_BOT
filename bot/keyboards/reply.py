from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu(lang: str = "uz") -> ReplyKeyboardMarkup:
    """
    ASOSIY MENYU (FOYDALANUVCHI UCHUN)
    2 ustun × 3 qator
    Jami 5 ta tugma
    """

    if lang == "ru":
        buttons = [
            ["🏢 О нас", "📋 Список услуг"],
            ["📝 Оставить заявку", "📞 Связаться с нами"],
            ["🌐 Сменить язык"],
        ]
    else:
        buttons = [
            ["🏢 Biz haqimizda", "📋 Xizmatlar ro'yxati"],
            ["📝 Murojaat qoldirish", "📞 Biz bilan bog'lanish"],
            ["🌐 Tilni o'zgartirish"],
        ]

    keyboard = [
        [KeyboardButton(text=button) for button in row]
        for row in buttons
    ]

    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )


def admin_menu() -> ReplyKeyboardMarkup:
    """
    ADMIN PANEL MENYUSI
    Faqat adminlar uchun
    """

    buttons = [
        ["📋 Jami murojaatlar"],
        ["📊 Statistika"],
        ["👨‍💻 Operatorlar statistikasi"],
    ]

    keyboard = [
        [KeyboardButton(text=button) for button in row]
        for row in buttons
    ]

    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )
