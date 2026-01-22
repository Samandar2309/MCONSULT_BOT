from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# =====================================================
# 🌐 TIL TANLASH
# =====================================================
def language_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🇺🇿 O‘zbekcha", callback_data="lang_uz"),
                InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru"),
            ]
        ]
    )


# =====================================================
# 📋 ASOSIY XIZMATLAR RO‘YXATI
# =====================================================
def services_keyboard(lang: str = "uz") -> InlineKeyboardMarkup:
    services = {
        "uz": [
            ("📊 Buxgalteriya", "service_1"),
            ("📑 Brokerlik", "service_2"),
            ("💻 IT xizmatlari", "service_it"),
            ("🎓 Xodimlar malakasini oshirish", "service_4"),
            ("📜 Litsenziya olishga yordam", "service_5"),
            ("⚡ Energiya audit", "service_6"),
            ("📣 Marketing (sotuv)", "service_7"),
        ],
        "ru": [
            ("📊 Бухгалтерия", "service_1"),
            ("📑 Брокерские услуги", "service_2"),
            ("💻 IT-услуги", "service_it"),
            ("🎓 Повышение квалификации", "service_4"),
            ("📜 Помощь с лицензиями", "service_5"),
            ("⚡ Энергетический аудит", "service_6"),
            ("📣 Маркетинг (продажи)", "service_7"),
        ],
    }

    keyboard = [
        [InlineKeyboardButton(text=text, callback_data=cb)]
        for text, cb in services.get(lang, services["uz"])
    ]

    # Bu yerda ORQAGA tugmasi bo'lmaydi (eng yuqori daraja)
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


# =====================================================
# 📊 BUXGALTERIYA — ICHKI XIZMATLAR
# =====================================================
def accounting_services_keyboard(lang: str = "uz") -> InlineKeyboardMarkup:
    services = {
        "uz": [
            ("💰 Kirim–chiqim hisobi", "acc_income"),
            ("📊 Daromad va xarajatlar", "acc_profit"),
            ("👨‍💼 Xodimlar oyligi", "acc_salary"),
            ("🧾 Soliq hisobotlari", "acc_tax"),
            ("📑 Moliyaviy hisobotlar", "acc_reports"),
            ("🧠 Buxgalteriya konsultatsiyasi", "acc_consult"),
        ],
        "ru": [
            ("💰 Учет доходов и расходов", "acc_income"),
            ("📊 Прибыль и затраты", "acc_profit"),
            ("👨‍💼 Зарплата сотрудников", "acc_salary"),
            ("🧾 Налоговая отчетность", "acc_tax"),
            ("📑 Финансовые отчеты", "acc_reports"),
            ("🧠 Бухгалтерская консультация", "acc_consult"),
        ],
    }

    keyboard = [
        [InlineKeyboardButton(text=text, callback_data=cb)]
        for text, cb in services.get(lang, services["uz"])
    ]
    keyboard.append([
        InlineKeyboardButton(
            text="🔙 Orqaga" if lang == "uz" else "🔙 Назад",
            callback_data="back_to_services"
        )
    ])
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


# =====================================================
# 📑 BROKERLIK — ICHKI XIZMATLAR
# =====================================================
def broker_services_keyboard(lang: str = "uz") -> InlineKeyboardMarkup:
    services = {
        "uz": [
            ("📦 Import–export hujjatlari", "broker_docs"),
            ("🛃 Bojxona deklaratsiyasi", "broker_customs"),
            ("📜 Sertifikat va ruxsatnomalar", "broker_cert"),
            ("📝 Shartnomalar bilan ishlash", "broker_contract"),
            ("🚚 Tovarni rasmiy olib kirish/chiqarish", "broker_logistics"),
            ("🧠 Brokerlik konsultatsiyasi", "broker_consult"),
        ],
        "ru": [
            ("📦 Импорт–экспорт документы", "broker_docs"),
            ("🛃 Таможенная декларация", "broker_customs"),
            ("📜 Сертификаты и разрешения", "broker_cert"),
            ("📝 Работа с договорами", "broker_contract"),
            ("🚚 Официальный ввоз/вывоз товара", "broker_logistics"),
            ("🧠 Брокерская консультация", "broker_consult"),
        ],
    }

    keyboard = [
        [InlineKeyboardButton(text=text, callback_data=cb)]
        for text, cb in services.get(lang, services["uz"])
    ]
    keyboard.append([
        InlineKeyboardButton(
            text="🔙 Orqaga" if lang == "uz" else "🔙 Назад",
            callback_data="back_to_services"
        )
    ])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


