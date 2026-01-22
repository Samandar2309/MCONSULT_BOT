from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from bot.utils.texts import (
    ACCOUNTING_TEXTS, BROKER_TEXTS, IT_TEXTS,
    SERVICE_4_TEXTS, SERVICE_5_TEXTS, SERVICE_6_TEXTS, SERVICE_7_TEXTS
)
from bot.keyboards.inline import (
    services_keyboard, accounting_services_keyboard, broker_services_keyboard,
    it_services_keyboard, services_4_keyboard, services_5_keyboard,
    services_6_keyboard, services_7_keyboard, service_action_keyboard
)
from bot.utils.storage import user_languages

router = Router()

# =====================================================
# 📋 SARLAVHALAR VA KONFIGURATSIYA
# =====================================================
TITLES = {
    "main_list": {"uz": "📋 Xizmatlar ro‘yxati 👇", "ru": "📋 Список услуг 👇"},
    "service_1": {"uz": "📊 Buxgalteriya xizmatlari 👇", "ru": "📊 Бухгалтерские услуги 👇"},
    "service_2": {"uz": "📑 Brokerlik xizmatlari 👇", "ru": "📑 Брокерские услуги 👇"},
    "service_it": {"uz": "💻 IT xizmatlari 👇", "ru": "💻 IT-услуги 👇"},
    "service_4": {"uz": "🎓 Xodimlarni malakasini oshirish 👇", "ru": "🎓 Повышение квалификации сотрудников 👇"},
    "service_5": {"uz": "📜 Litsenziya olishga yordam 👇", "ru": "📜 Помощь в получении лицензии 👇"},
    "service_6": {"uz": "⚡ Energiya auditi 👇", "ru": "⚡ Энергоаудит 👇"},
    "service_7": {"uz": "📣 Marketing xizmatlari 👇", "ru": "📣 Маркетинговые услуги 👇"},
}

SUB_SERVICES_MAP = {
    "acc_": (ACCOUNTING_TEXTS, "service_1"),
    "broker_": (BROKER_TEXTS, "service_2"),
    "it_": (IT_TEXTS, "service_it"),
    "service_4_": (SERVICE_4_TEXTS, "service_4"),
    "service_5_": (SERVICE_5_TEXTS, "service_5"),
    "service_6_": (SERVICE_6_TEXTS, "service_6"),
    "service_7_": (SERVICE_7_TEXTS, "service_7"),
}

KB_MAP = {
    "service_1": accounting_services_keyboard,
    "service_2": broker_services_keyboard,
    "service_it": it_services_keyboard,
    "service_4": services_4_keyboard,
    "service_5": services_5_keyboard,
    "service_6": services_6_keyboard,
    "service_7": services_7_keyboard,
}

# =====================================================
# 📋 ASOSIY RO'YXAT
# =====================================================
@router.message(F.text.in_(["📋 Xizmatlar ro'yxati", "📋 Список услуг"]))
@router.callback_query(F.data == "back_to_services")
async def show_services(event: Message | CallbackQuery):
    lang = user_languages.get(event.from_user.id, "uz")
    text = TITLES["main_list"][lang]
    kb = services_keyboard(lang)

    if isinstance(event, Message):
        await event.answer(text, reply_markup=kb)
    else:
        await event.message.edit_text(text, reply_markup=kb)
        await event.answer()

# =====================================================
# 📂 KATEGORIYALAR
# =====================================================
@router.callback_query(F.data.in_(TITLES.keys()))
async def handle_category(callback: CallbackQuery):
    lang = user_languages.get(callback.from_user.id, "uz")
    text = TITLES[callback.data][lang]
    kb_func = KB_MAP[callback.data]

    await callback.message.edit_text(text=text, reply_markup=kb_func(lang))
    await callback.answer()

# =====================================================
# 📝 ICHKI XIZMATLAR (Murojaat tugmasi bilan)
# =====================================================
@router.callback_query(lambda c: any(c.data.startswith(pre) for pre in SUB_SERVICES_MAP.keys()))
async def handle_sub_service(callback: CallbackQuery):
    lang = user_languages.get(callback.from_user.id, "uz")

    prefix = next(pre for pre in SUB_SERVICES_MAP.keys() if callback.data.startswith(pre))
    data_source, parent_callback = SUB_SERVICES_MAP[prefix]

    service = data_source.get(callback.data)
    if not service:
        msg = "❌ Xizmat topilmadi" if lang == "uz" else "❌ Услуга не найдена"
        await callback.answer(msg, show_alert=True)
        return

    text = service.get(lang, service["uz"])

    # ✅ TUZATISH: Hamma xizmatlar uchun service_action_keyboard ishlatiladi
    # Bu orqali "Murojaat qoldirish" tugmasi paydo bo'ladi
    kb = service_action_keyboard(category_callback=parent_callback, lang=lang)

    await callback.message.edit_text(text, parse_mode="HTML", reply_markup=kb)
    await callback.answer()