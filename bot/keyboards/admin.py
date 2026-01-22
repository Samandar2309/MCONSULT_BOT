from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def admin_menu():
    buttons = [
        ["📊 Umumiy statistika", "👥 Operatorlar statistikasi"],
        ["📥 Barcha murojaatlar", "⏳ Jarayondagi murojaatlar"],
        ["🟢 Muvaffaqiyatli", "🔴 Rad etilgan"],
        ["🔙 Asosiy menyuga qaytish"],
    ]

    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=b) for b in row] for row in buttons],
        resize_keyboard=True,
    )