# =====================================================
# 💻 IT — ICHKI XIZMATLAR
# =====================================================
def it_services_keyboard(lang: str = "uz") -> InlineKeyboardMarkup:
    items = {
        "uz": [
            ("🧠 CRM tizimlari", "it_crm"),
            ("👨‍💼 HRM tizimi", "it_hrm"),
            ("🤖 Telegram botlar", "it_bot"),
            ("🌐 Veb-saytlar va platformalar", "it_web"),
            ("🛒 Internet do‘konlar", "it_internet"),
            ("🏬 Marketplace platformalar", "it_marketplace"),
            ("📱 Mobil ilovalar", "it_mobile"),
            ("⚙️ Biznes jarayonlarni avtomatlashtirish", "it_automation"),
            ("💳 To‘lov tizimlari integratsiyasi", "it_payment"),
            ("🔧 Texnik qo‘llab-quvvatlash va IT konsultatsiya", "it_tech"),
        ],
        "ru": [
            ("🧠 CRM-системы", "it_crm"),
            ("👨‍💼 HRM-система", "it_hrm"),
            ("🤖 Telegram-боты", "it_bot"),
            ("🌐 Веб-сайты и платформы", "it_web"),
            ("🛒 Интернет-магазины", "it_internet"),
            ("🏬 Маркетплейс платформы", "it_marketplace"),
            ("📱 Мобильные приложения", "it_mobile"),
            ("⚙️ Автоматизация бизнес-процессов", "it_automation"),
            ("💳 Интеграция платежных систем", "it_payment"),
            ("🔧 Техническая поддержка и IT-консультации", "it_tech"),
        ],
    }

    keyboard = [
        [InlineKeyboardButton(text=text, callback_data=cb)]
        for text, cb in items.get(lang, items["uz"])
    ]

    keyboard.append([
        InlineKeyboardButton(
            text="🔙 Orqaga" if lang == "uz" else "🔙 Назад",
            callback_data="back_to_services"
        )
    ])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def services_4_keyboard(lang: str = "uz") -> InlineKeyboardMarkup:
    service_4 = {
        "uz": [
            ("📘 Buxgalteriya bo‘yicha treninglar", "service_4_1"),
            ("📣 Savdo va marketing treninglari", "service_4_2"),
            ("Menejment va boshqaruv ko‘nikmalari", "service_4_3"),
            ("💻 IT va raqamli savodxonlik treninglari", "service_4_4"),
            ("👥 HR va kadrlar boshqaruvi bo‘yicha o‘qitish", "service_4_5"),
            ("🏢 Korporativ treninglar (jamoa uchun)", "service_4_6"),
            ("🧠 Individual konsultatsiya va coaching", "service_4_7"),
        ],
        "ru": [
            ("📘 Тренинги по бухгалтерскому учёту", "service_4_1"),
            ("📣 Тренинги по продажам и маркетингу", "service_4_2"),
            ("🧭 Обучение навыкам менеджмента и управления", "service_4_3"),
            ("💻 IT-тренинги и развитие цифровой грамотности", "service_4_4"),
            ("👥 Обучение по управлению персоналом (HR)", "service_4_5"),
            ("🏢 Корпоративные тренинги (для команд)", "service_4_6"),
            ("🧠 Индивидуальные консультации и коучинг", "service_4_7"),
        ],
    }

    keyboard = [
        [InlineKeyboardButton(text=text, callback_data=cb)]
        for text, cb in service_4.get(lang, service_4["uz"])
    ]
    keyboard.append([
        InlineKeyboardButton(
            text="🔙 Orqaga" if lang == "uz" else "🔙 Назад",
            callback_data="back_to_services"
        )
    ])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


# =====================================================
# LITSENYA
def services_5_keyboard(lang: str = "uz") -> InlineKeyboardMarkup:
    service_5 = {
        "uz": [
            ("🔍 Litsenziya talablarini tahlil qilish", "service_5_1"),
            ("📄 Hujjatlarni tayyorlash", "service_5_2"),
            ("🏛 Davlat idoralariga topshirish", "service_5_3"),
            ("🔄 Jarayonni to‘liq kuzatib borish", "service_5_4"),
            ("♻️ Rad etilgan litsenziyalarni qayta tiklash", "service_5_5"),
            ("📑 Sertifikatlash xizmatlari", "service_5_6"),
            ("⚖️ Konsultatsiya va huquqiy yordam", "service_5_7"),
        ],

        "ru": [
            ("🔍 Анализ лицензионных требований", "service_5_1"),
            ("📄 Подготовка документов", "service_5_2"),
            ("🏛 Подача документов в государственные органы", "service_5_3"),
            ("🔄 Полное сопровождение процесса", "service_5_4"),
            ("♻️ Восстановление отказанных лицензий", "service_5_5"),
            ("📑 Сертификационные услуги", "service_5_6"),
            ("⚖️ Консультации и правовая поддержка", "service_5_7"),
        ],
    }

    keyboard = [
        [InlineKeyboardButton(text=text, callback_data=cb)]
        for text, cb in service_5.get(lang, service_5["uz"])
    ]
    keyboard.append([
        InlineKeyboardButton(
            text="🔙 Orqaga" if lang == "uz" else "🔙 Назад",
            callback_data="back_to_services"
        )
    ])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


# =====================================================
# AUDIT
def services_6_keyboard(lang: str = "uz") -> InlineKeyboardMarkup:
    service_6 = {
        "uz": [
            ("📊 Energiya iste’molini tahlil qilish", "service_6_1"),
            ("🚨 Ortiqcha energiya sarfini aniqlash", "service_6_2"),
            ("💡 Tejamkorlik bo‘yicha tavsiyalar", "service_6_3"),
            ("🏭 Ishlab chiqarish uskunalarini tekshirish", "service_6_4"),
            ("📈 Energiya samaradorligini oshirish loyihalari", "service_6_5"),
            ("🧾 Hisobot va texnik xulosa tayyorlash", "service_6_6"),
            ("🧠 Energiya audit bo‘yicha konsultatsiya", "service_6_7"),
        ],
        "ru": [
            ("📊 Анализ энергопотребления", "service_6_1"),
            ("🚨 Выявление избыточного потребления энергии", "service_6_2"),
            ("💡 Рекомендации по энергосбережению", "service_6_3"),
            ("🏭 Проверка производственного оборудования", "service_6_4"),
            ("📈 Проекты по повышению энергоэффективности", "service_6_5"),
            ("🧾 Подготовка отчёта и технического заключения", "service_6_6"),
            ("🧠 Консультации по энергетическому аудиту", "service_6_7"),
        ],
    }

    keyboard = [
        [InlineKeyboardButton(text=text, callback_data=cb)]
        for text, cb in service_6.get(lang, service_6["uz"])
    ]
    keyboard.append([
        InlineKeyboardButton(
            text="🔙 Orqaga" if lang == "uz" else "🔙 Назад",
            callback_data="back_to_services"
        )
    ])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


# ====================================================
# MARKETING
def services_7_keyboard(lang: str = "uz") -> InlineKeyboardMarkup:
    service_7 = {
        "uz": [
            ("📉 Sotuv jarayonlarini tahlil qilish", "service_7_1"),
            ("🧩 Marketing strategiya ishlab chiqish", "service_7_2"),
            ("🎯 Target va reklama kampaniyalari", "service_7_3"),
            ("📱 SMM (ijtimoiy tarmoqlar)", "service_7_4"),
            ("🏷 Brendni rivojlantirish", "service_7_5"),
            ("🔻 Savdo voronkasi (sales funnel)", "service_7_6"),
            ("📊 CRM orqali sotuvni oshirish", "service_7_7"),
            ("🧠 Konsultatsiya va audit", "service_7_8"),
        ],
        "ru": [
            ("📉 Анализ процессов продаж", "service_7_1"),
            ("🧩 Разработка маркетинговой стратегии", "service_7_2"),
            ("🎯 Таргетированная реклама и рекламные кампании", "service_7_3"),
            ("📱 SMM (социальные сети)", "service_7_4"),
            ("🏷 Развитие бренда", "service_7_5"),
            ("🔻 Воронка продаж (sales funnel)", "service_7_6"),
            ("📊 Увеличение продаж через CRM", "service_7_7"),
            ("🧠 Консультации и аудит", "service_7_8"),
        ],
    }

    keyboard = [
        [InlineKeyboardButton(text=text, callback_data=cb)]
        for text, cb in service_7.get(lang, service_7["uz"])
    ]
    keyboard.append([
        InlineKeyboardButton(
            text="🔙 Orqaga" if lang == "uz" else "🔙 Назад",
            callback_data="back_to_services"
        )
    ])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


# =====================================================
# 📝 XIZMAT ACTIONLARI (CTA)
def service_action_keyboard(
        *,
        category_callback: str,
        lang: str = "uz"
) -> InlineKeyboardMarkup:
    """
    Har bir xizmat description ostida chiqadi
    """

    texts = {
        "uz": {
            "leave": "📝 Murojaat qoldirish",
            "back": "🔙 Orqaga",
            "menu": "🏠 Asosiy menyu",
        },
        "ru": {
            "leave": "📝 Оставить заявку",
            "back": "🔙 Назад",
            "menu": "🏠 Главное меню",
        },
    }

    t = texts.get(lang, texts["uz"])

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=t["leave"],
                    callback_data="leave_request"
                )
            ],
            [
                InlineKeyboardButton(
                    text=t["back"],
                    callback_data=category_callback
                )
            ],
            [
                InlineKeyboardButton(
                    text=t["menu"],
                    callback_data="go_main_menu"
                )
            ],
        ]
    )


# =====================================================
# 👥 OPERATOR — TICKET
def take_ticket_keyboard(ticket_id: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📞 Bog‘lanish",
                    callback_data=f"take_{ticket_id}"
                )
            ]
        ]
    )


def close_ticket_keyboard(ticket_id: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🟢 Muvaffaqiyatli",
                    callback_data=f"success_{ticket_id}"
                ),
                InlineKeyboardButton(
                    text="🔴 Rad etildi",
                    callback_data=f"reject_{ticket_id}"
                ),
            ]
        ]
    )


# =====================================================
# 👑 ADMIN PANEL
def admin_menu_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("📊 Umumiy statistika", callback_data="admin_stats")],
            [InlineKeyboardButton("👥 Operatorlar statistikasi", callback_data="admin_operators")],
            [InlineKeyboardButton("📋 Barcha murojaatlar", callback_data="admin_tickets")],
        ]
    )


# =====================================================
# 📞 BIZ BILAN BOG‘LANISH
def contact_keyboard(lang: str = "uz") -> InlineKeyboardMarkup:
    texts = {
        "uz": {
            "phone": "☎️ Telefon",
            "telegram": "👤 Telegram",
            "location": "📍 Joylashuv",
            "menu": "🏠 Asosiy menyu",
        },
        "ru": {
            "phone": "☎️ Позвонить",
            "telegram": "👤 Telegram",
            "location": "📍 Местоположение",
            "menu": "🏠 Главное меню",
        },
    }

    t = texts.get(lang, texts["uz"])

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=t["phone"], callback_data="contact_phone")],
            [InlineKeyboardButton(text=t["telegram"], callback_data="contact_telegram")],
            [InlineKeyboardButton(text=t["location"], callback_data="contact_location")],
            [InlineKeyboardButton(text=t["menu"], callback_data="go_main_menu")],
        ]
    )


# =====================================================
# 🔙 ORQAGA + 🏠 ASOSIY MENYU (UNIVERSAL)
def back_and_menu_keyboard(*, back_callback: str, lang: str = "uz") -> InlineKeyboardMarkup:
    texts = {
        "uz": {"back": "🔙 Orqaga", "menu": "🏠 Asosiy menyu"},
        "ru": {"back": "🔙 Назад", "menu": "🏠 Главное меню"},
    }

    t = texts.get(lang, texts["uz"])

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=t["back"],
                    callback_data=back_callback
                )
            ],
            [
                InlineKeyboardButton(
                    text=t["menu"],
                    callback_data="go_main_menu"
                )
            ],
        ]
    )


def confirm_request_keyboard(lang: str = "uz") -> InlineKeyboardMarkup:
    texts = {
        "uz": {"yes": "✅ Tasdiqlash", "no": "❌ Qayta kiritish"},
        "ru": {"yes": "✅ Подтвердить", "no": "❌ Ввести заново"},
    }
    t = texts.get(lang, texts["uz"])

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=t["yes"], callback_data="confirm_yes"),
                InlineKeyboardButton(text=t["no"], callback_data="confirm_no")
            ]
        ]
    )