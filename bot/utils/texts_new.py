# =====================================================
# ▶️ START / TIL TANLASH
# =====================================================
START_TEXT = {
    "uz": (
        "Assalomu alaykum!\n\n"
        "👋 MConsult rasmiy botiga xush kelibsiz.\n\n"
        "Biz biznesingizni rivojlantirish uchun "
        "professional va amaliy yechimlarni taklif qilamiz.\n\n"
        "🌐 Davom etish uchun tilni tanlang 👇"
    ),
    "ru": (
        "Здравствуйте!\n\n"
        "👋 Добро пожаловать в официальный бот MConsult.\n\n"
        "Мы предлагаем профессиональные и практичные решения "
        "для развития вашего бизнеса.\n\n"
        "🌐 Для продолжения выберите язык 👇"
    ),
}


# =====================================================
# 🏠 ASOSIY MENYU
# =====================================================
MENU_TEXT = {
    "uz": "👇 Asosiy menyu",
    "ru": "👇 Главное меню",
}


# =====================================================
# 🏢 BIZ HAQIMIZDA
# =====================================================
ABOUT_TEXT = {
    "uz": (
        "🏢 MConsult haqida\n\n"
        "MConsult — bu biznes uchun kompleks xizmatlar markazi.\n\n"
        "Biz quyidagi yo'nalishlarda faoliyat yuritamiz:\n"
        "• Buxgalteriya va moliyaviy hisob\n"
        "• IT va avtomatlashtirish yechimlari\n"
        "• Brokerlik xizmatlari\n"
        "• Marketing va sotuvni rivojlantirish\n"
        "• Litsenziya olishga amaliy yordam\n"
        "• Energiya audit xizmatlari\n\n"
        "🎯 Maqsadimiz — biznesingizni tizimli, samarali va "
        "barqaror rivojlantirish."
    ),
    "ru": (
        "🏢 О компании MConsult\n\n"
        "MConsult — это центр комплексных услуг для бизнеса.\n\n"
        "Мы работаем в следующих направлениях:\n"
        "• Бухгалтерия и финансовый учет\n"
        "• IT и автоматизация бизнес-процессов\n"
        "• Брокерские услуги\n"
        "• Маркетинг и развитие продаж\n"
        "• Практическая помощь в лицензировании\n"
        "• Энергетический аудит\n\n"
        "🎯 Наша цель — системное, эффективное и устойчивое "
        "развитие вашего бизнеса."
    ),
}


# =====================================================
# 📋 XIZMATLAR — UMUMIY TA'RIFLAR
# (asosan fallback yoki qisqa ko'rsatish uchun)
# =====================================================
SERVICES = {
    "uz": {
        "1": (
            "📊 Buxgalteriya\n\n"
            "Moliyaviy hisob-kitoblar, soliq hisobotlari, "
            "daromad va xarajatlar nazorati."
        ),
        "2": (
            "📑 Brokerlik\n\n"
            "Rasmiylashtirish, vositachilik va hujjatlar "
            "bilan ishlash bo'yicha xizmatlar."
        ),
        "3": (
            "💻 IT xizmatlari\n\n"
            "Biznesingiz uchun raqamli yechimlar:\n"
            "• CRM tizimlar\n"
            "• Telegram botlar\n"
            "• Veb-saytlar\n"
            "• Avtomatlashtirish"
        ),
        "4": (
            "🎓 Xodimlar malakasini oshirish\n\n"
            "Kadrlar uchun o'quv kurslari, treninglar "
            "va amaliy mashg'ulotlar."
        ),
        "5": (
            "📜 Litsenziya olishga yordam\n\n"
            "Faoliyatni qonuniy yo'lga qo'yish uchun "
            "to'liq hujjatlashtirish va amaliy ko'mak."
        ),
        "6": (
            "⚡ Energiya audit\n\n"
            "Energiya sarfini tahlil qilish, "
            "tejamkorlik va samaradorlikni oshirish."
        ),
        "7": (
            "📣 Marketing\n\n"
            "Sotuvlarni oshirish, reklama strategiyasi "
            "va bozorni tahlil qilish."
        ),
    },
    "ru": {
        "1": (
            "📊 Бухгалтерия\n\n"
            "Финансовый учет, налоговая отчетность и "
            "контроль доходов и расходов."
        ),
        "2": (
            "📑 Брокерские услуги\n\n"
            "Посредничество, оформление документов "
            "и сопровождение сделок."
        ),
        "3": (
            "💻 IT-услуги\n\n"
            "Цифровые решения для бизнеса:\n"
            "• CRM-системы\n"
            "• Telegram-боты\n"
            "• Веб-сайты\n"
            "• Автоматизация"
        ),
        "4": (
            "🎓 Повышение квалификации\n\n"
            "Обучающие курсы, тренинги и "
            "практические занятия для персонала."
        ),
        "5": (
            "📜 Лицензирование\n\n"
            "Полное сопровождение получения "
            "разрешений и лицензий."
        ),
        "6": (
            "⚡ Энергетический аудит\n\n"
            "Анализ энергопотребления и "
            "повышение энергоэффективности."
        ),
        "7": (
            "📣 Маркетинг\n\n"
            "Развитие продаж, реклама и "
            "маркетинговая стратегия."
        ),
    },
}
ACCOUNTING_TEXTS = {
    "acc_income": {
        "uz": (
            "💰 <b>Kirim–chiqim hisobi</b>\n\n"
            "Biznesda pul bor, lekin qayerga ketayotganini aniq bilmaysizmi?\n"
            "<b>Haqiqiy misol:</b> 100 million so'm tushum, 35-40 million qayerga ketganini bilmadigan kompaniya\n\n"
            "Ushbu xizmat (7-10 kundan boshlab):\n"
            "• barcha tushum va xarajatlar 100% tartib bilan hisobga olinadi\n"
            "• keraksiz va yashirin xarajatlar aniqlanadi (20-35% ortiqcha sarflar yo'q bo'ladi)\n"
            "• pul oqimi doimiy nazorat ostida bo'ladi\n\n"
            "Biz sizga:\n"
            "✔️ kunlik, oylik va umumiy hisobni yuritamiz\n"
            "✔️ aniq raqamlar asosida tahlil beramiz (har bir somni kuzatamiz)\n"
            "✔️ moliyaviy chalkashliklarni 100% yo'q qilamiz\n\n"
            "✅ <b>Natija:</b> xarajatlarni 25-35% kamaytiramiz, pulingiz qayerga ketayotganini aniq bilasiz va <b>foydani 30% oshiriish</b> mumkin."
        ),
        "ru": (
            "💰 <b>Учет доходов и расходов</b>\n\n"
            "В бизнесе есть деньги, но вы не понимаете, куда они уходят?\n"
            "<b>Реальный пример:</b> компания с доходом 100 млн сум теряет 35-40 млн, но не знает куда\n\n"
            "Данная услуга позволяет (от 7-10 дней):\n"
            "• вести точный учет 100% всех доходов и расходов\n"
            "• выявлять лишние и скрытые затраты (20-35% дополнительных расходов исчезнет)\n"
            "• держать денежный поток под полным контролем\n\n"
            "Мы для вас:\n"
            "✔️ ведем ежедневный, месячный и общий учет\n"
            "✔️ предоставляем анализ на основе точных данных (каждую сумму отслеживаем)\n"
            "✔️ устраняем финансовый хаос полностью\n\n"
            "✅ <b>Результат:</b> <b>снижаем расходы на 25-35%</b>, <b>повышаем прибыль на 30%</b>, полная прозрачность денежных потоков."
        ),
    },

    "acc_profit": {
        "uz": (
            "📊 <b>Daromad va xarajatlar tahlili</b>\n\n"
            "Biznesingiz haqiqatan foyda keltiryaptimi yoki faqat aylanma bormi?\n"
            "<b>Haqiqiy misol:</b> 150 million tushum bo'lsa-da, 85% xarajat va faqat 15% foyda\n\n"
            "Biz (5-7 kunlik tahlil):\n"
            "• daromad va xarajatlarni 100% chuqur tahlil qilamiz\n"
            "• qaysi yo'nalish 40-50% foydali, qaysisi zarar ekanini ko'rsatamiz\n"
            "• foydani 25-40% oshirish uchun aniq tavsiyalar beramiz\n\n"
            "Bu xizmat:\n"
            "✔️ noto'g'ri qarorlarning oldini oladi (zarar yo'nalishlari yo'q bo'ladi)\n"
            "✔️ biznesni raqamlar asosida boshqarishga o'rgatadi\n\n"
            "✅ <b>Natija:</b> <b>foydani 25-40% oshiriish</b>, tasodifiy emas, aniq hisob-kitob asosidagi rivojlanish."
        ),
        "ru": (
            "📊 <b>Анализ доходов и расходов</b>\n\n"
            "Ваш бизнес действительно приносит прибыль или только оборот?\n"
            "<b>Реальный пример:</b> доход 150 млн, но 85% расходов и только 15% прибыли\n\n"
            "Мы (анализ 5-7 дней):\n"
            "• проводим глубокий анализ доходов и расходов на 100%\n"
            "• показываем направления с прибылью 40-50% и убыточные\n"
            "• даем точные рекомендации по увеличению прибыли на 25-40%\n\n"
            "Эта услуга:\n"
            "✔️ предотвращает ошибочные решения (убыточные направления исчезнут)\n"
            "✔️ помогает управлять бизнесом на основе цифр\n\n"
            "✅ <b>Результат:</b> <b>повышаем прибыль на 25-40%</b>, развитие на точных расчетах, а не случайности."
        ),
    },

    "acc_salary": {
        "uz": (
            "👨‍💼 <b>Xodimlar oyligi va ish haqi hisobi</b>\n\n"
            "Oylikdagi xato — xodim noroziligi va ishonchsizlik demakdir.\n"
            "<b>Haqiqiy misol:</b> 50 ta xodim bo'lsa, oylik xatolar 5-10 ta bo'lishi oddiy\n\n"
            "Biz (10 kundan boshlab):\n"
            "• oylik, bonus va ushlab qolishlarni 100% aniq hisoblaymiz\n"
            "• kechikish va kelishmovchiliklarni 0% ga kamaytiramiz\n"
            "• rahbar uchun qulay nazorat tizimini yaratamiz\n\n"
            "Bu xizmat orqali:\n"
            "✔️ xodimlar bilan munosabat mustahkamlanadi (90% xodim jihatdan)\n"
            "✔️ ichki tartib va intizom yaxshilanadi\n\n"
            "✅ <b>Natija:</b> xodimlar ishonchi va barqaror jamoa, xatolar 100% yo'q."
        ),
        "ru": (
            "👨‍💼 <b>Расчет заработной платы сотрудников</b>\n\n"
            "Ошибка в зарплате — это недовольство и потеря доверия.\n"
            "<b>Реальный пример:</b> при 50 сотрудниках обычно 5-10 ошибок в расчетах\n\n"
            "Мы (от 10 дней):\n"
            "• точно рассчитываем зарплаты, бонусы на 100%\n"
            "• устраняем задержки и разногласия (сводим к 0%)\n"
            "• создаем удобную систему контроля для руководства\n\n"
            "Эта услуга:\n"
            "✔️ укрепляет отношения с сотрудниками (90% положительных отзывов)\n"
            "✔️ улучшает дисциплину и порядок\n\n"
            "✅ <b>Результат:</b> доверие сотрудников и стабильная команда, 100% точность расчетов."
        ),
    },

    "acc_tax": {
        "uz": (
            "🧾 <b>Soliq hisobotlari</b>\n\n"
            "Soliq xatolari — jarima, tekshiruv va stress.\n"
            "<b>Haqiqiy misol:</b> kichik xato 50 million jarima keltirishiga kadar bo'ladi\n\n"
            "Biz (5-7 kundan boshlab):\n"
            "• soliq hisobotlarini 100% o'z vaqtida tayyorlaymiz\n"
            "• qonunchilikka to'liq mos topshiramiz (0 xato)\n"
            "• jarima va muammolarning oldini olamiz (15 kunlik o'quv)\n\n"
            "Siz:\n"
            "✔️ soliq haqida bosh qotirmaysiz\n"
            "✔️ tekshiruvlardan xotirjam o'tasiz (100% qabul bo'ladi)\n\n"
            "✅ <b>Natija:</b> xavfsiz va qonuniy yuritiladigan biznes, tekshiruvlarda 100% o'tish."
        ),
        "ru": (
            "🧾 <b>Налоговая отчетность</b>\n\n"
            "Ошибки в налогах — это штрафы, проверки и стресс.\n"
            "<b>Реальный пример:</b> одна ошибка может стоить штраф до 50 млн сум\n\n"
            "Мы (от 5-7 дней):\n"
            "• готовим отчетность на 100% в установленные сроки\n"
            "• сдаем ее в полном соответствии с законом (0 ошибок)\n"
            "• предотвращаем штрафы и проблемы (проверка 14 дней)\n\n"
            "Вы:\n"
            "✔️ не переживаете из-за налогов\n"
            "✔️ спокойно проходите проверки (100% успешно)\n\n"
            "✅ <b>Результат:</b> безопасный и законный бизнес, 100% успешные проверки."
        ),
    },

    "acc_reports": {
        "uz": (
            "📑 <b>Moliyaviy hisobotlar</b>\n\n"
            "Biznes holatini aniq ko'rish uchun hisobotlar muhim.\n"
            "<b>Haqiqiy misol:</b> bank 85% qarz qabul qilmas-u, hisobotlar bo'lmasa\n\n"
            "Biz (14 kunlik davrda):\n"
            "• oylik, choraklik va yillik hisobotlar 100% tayyorlaymiz\n"
            "• biznesning real holatini 100% ko'rsatamiz\n"
            "• rivojlanish va muammo nuqtalarini 30-40% aniqlaymiz\n\n"
            "Bu hisobotlar:\n"
            "✔️ rahbar uchun aniq qarorlar qabul qilishga yordam beradi\n"
            "✔️ investor va banklar uchun ishonch yaratadi (85% qabul bo'ladi)\n\n"
            "✅ <b>Natija:</b> biznesingiz raqamlar orqali boshqariladi, bank qarz 85% qabul."
        ),
        "ru": (
            "📑 <b>Финансовые отчеты</b>\n\n"
            "Чтобы видеть реальное состояние бизнеса, нужны отчеты.\n"
            "<b>Реальный пример:</b> без отчетов банк 85% одобрит кредит\n\n"
            "Мы (в течение 14 дней):\n"
            "• готовим месячные, квартальные и годовые отчеты на 100%\n"
            "• показываем реальную картину бизнеса на 100%\n"
            "• выявляем точки роста на 30-40%\n\n"
            "Эти отчеты:\n"
            "✔️ помогают руководителю принимать точные решения\n"
            "✔️ повышают доверие инвесторов и банков (85% одобрения)\n\n"
            "✅ <b>Результат:</b> управление бизнесом на основе цифр, 85% кредитов одобрены."
        ),
    },

    "acc_consult": {
        "uz": (
            "🧠 <b>Buxgalteriya konsultatsiyasi</b>\n\n"
            "Qanday tizim foydaliroq? Qanday ishlash xavfsiz?\n"
            "<b>Haqiqiy misol:</b> 50% kompaniya sof tizimda 50% hisobda sarmoya isrofi qiladi\n\n"
            "Biz (5-7 kundan):\n"
            "• biznesingizni 100% chuqur tahlil qilamiz\n"
            "• individual maslahat beramiz (2-3 variantni)  \n"
            "• eng to'g'ri buxgalteriya yechimini taklif qilamiz (20-35% tejamkorlik)\n\n"
            "Bu xizmat:\n"
            "✔️ xatolarni oldindan ko'rishga yordam beradi\n"
            "✔️ noto'g'ri qarorlardan saqlaydi (40% xato olmasa)\n\n"
            "✅ <b>Natija:</b> ishonchli va xotirjam rivojlanish, 20-35% tejamkorlik."
        ),
        "ru": (
            "🧠 <b>Бухгалтерская консультация</b>\n\n"
            "Какая система выгоднее? Как работать безопасно?\n"
            "<b>Реальный пример:</b> 50% компаний теряют 20-35% денег на неправильной системе\n\n"
            "Мы (от 5-7 дней):\n"
            "• анализируем ваш бизнес на 100%\n"
            "• даем индивидуальные консультации (2-3 варианта)\n"
            "• предлагаем оптимальное решение (экономия 20-35%)\n\n"
            "Эта услуга:\n"
            "✔️ помогает заранее увидеть ошибки\n"
            "✔️ защищает от неверных решений (избегаем 40% ошибок)\n\n"
            "✅ <b>Результат:</b> уверенное развитие, экономия 20-35%, безопасность."
        ),
    },
}
BROKER_TEXTS = {
    "broker_docs": {
        "uz": (
            "📦 <b>Import hujjatlarini rasmiylashtirish</b>\n\n"
            "Tovar olib kirishda bitta noto'g'ri hujjat — kechikish va jarima degani.\n"
            "<b>Haqiqiy misol:</b> 3 kunlik kechikish = 150-200 million zarara qadar\n\n"
            "Biz (7 kundan):\n"
            "• import uchun zarur barcha hujjatlarni 100% aniqlaymiz\n"
            "• hujjatlarni qonunchilikka mos rasmiylashtiramiz (0 xato)\n"
            "• bojxona talablariga to'liq moslab topshiramiz (14 kunlik ishlash)\n\n"
            "Bu xizmat:\n"
            "✔️ tovarlaringiz ushlanib qolmasligini ta'minlaydi (100% o'tish)\n"
            "✔️ vaqt va ortiqcha xarajatlarni tejaydi (20-30% vaqt tejamkorlik)\n\n"
            "✅ <b>Natija:</b> import jarayoni tez, xavfsiz va muammosiz, 0 xato, 100% o'tish."
        ),
        "ru": (
            "📦 <b>Оформление импортных документов</b>\n\n"
            "Одна ошибка в документах — задержка и штраф.\n"
            "<b>Реальный пример:</b> 3 дня задержки = убыток 150-200 млн сум\n\n"
            "Мы (от 7 дней):\n"
            "• определяем полный перечень необходимых документов на 100%\n"
            "• оформляем их в соответствии с законодательством (0 ошибок)\n"
            "• подаем документы с учетом всех требований таможни (14 дней работы)\n\n"
            "Эта услуга:\n"
            "✔️ предотвращает задержку товара (100% прохождение)\n"
            "✔️ экономит время на 20-30% и лишние расходы\n\n"
            "✅ <b>Результат:</b> быстрый импорт, 0 ошибок, 100% успех, экономия времени на 20-30%."
        ),
    },

    "broker_customs": {
        "uz": (
            "🛃 <b>Bojxona deklaratsiyasi</b>\n\n"
            "Bojxona deklaratsiyasidagi xato — tovarning ushlanishi yoki jarima.\n"
            "<b>Haqiqiy misol:</b> 1 xato = 100-150 million jarima yoki 7-14 kunlik kechikish\n\n"
            "Biz (5 kundan):\n"
            "• deklaratsiyani 100% to'g'ri va aniq rasmiylashtiramiz\n"
            "• kodlar va toifalarni 100% to'g'ri tanlaymiz\n"
            "• bojxona jarayonini 30-40% tezlashtiramiz\n\n"
            "Bu xizmat:\n"
            "✔️ bojxona nazoratidan muammosiz o'tishga yordam beradi (100% o'tish)\n"
            "✔️ ortiqcha to'lovlarni 0 ga kamaytiradi\n\n"
            "✅ <b>Natija:</b> tezkor va qonuniy bojxona rasmiylashtiruvi, 100% o'tish, 0 xato."
        ),
        "ru": (
            "🛃 <b>Таможенная декларация</b>\n\n"
            "Ошибка в декларации — задержка товара или штраф.\n"
            "<b>Реальный пример:</b> одна ошибка = штраф 100-150 млн или задержка 7-14 дней\n\n"
            "Мы (от 5 дней):\n"
            "• оформляем декларацию точно на 100%\n"
            "• правильно подбираем коды на 100%\n"
            "• ускоряем прохождение таможни на 30-40%\n\n"
            "Эта услуга:\n"
            "✔️ обеспечивает беспрепятственное прохождение на 100%\n"
            "✔️ снижает лишние платежи на 100%\n\n"
            "✅ <b>Результат:</b> законное и быстрое оформление, 100% успех, 0 штрафов."
        ),
    },

    "broker_cert": {
        "uz": (
            "📜 <b>Sertifikat va ruxsatnomalarni olish</b>\n\n"
            "Ruxsatnomasiz tovar — katta huquqiy muammo.\n"
            "<b>Haqiqiy misol:</b> sertifikatsiz 5 million rubl tovar taqiqlanishi oddiy\n\n"
            "Biz (14 kundan):\n"
            "• qaysi sertifikat va ruxsatnoma kerakligini 100% aniqlaymiz\n"
            "• ularni olish jarayonini 40% tezlashtiramiz\n"
            "• hujjatlarni 100% to'liq tayyorlab beramiz\n\n"
            "Bu xizmat:\n"
            "✔️ tekshiruvlarda muammosiz o'tishni ta'minlaydi (100% o'tish)\n"
            "✔️ savdoni 100% qonuniy qiladi\n\n"
            "✅ <b>Natija:</b> xotirjam va qonuniy savdo faoliyati, 100% ruxsatli, 14 kundan ruxsat."
        ),
        "ru": (
            "📜 <b>Получение сертификатов и разрешений</b>\n\n"
            "Товар без разрешений — серьезный юридический риск.\n"
            "<b>Реальный пример:</b> без сертификата конфискация товара стоит 5 млн сум\n\n"
            "Мы (от 14 дней):\n"
            "• определяем необходимые сертификаты на 100%\n"
            "• ускоряем процесс получения на 40%\n"
            "• полностью подготавливаем документы\n\n"
            "Эта услуга:\n"
            "✔️ гарантирует успешное прохождение проверок на 100%\n"
            "✔️ делает торговлю легальной на 100%\n\n"
            "✅ <b>Результат:</b> законная торговля, все сертификаты получены за 14 дней, 100% легальность."
        ),
    },

    "broker_contract": {
        "uz": (
            "📝 <b>Shartnomalarni tekshirish va tayyorlash</b>\n\n"
            "Noto'g'ri shartnoma — katta moliyaviy xavf.\n"
            "<b>Haqiqiy misol:</b> noto'g'ri shartnoma 500 million zarariga qadar bo'ladi\n\n"
            "Biz (7 kundan):\n"
            "• shartnomalarni professional 100% tahlil qilamiz\n"
            "• xavfli bandlarni 100% aniqlaymiz (50-100 ta nuqta tekshiramiz)\n"
            "• manfaatlaringizni himoya qiladigan shartnoma tayyorlaymiz (100% qo'llab-quvvatlash)\n\n"
            "Bu xizmat:\n"
            "✔️ kelishmovchiliklarning oldini oladi (100% himoya)\n"
            "✔️ huquqiy xavfsizlikni ta'minlaydi (500 million gacha himoya)\n\n"
            "✅ <b>Natija:</b> ishonchli va himoyalangan bitimlar, 100% manfaat himoyasi."
        ),
        "ru": (
            "📝 <b>Проверка и подготовка договоров</b>\n\n"
            "Неправильный договор — серьезный финансовый риск.\n"
            "<b>Реальный пример:</b> неправильный договор стоит убыток до 500 млн сум\n\n"
            "Мы (от 7 дней):\n"
            "• профессионально анализируем договоры на 100%\n"
            "• выявляем рисковые пункты на 100% (50-100 критических точек)\n"
            "• готовим договор с защитой ваших интересов (100% защита)\n\n"
            "Эта услуга:\n"
            "✔️ предотвращает споры на 100%\n"
            "✔️ обеспечивает юридическую безопасность на 500 млн сум\n\n"
            "✅ <b>Результат:</b> надежные договоры, полная защита интересов, 100% правовая безопасность."
        ),
    },

    "broker_logistics": {
        "uz": (
            "🚚 <b>Tovarni rasmiy olib kirish / chiqarish</b>\n\n"
            "Noto'g'ri rasmiylashtirish — tovar yo'qotilishi yoki jarima.\n"
            "<b>Haqiqiy misol:</b> noto'g'ri rasmiylashtirish = 7-14 kunlik kechikish va 100-200 million jarima\n\n"
            "Biz (7-10 kundan):\n"
            "• tovarni 100% qonuniy va rasmiy yo'l bilan olib kiramiz yoki chiqaramiz\n"
            "• barcha hujjatlarni 100% to'g'ri yuritamiz\n"
            "• jarayonni 100% to'liq nazorat qilamiz (har kunni report)\n\n"
            "Bu xizmat:\n"
            "✔️ xavfsiz va tezkor logistika yaratadi (7-10 kundan)\n"
            "✔️ muammosiz savdoni ta'minlaydi (100% o'tish)\n\n"
            "✅ <b>Natija:</b> tovaringiz xavfsiz va qonuniy harakatlanadi, 7-10 kundan tayyar, 100% o'tish."
        ),
        "ru": (
            "🚚 <b>Официальный ввоз / вывоз товара</b>\n\n"
            "Неправильное оформление — риск потери товара или штрафа.\n"
            "<b>Реальный пример:</b> неправильное оформление = задержка 7-14 дней и штраф 100-200 млн\n\n"
            "Мы (от 7-10 дней):\n"
            "• организуем официальный и законный ввоз на 100%\n"
            "• ведем всю документацию корректно на 100%\n"
            "• полностью контролируем процесс (ежедневные отчеты)\n\n"
            "Эта услуга:\n"
            "✔️ обеспечивает безопасную логистику (7-10 дней)\n"
            "✔️ гарантирует бесперебойную торговлю на 100%\n\n"
            "✅ <b>Результат:</b> законный импорт за 7-10 дней, 100% безопасность, 0 проблем."
        ),
    },

    "broker_consult": {
        "uz": (
            "🧠 <b>Brokerlik konsultatsiyasi</b>\n\n"
            "Qaysi yo'l xavfsizroq? Qanday rasmiylashtirish foydaliroq?\n"
            "<b>Haqiqiy misol:</b> to'g'ri maslahat = 50% vaqt va 30% xarajat tejamkorlik\n\n"
            "Biz (5-7 kundan):\n"
            "• holatingizni 100% chuqur tahlil qilamiz\n"
            "• individual maslahat beramiz (3-5 variantni)\n"
            "• eng xavfsiz va tejamkor yechimni taklif qilamiz (30-40% tejamkorlik)\n\n"
            "Bu xizmat:\n"
            "✔️ xatolarni oldindan ko'rishga yordam beradi (100% ko'rishlik)\n"
            "✔️ risklarni 50% gacha kamaytiradi\n\n"
            "✅ <b>Natija:</b> ishonchli tashqi savdo faoliyati, 30-40% tejamkorlik, 50% risk kamaytirish."
        ),
        "ru": (
            "🧠 <b>Брокерская консультация</b>\n\n"
            "Какой путь безопаснее? Как оформить выгоднее?\n"
            "<b>Реальный пример:</b> правильная консультация экономит 50% времени и 30% расходов\n\n"
            "Мы (от 5-7 дней):\n"
            "• глубоко анализируем вашу ситуацию на 100%\n"
            "• предоставляем индивидуальные консультации (3-5 вариантов)\n"
            "• предлагаем безопасные решения (экономия 30-40%)\n\n"
            "Эта услуга:\n"
            "✔️ помогает заранее избежать ошибок на 100%\n"
            "✔️ снижает риски на 50%\n\n"
            "✅ <b>Результат:</b> надежная внешнеторговая деятельность, экономия 30-40%, риски -50%."
        ),
    },
}
IT_TEXTS = {
    "it_crm": {
        "uz": (
            "🧠 <b>CRM tizimlari</b>\n\n"
            "Mijozlar ko'p, lekin nazorat yo'qmi? Savdo jarayoni tartibsizmi?\n"
            "<b>Haqiqiy misol:</b> CRM siz 150 ta mijozdan 50 tami yo'qotib ketgan\n\n"
            "CRM tizimi orqali (14 kundan boshlab):\n"
            "• barcha mijozlar yagona bazada saqlanadi (100% markazlashtirilgan)\n"
            "• savdo jarayonlari 80% avtomatlashtiriladi\n"
            "• menejerlar faoliyati 100% nazorat qilinadi (har kunni report)\n\n"
            "Biz:\n"
            "✔️ biznesingizga mos CRM yaratamiz (14 kundan tayyar)\n"
            "✔️ hisobot va tahlillarni avtomatlashtiramiz (50% vaqt tejamkorlik)\n"
            "✔️ Telegram bot va to'lov tizimlari bilan integratsiya qilamiz (100% avtomatlash)\n\n"
            "✅ <b>Natija:</b> tartibli savdo, <b>sotuv 40% oshadi</b>, 50 ta yo'qolgan mijozni qaytaramiz."
        ),
        "ru": (
            "🧠 <b>CRM-системы</b>\n\n"
            "Много клиентов, но нет контроля? Продажи хаотичны?\n"
            "<b>Реальный пример:</b> без CRM теряете 50 клиентов из 150 в месяц\n\n"
            "CRM позволяет (от 14 дней):\n"
            "• хранить всех клиентов в единой базе на 100%\n"
            "• автоматизировать продажи на 80%\n"
            "• контролировать менеджеров на 100% (ежедневные отчеты)\n\n"
            "Мы:\n"
            "✔️ разрабатываем CRM за 14 дней\n"
            "✔️ автоматизируем на 50% ручную работу\n"
            "✔️ интегрируем Telegram и платежи на 100%\n\n"
            "✅ <b>Результат:</b> <b>продажи растут на 40%</b>, организованная работа, экономия времени 50%."
        ),
    },

    "it_hrm": {
        "uz": (
            "👨‍💼 <b>HRM tizimi</b>\n\n"
            "Xodimlar bilan bog'liq muammolar ko'p vaqt olyaptimi?\n"
            "<b>Haqiqiy misol:</b> HRM siz oylik 30-40 soat qayta bajarilgan ishni 2 soatga qisqartiradi\n\n"
            "HRM orqali (10 kundan):\n"
            "• xodimlar hisobi 100% avtomatlashtiriladi\n"
            "• ish haqi va faoliyat 100% nazorat qilinadi\n"
            "• hujjatlar avtomatlashtiriladi (95% avtomatlash)\n\n"
            "Biz:\n"
            "✔️ kompaniyangizga mos HRM yaratamiz (10 kundan tayyar)\n"
            "✔️ rahbar uchun qulay panel beramiz (har kunni report)\n"
            "✔️ inson omili sabab xatolarni 90% kamaytiramiz\n\n"
            "✅ <b>Natija:</b> intizomli jamoa, 30-40 soatlik vaqt tejamkorlik, 90% xata kamaytirish."
        ),
        "ru": (
            "👨‍💼 <b>HRM-система</b>\n\n"
            "Проблемы с персоналом отнимают много времени?\n"
            "<b>Реальный пример:</b> HRM сокращает рутинную работу с кадрами с 30-40 часов до 2 часов в месяц\n\n"
            "HRM позволяет (от 10 дней):\n"
            "• вести учет на 100% автоматизированно\n"
            "• контролировать зарплаты на 100%\n"
            "• автоматизировать документы на 95%\n\n"
            "Мы:\n"
            "✔️ разрабатываем HRM за 10 дней\n"
            "✔️ даем удобную панель для руководителя\n"
            "✔️ уменьшаем ошибки на 90%\n\n"
            "✅ <b>Результат:</b> дисциплинированная команда, сэкономлено 30-40 часов, ошибки -90%."
        ),
    },

    "it_bot": {
        "uz": (
            "🤖 <b>Telegram botlar</b>\n\n"
            "Mijozlarga doimiy javob berish qiyinmi?\n"
            "<b>Haqiqiy misol:</b> Telegram bot siz 500 soatlik operatornig ishini 10 soatga qisqartiradi\n\n"
            "Telegram bot orqali (7-10 kundan):\n"
            "• murojaatlar va buyurtmalar 95% avtomatik qabul qilinadi\n"
            "• 24/7 aloqa 100% yo'lga qo'yiladi\n"
            "• operatorlar yuklamasi 90% kamayadi\n\n"
            "Biz:\n"
            "✔️ maxsus bot ishlab chiqamiz (7-10 kundan tayyar)\n"
            "✔️ CRM va to'lov tizimlari bilan bog'laymiz (100% integratsiya)\n"
            "✔️ admin va operator paneli qo'shamiz (50+ funksiya)\n\n"
            "✅ <b>Natija:</b> <b>sotuv avtomatlashtiriladi 95%</b>, 24/7 aloqa, 500 soatlik tejamkorlik."
        ),
        "ru": (
            "🤖 <b>Telegram-боты</b>\n\n"
            "Сложно постоянно отвечать клиентам?\n"
            "<b>Реальный пример:</b> бот сокращает ручную работу операторов с 500 часов до 10 часов в месяц\n\n"
            "Telegram-бот (от 7-10 дней):\n"
            "• принимает заявки автоматически на 95%\n"
            "• работает 24/7 на 100%\n"
            "• снижает нагрузку операторов на 90%\n\n"
            "Мы:\n"
            "✔️ создаем бота за 7-10 дней\n"
            "✔️ интегрируем CRM на 100%\n"
            "✔️ добавляем админ панель с 50+ функциями\n\n"
            "✅ <b>Результат:</b> <b>автоматизировано 95% продаж</b>, 24/7 сервис, сэкономлено 500 часов."
        ),
    },

    "it_web": {
        "uz": (
            "🌐 <b>Veb-saytlar va platformalar</b>\n\n"
            "Agar saytingiz bo'lmasa — sizni internetda topishmaydi.\n"
            "<b>Haqiqiy misol:</b> veb-sayt siz 70% ko'proq mijoz oladi\n\n"
            "Biz (14-21 kundan):\n"
            "• zamonavoy dizayn yaratamiz (mobil optimizatsiya 100%)\n"
            "• korporativ va sotuvga yo'naltirilgan saytlar qilamiz (SEO optimizatsiya)\n"
            "• barcha qurilmalarga moslaymiz (responsive 100%)\n\n"
            "✅ <b>Natija:</b> internetda ishonchli imij, <b>70% ko'proq mijoz</b> oladi, 14-21 kundan tayyar."
        ),
        "ru": (
            "🌐 <b>Веб-сайты и платформы</b>\n\n"
            "Если у вас нет сайта — вас не найдут в интернете.\n"
            "<b>Реальный пример:</b> сайт привлекает 70% больше клиентов\n\n"
            "Мы (от 14-21 дней):\n"
            "• создаем современный дизайн (100% мобильная оптимизация)\n"
            "• делаем продающие сайты (SEO оптимизация)\n"
            "• адаптируем под все устройства на 100%\n\n"
            "✅ <b>Результат:</b> надежный онлайн-имидж, <b>70% больше клиентов</b> с интернета, готов за 14-21 день."
        ),
    },

    "it_internet": {
        "uz": (
            "🛒 <b>Internet do'konlar</b>\n\n"
            "Onlayn savdo qilmaslik — imkoniyatni yo'qotish demak.\n"
            "<b>Haqiqiy misol:</b> onlayn do'kon siz sotuv 3-5 baravar oshadi\n\n"
            "Biz (14-21 kundan):\n"
            "• tez va qulay do'kon yaratamiz (loading 2-3 sekunda)\n"
            "• buyurtma va to'lovlarni avtomatlashtiramiz (100% avtomatlash)\n"
            "• yetkazib berishni integratsiya qilamiz (5+ hizmatlar)\n\n"
            "✅ <b>Natija:</b> <b>sotuv 3-5 baravar oshadi</b>, 24/7 avtomatlashtirilgan savdo, 14-21 kundan online."
        ),
        "ru": (
            "🛒 <b>Интернет-магазины</b>\n\n"
            "Отказ от онлайн-продаж — потеря возможностей.\n"
            "<b>Реальный пример:</b> онлайн магазин увеличивает продажи в 3-5 раз\n\n"
            "Мы (от 14-21 дней):\n"
            "• создаем быстрые магазины (загрузка 2-3 сек)\n"
            "• автоматизируем заказы на 100%\n"
            "• интегрируем доставку (5+ сервисов)\n\n"
            "✅ <b>Результат:</b> <b>продажи растут в 3-5 раз</b>, полная автоматизация, готов за 14-21 день."
        ),
    },

    "it_marketplace": {
        "uz": (
            "🏬 <b>Marketplace platformalar</b>\n\n"
            "Bir nechta sotuvchi — bitta platformada.\n"
            "<b>Haqiqiy misol:</b> marketplace 100+ sotuvchini boshqaradi, 500+ mahsulot\n\n"
            "Biz (21-30 kundan):\n"
            "• marketplace tizimlar yaratamiz (100+ sotuvchi imkoniyati)\n"
            "• sotuvchi va xaridorlar uchun qulay interfeys qilamiz (interface 50+ funksiya)\n"
            "• to'lov va buyurtmalarni avtomatlashtiramiz (100% avtomatlash)\n\n"
            "✅ <b>Natija:</b> kengayishga tayyor platforma, 100+ sotuvchi imkoniyati, 21-30 kundan ready."
        ),
        "ru": (
            "🏬 <b>Маркетплейс платформы</b>\n\n"
            "Несколько продавцов — одна платформа.\n"
            "<b>Реальный пример:</b> маркетплейс управляет 100+ продавцами и 500+ товарами\n\n"
            "Мы (от 21-30 дней):\n"
            "• разрабатываем маркетплейсы (поддержка 100+ продавцов)\n"
            "• создаем удобную систему (50+ функций для пользователей)\n"
            "• автоматизируем заказы на 100%\n\n"
            "✅ <b>Результат:</b> масштабируемый бизнес, поддержка 100+ продавцов, готов за 21-30 дней."
        ),
    },

    "it_mobile": {
        "uz": (
            "📱 <b>Mobil ilovalar</b>\n\n"
            "Mijozlar telefonda — biznes ham telefonda bo'lishi kerak.\n"
            "<b>Haqiqiy misol:</b> mobil ilova siz installmentni 50% oshiradi\n\n"
            "Biz (21-30 kundan):\n"
            "• Android va iOS ilovalar yaratamiz (100% ishlaydigan)\n"
            "• real vaqt monitoring va to'lov qo'shamiz (50+ funksiya)\n\n"
            "✅ <b>Natija:</b> zamonaviy raqamli biznes, <b>installment 50% oshadi</b>, 21-30 kundan ready."
        ),
        "ru": (
            "📱 <b>Мобильные приложения</b>\n\n"
            "Клиенты в телефоне — бизнес тоже должен быть там.\n"
            "<b>Реальный пример:</b> мобильное приложение увеличивает конверсию на 50%\n\n"
            "Мы (от 21-30 дней):\n"
            "• создаем Android и iOS приложения (100% рабочие)\n"
            "• добавляем мониторинг и оплаты (50+ функций)\n\n"
            "✅ <b>Результат:</b> современный цифровой бизнес, <b>конверсия +50%</b>, готово за 21-30 дней."
        ),
    },

    "it_automation": {
        "uz": (
            "⚙️ <b>Biznes jarayonlarni avtomatlashtirish</b>\n\n"
            "Qo'lda ishlar ko'p vaqt olyaptimi?\n"
            "<b>Haqiqiy misol:</b> avtomatlashtirish siz 60% ish vaqtini tejaydi\n\n"
            "Biz (10-14 kundan):\n"
            "• jarayonlarni tahlil qilamiz (50+ bosqichni o'rganamiz)\n"
            "• qo'lda ishlarni 80% avtomatlashtiramiz\n"
            "• xatolarni 85% kamaytiramiz\n\n"
            "✅ <b>Natija:</b> <b>60% ish vaqti tejandi</b>, 80% avtomatlash, 85% xata kamaytirish."
        ),
        "ru": (
            "⚙️ <b>Автоматизация бизнес-процессов</b>\n\n"
            "Ручная работа отнимает много времени?\n"
            "<b>Реальный пример:</b> автоматизация сокращает ручную работу на 60%\n\n"
            "Мы (от 10-14 дней):\n"
            "• анализируем процессы (изучаем 50+ операций)\n"
            "• автоматизируем 80% ручного труда\n"
            "• уменьшаем ошибки на 85%\n\n"
            "✅ <b>Результат:</b> <b>экономия 60% времени</b>, 80% автоматизация, ошибки -85%."
        ),
    },

    "it_payment": {
        "uz": (
            "💳 <b>To'lov tizimlari integratsiyasi</b>\n\n"
            "Qulay to'lov — ko'proq sotuv.\n"
            "<b>Haqiqiy misol:</b> to'lov integratsiyasi sotuv 35-40% oshadi\n\n"
            "Biz (5-7 kundan):\n"
            "• Click, Payme, Uzum va bank to'lovlarini ulaymiz (100% integratsiya)\n"
            "• xavfsiz va tezkor tizim yaratamiz (sertifikat 100%)\n\n"
            "✅ <b>Natija:</b> <b>sotuv 35-40% oshadi</b>, qulay to'lov, 5-7 kundan ready."
        ),
        "ru": (
            "💳 <b>Интеграция платежных систем</b>\n\n"
            "Удобная оплата — больше продаж.\n"
            "<b>Реальный пример:</b> интеграция платежей увеличивает продажи на 35-40%\n\n"
            "Мы (от 5-7 дней):\n"
            "• подключаем Click, Payme, Uzum на 100%\n"
            "• создаем безопасную систему (сертифицировано)\n\n"
            "✅ <b>Результат:</b> <b>продажи +35-40%</b>, быстрые платежи, готово за 5-7 дней."
        ),
    },

    "it_tech": {
        "uz": (
            "🔧 <b>Texnik qo'llab-quvvatlash va IT konsultatsiya</b>\n\n"
            "Tizim ishlamasa — biznes to'xtaydi.\n"
            "<b>Haqiqiy misol:</b> texnik qo'llab-quvvatlash 99.9% uptime ta'minlaydi\n\n"
            "Biz (doimiy):\n"
            "• texnik muammolarni 2 soatda hal qilamiz (24/7 support)\n"
            "• tizimlarni doimiy nazorat qilamiz (har minutda check)\n"
            "• rivojlanish bo'yicha maslahat beramiz (monthly consultation)\n\n"
            "✅ <b>Natija:</b> barqaror infrastruktura, 99.9% uptime, 24/7 doomiy qo'llab-quvvatlash."
        ),
        "ru": (
            "🔧 <b>Техническая поддержка и IT-консультации</b>\n\n"
            "Если система не работает — бизнес останавливается.\n"
            "<b>Реальный пример:</b> техподдержка обеспечивает 99.9% uptime\n\n"
            "Мы (постоянно):\n"
            "• быстро решаем проблемы (в течение 2 часов, 24/7)\n"
            "• контролируем системы (проверка каждую минуту)\n"
            "• консультируем по развитию (ежемесячно)\n\n"
            "✅ <b>Результат:</b> стабильная IT-инфраструктура, 99.9% uptime, 24/7 поддержка."
        ),
    },
}
SERVICE_4_TEXTS = {
    "service_4_1": {
        "uz": (
            "📊 <b>Buxgalteriya bo'yicha treninglar</b>\n\n"
            "Xodimlar xatolari moliyaviy yo'qotishlarga olib kelayaptimi?\n"
            "<b>Haqiqiy misol:</b> treningdan keyin xodimlar xatalari 80% kamayadi\n\n"
            "Ushbu trening (5 kundan):\n"
            "• buxgalteriya asoslari chuqur o'rgatiladi (40+ soat)\n"
            "• real amaliy misollar bilan ishlanadi (20+ case study)\n"
            "• xatolarni oldindan ko'rish ko'nikmasi shakllanadi (100% o'rgatish)\n\n"
            "Biz:\n"
            "✔️ zamonaviy qonunchilik asosida o'qitamiz (2024-2025 yangiliklari)\n"
            "✔️ nazariya va amaliyotni 50-50 birlashtiramiz\n\n"
            "✅ <b>Natija:</b> xodim xatalari 80% kamayadi, ishonchli buxgalter 5-7 kundan tayyar."
        ),
        "ru": (
            "📊 <b>Тренинги по бухгалтерскому учёту</b>\n\n"
            "Ошибки сотрудников приводят к финансовым потерям?\n"
            "<b>Реальный пример:</b> после тренинга ошибки сотрудников падают на 80%\n\n"
            "На тренинге (от 5 дней):\n"
            "• изучаются основы бухгалтерии (40+ часов)\n"
            "• разбираются реальные кейсы (20+ примеров)\n"
            "• формируется навык предотвращения (обучение 100%)\n\n"
            "Мы:\n"
            "✔️ обучаем по актуальному закону (обновления 2024-2025)\n"
            "✔️ совмещаем теорию 50% и практику 50%\n\n"
            "✅ <b>Результат:</b> ошибки -80%, уверенный бухгалтер, тренинг за 5-7 дней."
        ),
    },

    "service_4_2": {
        "uz": (
            "📣 <b>Savdo va marketing treninglari</b>\n\n"
            "Yaxshi mahsulot bor, lekin sotuv pastmi?\n"
            "<b>Haqiqiy misol:</b> treningdan keyin sotuvchi 50% ko'proq sotuv qiladi\n\n"
            "Biz (7-10 kundan):\n"
            "• mijoz bilan to'g'ri ishlashni o'rgatamiz (50+ texnika)\n"
            "• savdo texnikalarini amalda ko'rsatamiz (20+ praktika)\n"
            "• marketing fikrlashni shakllantiramiz (15+ strategy)\n\n"
            "Bu trening:\n"
            "✔️ sotuvchilarni 50% kuchaytiradi\n"
            "✔️ daromadni 35-45% oshiradi\n\n"
            "✅ <b>Natija:</b> <b>sotuv 50% oshadi</b>, <b>daromad 35-45% oshadi</b>, faol jamoa."
        ),
        "ru": (
            "📣 <b>Тренинги по продажам и маркетингу</b>\n\n"
            "Хороший продукт есть, а продажи низкие?\n"
            "<b>Реальный пример:</b> после тренинга продавец увеличивает продажи на 50%\n\n"
            "Мы (от 7-10 дней):\n"
            "• учим правильной работе (50+ техник)\n"
            "• показываем техники продаж на практике (20+ кейсов)\n"
            "• формируем маркетинговое мышление (15+ стратегий)\n\n"
            "Тренинг:\n"
            "✔️ усиливает продавцов на 50%\n"
            "✔️ увеличивает доход на 35-45%\n\n"
            "✅ <b>Результат:</b> <b>продажи +50%</b>, <b>доход +35-45%</b>, эффективная команда."
        ),
    },

    "service_4_3": {
        "uz": (
            "🧭 <b>Menejment va boshqaruv ko'nikmalari</b>\n\n"
            "Rahbar bor, lekin tizim yo'qmi?\n"
            "<b>Haqiqiy misol:</b> treningdan keyin rahbar 70% tezroq qaror qabul qiladi\n\n"
            "Biz (10-14 kundan):\n"
            "• to'g'ri rejalashtirishni o'rgatamiz (30+ method)\n"
            "• jamoani boshqarish usullarini ko'rsatamiz (25+ texnika)\n"
            "• mas'uliyat va nazoratni tizimlashtiramiz (100% nazorat)\n\n"
            "Bu trening:\n"
            "✔️ rahbarlik salohiyatini 70% oshiradi\n"
            "✔️ ichki tartibni 80% mustahkamlaydi\n\n"
            "✅ <b>Natija:</b> <b>qaror 70% tezroq</b>, tartibli va samarali jamoa."
        ),
        "ru": (
            "🧭 <b>Навыки менеджмента и управления</b>\n\n"
            "Есть руководитель, но нет системы?\n"
            "<b>Реальный пример:</b> после тренинга лидер принимает решения на 70% быстрее\n\n"
            "Мы (от 10-14 дней):\n"
            "• обучаем планированию (30+ методов)\n"
            "• показываем методы управления (25+ техник)\n"
            "• систематизируем контроль (100% контроль)\n\n"
            "Тренинг:\n"
            "✔️ развивает навыки на 70%\n"
            "✔️ укрепляет порядок на 80%\n\n"
            "✅ <b>Результат:</b> <b>решения на 70% быстрее</b>, управляемая эффективная команда."
        ),
    },

    "service_4_4": {
        "uz": (
            "💻 <b>IT va raqamli savodxonlik treninglari</b>\n\n"
            "Xodimlar texnologiyadan to'liq foydalana olmayaptimi?\n"
            "<b>Haqiqiy misol:</b> treningdan keyin xodimlar produktivligi 60% oshadi\n\n"
            "Biz (5-7 kundan):\n"
            "• kompyuter va raqamli vositalarni o'rgatamiz (30+ tool)\n"
            "• CRM va online tizimlar bilan ishlashni ko'rsatamiz (20+ platform)\n"
            "• texnologiyadan samarali foydalanishni o'rgatamiz (100% tajriba)\n\n"
            "✅ <b>Natija:</b> <b>produktivlik 60% oshadi</b>, zamonaviy raqamli fikrlaydigan xodimlar."
        ),
        "ru": (
            "💻 <b>IT-тренинги и цифровая грамотность</b>\n\n"
            "Сотрудники не умеют эффективно использовать технологии?\n"
            "<b>Реальный пример:</b> после тренинга продуктивность сотрудников растет на 60%\n\n"
            "Мы (от 5-7 дней):\n"
            "• обучаем работе с компьютером (30+ инструментов)\n"
            "• показываем CRM и системы (20+ платформ)\n"
            "• повышаем цифровую эффективность (100% применение)\n\n"
            "✅ <b>Результат:</b> <b>продуктивность +60%</b>, цифрово грамотные сотрудники."
        ),
    },

    "service_4_5": {
        "uz": (
            "👥 <b>HR va kadrlar boshqaruvi bo'yicha o'qitish</b>\n\n"
            "Xodimlarni tanlash va saqlab qolish muammo bo'lyaptimi?\n"
            "<b>Haqiqiy misol:</b> HR treningidan keyin xodim chiqib ketishi 40% kamayadi\n\n"
            "Biz (7-10 kundan):\n"
            "• HR tizimini o'rgatamiz (25+ protsess)\n"
            "• baholash va motivatsiya usullarini ko'rsatamiz (20+ method)\n"
            "• hujjatlar bilan ishlashni tushuntiramiz (30+ hujjat turi)\n\n"
            "✅ <b>Natija:</b> xodim chiqib ketishi 40% kamayadi, <b>kuchli va barqaror jamoa</b>."
        ),
        "ru": (
            "👥 <b>Обучение HR и управлению персоналом</b>\n\n"
            "Проблемы с подбором и удержанием сотрудников?\n"
            "<b>Реальный пример:</b> после HR-тренинга текучесть падает на 40%\n\n"
            "Мы (от 7-10 дней):\n"
            "• обучаем HR-системам (25+ процессов)\n"
            "• показываем методы оценки (20+ методик)\n"
            "• объясняем кадровые процессы (30+ документов)\n\n"
            "✅ <b>Результат:</b> текучесть -40%, <b>сильная стабильная команда</b>."
        ),
    },

    "service_4_6": {
        "uz": (
            "🏢 <b>Korporativ treninglar</b>\n\n"
            "Jamoa bor, lekin hamjihatlik yo'qmi?\n"
            "<b>Haqiqiy misol:</b> korporativ treningdan keyin jamoa 80% hamjihat bo'ladi\n\n"
            "Biz (10-14 kundan):\n"
            "• kompaniya ehtiyojiga mos trening o'tkazamiz (custom tuzilish)\n"
            "• jamoaviy ishlashni rivojlantiramiz (20+ aktivitas)\n"
            "• ichki muammolarni aniqlaymiz va hal qilamiz (90% muammoni echamiz)\n\n"
            "✅ <b>Natija:</b> <b>jamoa 80% hamjihat</b>, bir maqsad sari ishlaydigan kuchli jamoa."
        ),
        "ru": (
            "🏢 <b>Корпоративные тренинги</b>\n\n"
            "Есть команда, но нет сплоченности?\n"
            "<b>Реальный пример:</b> после корпоративного тренинга сплоченность растет на 80%\n\n"
            "Мы (от 10-14 дней):\n"
            "• проводим тренинги под задачи компании (индивидуальный подход)\n"
            "• развиваем командную работу (20+ активностей)\n"
            "• выявляем и решаем проблемы (решаем 90% проблем)\n\n"
            "✅ <b>Результат:</b> <b>сплоченность +80%</b>, сильная организованная команда."
        ),
    },

    "service_4_7": {
        "uz": (
            "🧠 <b>Individual konsultatsiya va coaching</b>\n\n"
            "Professional yoki rahbar sifatida o'sishni xohlaysizmi?\n"
            "<b>Haqiqiy misol:</b> coaching natijasida rahbar samaradorligi 75% oshadi\n\n"
            "Biz (5-10 seans):\n"
            "• individual tahlil qilamiz (chuqur interview)\n"
            "• shaxsiy rivojlanish rejasini tuzamiz (3-6 oylik plan)\n"
            "• qaror qabul qilishni kuchaytiramiz (leadership style)\n\n"
            "✅ <b>Natija:</b> <b>samaradorlik 75% oshadi</b>, ishonchli qaror qabul qiladigan mutaxassis."
        ),
        "ru": (
            "🧠 <b>Индивидуальные консультации и коучинг</b>\n\n"
            "Хотите профессионального роста?\n"
            "<b>Реальный пример:</b> после коучинга эффективность лидера растет на 75%\n\n"
            "Мы (5-10 сеансов):\n"
            "• проводим персональный анализ (глубокое интервью)\n"
            "• составляем план развития (3-6 месяцев)\n"
            "• усиливаем навыки принятия решений (лидерство)\n\n"
            "✅ <b>Результат:</b> <b>эффективность +75%</b>, уверенный и сильный специалист."
        ),
    },
}
SERVICE_5_TEXTS = {
    "service_5_1": {
        "uz": (
            "🔍 <b>Litsenziya talablarini tahlil qilish</b>\n\n"
            "Qaysi hujjatlar kerak? Qanday shartlar bajarilishi lozim?\n"
            "<b>Haqiqiy misol:</b> to'g'ri tahlil siz 30% vaqt va xarajat tejaydi\n\n"
            "Biz (5 kundan):\n"
            "• faoliyatingizni 100% chuqur o'rganamiz (har detalni)\n"
            "• aynan sizga kerak bo'lgan talablarni aniqlaymiz (0 ortiqcha)\n"
            "• noto'g'ri yoki ortiqcha talablarni oldindan bartaraf etamiz (90% xato yo'q)\n\n"
            "Bu xizmat:\n"
            "✔️ vaqtni 30% tejaydi\n"
            "✔️ rad etilish xavfini 80% kamaytiradi\n\n"
            "✅ <b>Natija:</b> aniq reja, 30% vaqt tejamkorlik, xatosiz boshlang'ich bosqich."
        ),
        "ru": (
            "🔍 <b>Анализ лицензионных требований</b>\n\n"
            "Какие документы нужны? Какие условия необходимо выполнить?\n"
            "<b>Реальный пример:</b> правильный анализ экономит 30% времени и средств\n\n"
            "Мы (от 5 дней):\n"
            "• подробно изучаем вашу деятельность на 100% (каждый нюанс)\n"
            "• определяем точные требования (0 излишних)\n"
            "• заранее устраняем ошибки (избегаем 90% проблем)\n\n"
            "Эта услуга:\n"
            "✔️ экономит 30% времени\n"
            "✔️ снижает риск отказа на 80%\n\n"
            "✅ <b>Результат:</b> четкий план, экономия 30%, правильный старт."
        ),
    },

    "service_5_2": {
        "uz": (
            "📑 <b>Hujjatlarni tayyorlash</b>\n\n"
            "Litsenziya olishda eng ko'p xato hujjatlarda bo'ladi.\n"
            "<b>Haqiqiy misol:</b> to'g'ri tayyorlangan hujjatlar 95% qabul bo'ladi\n\n"
            "Biz (7-10 kundan):\n"
            "• barcha zarur hujjatlarni 100% ro'yxatini shakllantiramiz (0 yo'qotish)\n"
            "• hujjatlarni qonunchilikka mos tayyorlaymiz (100% moslik)\n"
            "• kamchilik va xatolarni oldindan tuzatamiz (0 xato)\n\n"
            "Bu xizmat:\n"
            "✔️ qayta topshirish holatlarini 0% ga kamaytiramiz\n"
            "✔️ jarayonni 50% tezlashtiramiz\n\n"
            "✅ <b>Natija:</b> <b>95% qabul</b>, to'liq mukammal paket, 7-10 kundan tayyar."
        ),
        "ru": (
            "📑 <b>Подготовка документов</b>\n\n"
            "Чаще всего отказ возникает из-за ошибок в документах.\n"
            "<b>Реальный пример:</b> правильно подготовленные документы принимаются в 95% случаев\n\n"
            "Мы (от 7-10 дней):\n"
            "• формируем полный список на 100% (ничего не упускаем)\n"
            "• готовим документы на 100% (полное соответствие)\n"
            "• заранее устраняем ошибки (0 дефектов)\n\n"
            "Эта услуга:\n"
            "✔️ исключает повторную подачу (0% переделок)\n"
            "✔️ ускоряет на 50%\n\n"
            "✅ <b>Результат:</b> <b>95% принятие</b>, полный пакет, готово за 7-10 дней."
        ),
    },

    "service_5_3": {
        "uz": (
            "🏛 <b>Davlat idoralariga topshirish</b>\n\n"
            "Davlat idoralari bilan ishlash ko'p vaqt va asab talab qiladi.\n"
            "<b>Haqiqiy misol:</b> professional topshirish 5-7 kunda qabul bo'ladi, amatyor 30+ kun\n\n"
            "Biz (7-10 kundan):\n"
            "• hujjatlarni tegishli idoralarga o'zimiz topshiramiz (100% shaxsan)\n"
            "• to'g'ri bo'lim va mutasaddilar bilan ishlaymiz (20+ yillik aloqa)\n"
            "• ortiqcha yurishlarni oldini olamiz (100% muammosiz)\n\n"
            "Bu xizmat:\n"
            "✔️ byurokratik muammolardan xalos qiladi (0 kechikish)\n"
            "✔️ vaqtni 80% tejaydi (5-7 kundan vs 30+ kun)\n\n"
            "✅ <b>Natija:</b> tez va to'g'ri topshirish, 5-7 kundan qabul, 80% tejamkorlik."
        ),
        "ru": (
            "🏛 <b>Подача документов в государственные органы</b>\n\n"
            "Работа с госорганами требует времени и нервов.\n"
            "<b>Реальный пример:</b> профессиональная подача принимается за 5-7 дней, самостоятельно 30+ дней\n\n"
            "Мы (от 7-10 дней):\n"
            "• самостоятельно подаем в нужные органы на 100% (лично)\n"
            "• работаем с ответственными (20+ лет контактов)\n"
            "• исключаем лишние хождения (0 проблем)\n\n"
            "Эта услуга:\n"
            "✔️ избавляет от бюрократии полностью (0 забот)\n"
            "✔️ экономит 80% времени (5-7 дней vs 30+ дней)\n\n"
            "✅ <b>Результат:</b> быстро и правильно за 5-7 дней, сэкономлено 80% времени."
        ),
    },

    "service_5_4": {
        "uz": (
            "🔄 <b>Jarayonni to'liq kuzatib borish</b>\n\n"
            "Hujjat topshirildi, lekin javob yo'qmi?\n"
            "<b>Haqiqiy misol:</b> to'liq kuzatish orqali 98% ijobiy natija\n\n"
            "Biz (doimiy):\n"
            "• litsenziya jarayonini boshidan oxirigacha nazorat qilamiz (100% nazorat)\n"
            "• kechikish sabablarini aniqlaymiz (real-time follow-up)\n"
            "• zarur bo'lsa, tezlashtirish choralarini ko'ramiz (50+ aloqa)\n\n"
            "Bu xizmat:\n"
            "✔️ noaniqlikni 100% yo'q qilamiz\n"
            "✔️ doimiy xabardorlikni ta'minlaydi (har 3-5 kunda)\n\n"
            "✅ <b>Natija:</b> <b>98% ijobiy natija</b>, shaffof va nazoratdagi jarayon."
        ),
        "ru": (
            "🔄 <b>Полное сопровождение процесса</b>\n\n"
            "Документы поданы, но нет ответа?\n"
            "<b>Реальный пример:</b> полное сопровождение дает 98% положительного результата\n\n"
            "Мы (постоянно):\n"
            "• контролируем процесс на 100% (каждый день)\n"
            "• выявляем причины задержек (real-time)\n"
            "• ускоряем при необходимости (50+ контактов)\n\n"
            "Эта услуга:\n"
            "✔️ устраняет неопределенность полностью (0% тревоги)\n"
            "✔️ обеспечивает прозрачность (отчет каждые 3-5 дней)\n\n"
            "✅ <b>Результат:</b> <b>98% успех</b>, полный контроль процесса, полная прозрачность."
        ),
    },

    "service_5_5": {
        "uz": (
            "❌➡️✅ <b>Rad etilgan litsenziyalarni qayta tiklash</b>\n\n"
            "Oldin rad etilgan litsenziya — oxiri emas.\n"
            "<b>Haqiqiy misol:</b> qayta topshirishda 85% muvaffaqiyat\n\n"
            "Biz (10-14 kundan):\n"
            "• rad etilish sabablarini 100% tahlil qilamiz (chuqur suvor)\n"
            "• xatolarni to'g'rilaymiz (100% takomil)\n"
            "• hujjatlarni qayta mukammallashtiramiz (2-3 round)\n\n"
            "Bu xizmat:\n"
            "✔️ ikkinchi imkoniyat beradi (85% muvaffaqiyat)\n"
            "✔️ muvaffaqiyat ehtimolini 85%ga oshiradi\n\n"
            "✅ <b>Natija:</b> <b>85% qayta qabul</b>, to'g'ri va qayta topshirilgan ariza."
        ),
        "ru": (
            "❌➡️✅ <b>Восстановление отказанных лицензий</b>\n\n"
            "Отказ — это не конец.\n"
            "<b>Реальный пример:</b> повторная подача дает 85% положительного результата\n\n"
            "Мы (от 10-14 дней):\n"
            "• анализируем причины отказа на 100% (глубокий разбор)\n"
            "• исправляем ошибки полностью (100% правка)\n"
            "• подготавливаем к повторной подаче (2-3 итерации)\n\n"
            "Эта услуга:\n"
            "✔️ дает второй шанс (85% успеха)\n"
            "✔️ повышает вероятность на 85%\n\n"
            "✅ <b>Результат:</b> <b>85% повторного одобрения</b>, правильно переподготовленная заявка."
        ),
    },

    "service_5_6": {
        "uz": (
            "🏷 <b>Sertifikatlash xizmatlari</b>\n\n"
            "Sertifikatsiz faoliyat — katta huquqiy xavf.\n"
            "<b>Haqiqiy misol:</b> sertifikatsiz 100 million rubl tovar taqiqlanib qolishi oddiy\n\n"
            "Biz (14-21 kundan):\n"
            "• kerakli sertifikatlarni 100% aniqlaymiz (har birini)\n"
            "• sertifikatlash jarayonini tashkil qilamiz (100% o'tkazib beramiz)\n"
            "• hujjatlarni tez va to'g'ri rasmiylashtiramiz (20+ sertifikat turi)\n\n"
            "Bu xizmat:\n"
            "✔️ tekshiruvlarda muammosiz o'tishni ta'minlaydi (100% o'tish)\n"
            "✔️ biznesni 100% qonuniy qiladi\n\n"
            "✅ <b>Natija:</b> sertifikatlangan faoliyat, 100% qonuniy, 14-21 kundan tayyar."
        ),
        "ru": (
            "🏷 <b>Сертификационные услуги</b>\n\n"
            "Работа без сертификатов — юридический риск.\n"
            "<b>Реальный пример:</b> без сертификата конфискация может быть 100 млн сум\n\n"
            "Мы (от 14-21 дней):\n"
            "• определяем необходимые сертификаты на 100% (каждый вид)\n"
            "• организуем процесс сертификации (100% проведение)\n"
            "• оформляем быстро и правильно (20+ видов сертификатов)\n\n"
            "Эта услуга:\n"
            "✔️ гарантирует успех на 100% (проверки пройдены)\n"
            "✔️ делает бизнес легальным на 100%\n\n"
            "✅ <b>Результат:</b> сертифицированная деятельность, 100% законность, готово за 14-21 день."
        ),
    },

    "service_5_7": {
        "uz": (
            "⚖️ <b>Konsultatsiya va huquqiy yordam</b>\n\n"
            "Qonunchilikni bilmaslik — risk.\n"
            "<b>Haqiqiy misol:</b> huquqiy maslahat siz 500 million rubllik xatalarni saqlaydi\n\n"
            "Biz (5-7 kundan):\n"
            "• litsenziya va ruxsatnomalar bo'yicha maslahat beramiz (100% coverage)\n"
            "• huquqiy xavflarni tushuntiramiz (20+ risk type)\n"
            "• eng to'g'ri yo'lni ko'rsatamiz (proven strategy)\n\n"
            "Bu xizmat:\n"
            "✔️ xatolarning oldini oladi (100% himoya)\n"
            "✔️ qaror qabul qilishni osonlashtiradi (3-5 variant)\n\n"
            "✅ <b>Natija:</b> <b>500 million rubllik himoya</b>, huquqiy himoyalangan biznes."
        ),
        "ru": (
            "⚖️ <b>Консультации и правовая поддержка</b>\n\n"
            "Незнание закона — это риск.\n"
            "<b>Реальный пример:</b> правовая консультация защищает от ошибок на 500 млн сум\n\n"
            "Мы (от 5-7 дней):\n"
            "• консультируем по лицензиям на 100% (полное покрытие)\n"
            "• объясняем риски (20+ типов рисков)\n"
            "• предлагаем оптимальное решение (3-5 вариантов)\n\n"
            "Эта услуга:\n"
            "✔️ предотвращает ошибки на 100% (полная защита)\n"
            "✔️ упрощает принятие решений (четкие варианты)\n\n"
            "✅ <b>Результат:</b> <b>защита 500 млн сум</b>, юридически защищенный бизнес."
        ),
    },
}
SERVICE_6_TEXTS = {
    "service_6_1": {
        "uz": (
            "🔌 <b>Energiya iste'molini tahlil qilish</b>\n\n"
            "Elektr va energiya xarajatlari nazoratsiz ketayaptimi?\n"
            "<b>Haqiqiy misol:</b> tahlil orqali 30-40% ortiqcha sarf aniqlash mumkin\n\n"
            "Biz (10 kundan):\n"
            "• barcha energiya manbalarini 100% tahlil qilamiz (har bitta aylan)\n"
            "• qayerda va nima sabab ko'p sarf bo'layotganini aniqlaymiz (25+ nuqta)\n"
            "• real raqamlar bilan holatni ko'rsatamiz (detailed report)\n\n"
            "✅ <b>Natija:</b> 30-40% ortiqcha sarf aniqlandi, to'liq va aniq manzara."
        ),
        "ru": (
            "🔌 <b>Анализ энергопотребления</b>\n\n"
            "Расходы на электроэнергию выходят из-под контроля?\n"
            "<b>Реальный пример:</b> анализ выявляет 30-40% скрытого потребления\n\n"
            "Мы (от 10 дней):\n"
            "• анализируем все источники на 100% (каждый канал)\n"
            "• выявляем лишнее потребление на 30-40% (точные цифры)\n"
            "• показываем реальную картину (детальный отчет)\n\n"
            "✅ <b>Результат:</b> выявлено <b>30-40% лишних расходов</b>, полная картина потребления."
        ),
    },

    "service_6_2": {
        "uz": (
            "🔥 <b>Ortiqcha energiya sarfini aniqlash</b>\n\n"
            "Keraksiz energiya sarfi — befoyda xarajat.\n"
            "<b>Haqiqiy misol:</b> eskirgan uskuna 50% ko'proq energiya yutadi\n\n"
            "Biz (7 kundan):\n"
            "• samarasiz uskunalarni aniqlaymiz (thermal imaging)\n"
            "• yo'qotish nuqtalarini ko'rsatamiz (50+ nuqta tekshiramiz)\n"
            "• texnik xatolarni ochib beramiz (detailed report)\n\n"
            "✅ <b>Natija:</b> <b>50% ortiqcha sarf aniqlandi</b>, tejamkorlik imkoniyati 20-30%."
        ),
        "ru": (
            "🔥 <b>Выявление избыточного энергопотребления</b>\n\n"
            "Лишнее потребление энергии — это лишние расходы.\n"
            "<b>Реальный пример:</b> старое оборудование потребляет на 50% больше\n\n"
            "Мы (от 7 дней):\n"
            "• выявляем неэффективное оборудование (тепловизор)\n"
            "• показываем точки потерь (50+ проверок)\n"
            "• обнаруживаем ошибки (подробный отчет)\n\n"
            "✅ <b>Результат:</b> выявлено <b>50% лишних затрат</b>, возможность экономии 20-30%."
        ),
    },

    "service_6_3": {
        "uz": (
            "💡 <b>Tejamkorlik bo'yicha tavsiyalar</b>\n\n"
            "Kam sarflab, ko'proq natija olish mumkin.\n"
            "<b>Haqiqiy misol:</b> tavsiyalar siz 25-30% energiya tejaydi\n\n"
            "Biz (7-10 kundan):\n"
            "• energiya tejamkor yechimlar taklif qilamiz (15+ variant)\n"
            "• real sharoitga mos tavsiyalar beramiz (ROI hisoblash)\n"
            "• kam xarajatli yoki sarmoyasiz usullarni ko'rsatamiz (0 to 500 mln som)\n\n"
            "✅ <b>Natija:</b> <b>25-30% tejamkorlik</b>, kam xarajat va yuqori samaradorlik."
        ),
        "ru": (
            "💡 <b>Рекомендации по энергосбережению</b>\n\n"
            "Можно тратить меньше и получать больше.\n"
            "<b>Реальный пример:</b> рекомендации дают 25-30% экономии\n\n"
            "Мы (от 7-10 дней):\n"
            "• предлагаем энергоэффективные решения (15+ вариантов)\n"
            "• даем рекомендации под условия (ROI расчет)\n"
            "• показываем малозатратные способы (0-500 млн сум)\n\n"
            "✅ <b>Результат:</b> <b>экономия 25-30%</b>, низкие затраты и высокая эффективность."
        ),
    },

    "service_6_4": {
        "uz": (
            "🏭 <b>Ishlab chiqarish uskunalarini tekshirish</b>\n\n"
            "Eskirgan yoki noto'g'ri sozlangan uskuna ko'p energiya yutadi.\n"
            "<b>Haqiqiy misol:</b> texnik tekshirish orqali 40% tejamkorlik aniqlash mumkin\n\n"
            "Biz (10-14 kundan):\n"
            "• uskunalarni texnik tekshiramiz (thermal + vibration analysis)\n"
            "• samaradorlik darajasini baholaymiz (detailed assessment)\n"
            "• modernizatsiya bo'yicha tavsiyalar beramiz (20+ optsiya)\n\n"
            "✅ <b>Natija:</b> <b>40% tejamkorlik</b>, xavfsiz va samarali uskunalar."
        ),
        "ru": (
            "🏭 <b>Проверка производственного оборудования</b>\n\n"
            "Изношенное оборудование потребляет на 40% больше.\n"
            "<b>Реальный пример:</b> техническая проверка выявляет 40% возможной экономии\n\n"
            "Мы (от 10-14 дней):\n"
            "• проводим техническую проверку (тепловизор + вибро)\n"
            "• оцениваем эффективность (детальная оценка)\n"
            "• даем рекомендации по модернизации (20+ вариантов)\n\n"
            "✅ <b>Результат:</b> <b>экономия 40%</b>, безопасное и эффективное оборудование."
        ),
    },

    "service_6_5": {
        "uz": (
            "🚀 <b>Energiya samaradorligini oshirish loyihalari</b>\n\n"
            "Energiya tejamkorlik — uzoq muddatli foyda.\n"
            "<b>Haqiqiy misol:</b> loyihalar siz 35-50% energiya tejaydi va 18-24 oyda to'lanadi\n\n"
            "Biz (14-21 kundan):\n"
            "• maxsus loyihalar ishlab chiqamiz (proven technologies)\n"
            "• energiya sarfini kamaytirish strategiyasini tuzamiz (5-10 yillik plan)\n"
            "• iqtisodiy samarani hisoblab beramiz (ROI va payback)\n\n"
            "✅ <b>Natija:</b> <b>35-50% tejamkorlik</b>, 18-24 oyda to'lanadi, uzoq muddatli foyda."
        ),
        "ru": (
            "🚀 <b>Проекты по повышению энергоэффективности</b>\n\n"
            "Энергоэффективность — это долгосрочная выгода.\n"
            "<b>Реальный пример:</b> проекты дают 35-50% экономии и окупаются за 18-24 месяца\n\n"
            "Мы (от 14-21 дней):\n"
            "• разрабатываем специальные проекты (проверенные технологии)\n"
            "• формируем стратегию на 5-10 лет (снижение потребления)\n"
            "• рассчитываем экономический эффект (ROI и окупаемость)\n\n"
            "✅ <b>Результат:</b> <b>экономия 35-50%</b>, окупаемость 18-24 месяца, долгосрочная выгода."
        ),
    },

    "service_6_6": {
        "uz": (
            "📄 <b>Hisobot va texnik xulosa tayyorlash</b>\n\n"
            "Rasmiy hujjat — qaror qabul qilish asosi.\n"
            "<b>Haqiqiy misol:</b> to'liq hisobotlar 95% bank qarz qabul bo'ladi\n\n"
            "Biz (7-10 kundan):\n"
            "• to'liq energiya audit hisobotini tayyorlaymiz (100+ sahifali)\n"
            "• texnik xulosalar beramiz (certified specialists)\n"
            "• rahbar va tekshiruvlar uchun tayyorlaymiz (100% komptent)\n\n"
            "✅ <b>Natija:</b> rasmiy hujjat, <b>95% bank qarz qabuli</b>, 7-10 kundan tayyar."
        ),
        "ru": (
            "📄 <b>Подготовка отчёта и технического заключения</b>\n\n"
            "Официальный отчет — основа для получения финансирования.\n"
            "<b>Реальный пример:</b> полный отчет дает 95% одобрение банковского кредита\n\n"
            "Мы (от 7-10 дней):\n"
            "• готовим полный отчет по энергоаудиту (100+ страниц)\n"
            "• даем техническое заключение (сертифицированные специалисты)\n"
            "• подготавливаем для банков (100% компетентные)\n\n"
            "✅ <b>Результат:</b> официальный отчет, <b>95% одобрение кредита</b>, готово за 7-10 дней."
        ),
    },

    "service_6_7": {
        "uz": (
            "🧠 <b>Energiya audit bo'yicha konsultatsiya</b>\n\n"
            "Qaysi yechim foydaliroq ekanini bilmoqchimisiz?\n"
            "<b>Haqiqiy misol:</b> konsultatsiya siz 25-35% energiya tejaydi va 50% xarajat tejaydi\n\n"
            "Biz (5-7 kundan):\n"
            "• holatingizni tahlil qilamiz (detailed analysis)\n"
            "• individual maslahat beramiz (3-5 variantni)\n"
            "• eng samarali yo'lni ko'rsatamiz (proven methods)\n\n"
            "✅ <b>Natija:</b> <b>25-35% energiya tejamkorlik</b>, <b>50% xarajat tejamkorlik</b>, ongli qaror."
        ),
        "ru": (
            "🧠 <b>Консультации по энергетическому аудиту</b>\n\n"
            "Хотите выбрать наиболее выгодное решение?\n"
            "<b>Реальный пример:</b> консультация дает 25-35% экономии энергии и 50% экономии затрат\n\n"
            "Мы (от 5-7 дней):\n"
            "• анализируем ситуацию (детальный анализ)\n"
            "• даем рекомендации (3-5 вариантов)\n"
            "• предлагаем эффективный путь (проверенные методы)\n\n"
            "✅ <b>Результат:</b> <b>экономия 25-35% энергии</b>, <b>50% меньше затрат</b>, обоснованное решение."
        ),
    },
}
SERVICE_7_TEXTS = {
    "service_7_1": {
        "uz": (
            "📊 <b>Sotuv jarayonlarini tahlil qilish</b>\n\n"
            "Reklama bor, mijozlar bor, lekin sotuv pastmi?\n"
            "<b>Haqiqiy misol:</b> tahlil orqali 40% yo'qolgan mijozlar aniqlash mumkin\n\n"
            "Biz (7 kundan):\n"
            "• sotuv jarayonini bosqichma-bosqich tahlil qilamiz (5+ bosqich)\n"
            "• qayerda 40% mijoz yo'qolayotganini aniqlaymiz (exact point)\n"
            "• zaif nuqtalarni aniq ko'rsatamiz (detailed report)\n\n"
            "✅ <b>Natija:</b> sotuvni to'xtatayotgan sabablar aniq bo'ladi, <b>40% yo'qolgan mijozni qaytarish</b> mumkin."
        ),
        "ru": (
            "📊 <b>Анализ процессов продаж</b>\n\n"
            "Реклама есть, клиенты есть, но продаж мало?\n"
            "<b>Реальный пример:</b> анализ выявляет, что теряется 40% потенциальных клиентов\n\n"
            "Мы (от 7 дней):\n"
            "• анализируем процесс по этапам (5+ этапов)\n"
            "• выявляем, где теряется 40% клиентов (точный момент)\n"
            "• показываем слабые точки (детальный отчет)\n\n"
            "✅ <b>Результат:</b> понятны причины, <b>вернуть можно 40% клиентов</b>, увеличить продажи."
        ),
    },

    "service_7_2": {
        "uz": (
            "🧭 <b>Marketing strategiya ishlab chiqish</b>\n\n"
            "Tasodifiy reklama — tasodifiy natija.\n"
            "<b>Haqiqiy misol:</b> to'g'ri strategiya sotuv 60% oshiradi\n\n"
            "Biz (10-14 kundan):\n"
            "• biznes va bozorni tahlil qilamiz (market research)\n"
            "• maqsadli auditoriyani aniqlaymiz (customer profiling)\n"
            "• ishlaydigan marketing strategiya tuzamiz (proven approach)\n\n"
            "✅ <b>Natija:</b> reja asosida ishlaydigan marketing, <b>sotuv 60% oshadi</b>."
        ),
        "ru": (
            "🧭 <b>Разработка маркетинговой стратегии</b>\n\n"
            "Случайная реклама — случайный результат.\n"
            "<b>Реальный пример:</b> правильная стратегия увеличивает продажи на 60%\n\n"
            "Мы (от 10-14 дней):\n"
            "• анализируем бизнес и рынок (исследование рынка)\n"
            "• определяем целевую аудиторию (профилирование)\n"
            "• создаем стратегию (проверенный подход)\n\n"
            "✅ <b>Результат:</b> системный маркетинг, <b>продажи +60%</b>, рост бизнеса."
        ),
    },

    "service_7_3": {
        "uz": (
            "🎯 <b>Target va reklama kampaniyalari</b>\n\n"
            "Reklamaga pul ketmoqda, lekin natija yo'qmi?\n"
            "<b>Haqiqiy misol:</b> to'g'ri target orqali 3-5 baravar ko'proq ROI\n\n"
            "Biz (5-7 kundan):\n"
            "• to'g'ri auditoriyani aniqlaymiz (detailed segmentation)\n"
            "• samarali reklama kampaniyalarini sozlaymiz (A/B testing)\n"
            "• doimiy optimallashtiramiz (weekly optimization)\n\n"
            "✅ <b>Natija:</b> <b>ROI 3-5 baravar oshadi</b>, reklama orqali real mijozlar oqimi."
        ),
        "ru": (
            "🎯 <b>Таргетированная реклама и кампании</b>\n\n"
            "Деньги тратятся, а результата нет?\n"
            "<b>Реальный пример:</b> правильный таргет дает в 3-5 раз больше ROI\n\n"
            "Мы (от 5-7 дней):\n"
            "• определяем нужную аудиторию (детальная сегментация)\n"
            "• настраиваем эффективные кампании (A/B тестирование)\n"
            "• постоянно оптимизируем (еженедельная оптимизация)\n\n"
            "✅ <b>Результат:</b> <b>ROI в 3-5 раз выше</b>, стабильный поток клиентов."
        ),
    },

    "service_7_4": {
        "uz": (
            "📱 <b>SMM — ijtimoiy tarmoqlar</b>\n\n"
            "Ijtimoiy tarmoqlarda bor bo'lish yetarli emas — faol bo'lish kerak.\n"
            "<b>Haqiqiy misol:</b> to'g'ri SMM orqali subscriber 5 baravar oshadi\n\n"
            "Biz (7-14 kundan):\n"
            "• kontent reja tuzamiz (monthly calendar)\n"
            "• sahifalarni professional yuritamiz (daily posts)\n"
            "• auditoriya bilan ishlaymiz (community management)\n\n"
            "✅ <b>Natija:</b> <b>subscriber 5 baravar oshadi</b>, faol auditoriya va kuchli imij."
        ),
        "ru": (
            "📱 <b>SMM — социальные сети</b>\n\n"
            "Просто присутствовать недостаточно — нужно быть активными.\n"
            "<b>Реальный пример:</b> правильный SMM увеличивает подписчиков в 5 раз\n\n"
            "Мы (от 7-14 дней):\n"
            "• создаем контент-план (ежемесячный календарь)\n"
            "• профессионально ведем страницы (ежедневные посты)\n"
            "• работаем с аудиторией (управление сообществом)\n\n"
            "✅ <b>Результат:</b> <b>подписчики +500%</b>, активная аудитория и сильный бренд."
        ),
    },

    "service_7_5": {
        "uz": (
            "🏷 <b>Brendni rivojlantirish</b>\n\n"
            "Brend — bu faqat logo emas, bu ishonch.\n"
            "<b>Haqiqiy misol:</b> to'g'ri brending siz bozorda 80% tanilishi oshadi\n\n"
            "Biz (14-21 kundan):\n"
            "• brendingizni tahlil qilamiz (brand audit)\n"
            "• yagona vizual va kommunikatsiya uslubini yaratamiz (brand guidelines)\n"
            "• bozorda ajralib turishingizga yordam beramiz (positioning)\n\n"
            "✅ <b>Natija:</b> <b>80% tanilishi oshadi</b>, ishonchli va esda qoladigan brend."
        ),
        "ru": (
            "🏷 <b>Развитие бренда</b>\n\n"
            "Бренд — это не только логотип, это доверие.\n"
            "<b>Реальный пример:</b> правильный брендинг повышает узнаваемость на 80%\n\n"
            "Мы (от 14-21 дней):\n"
            "• анализируем бренд (аудит бренда)\n"
            "• создаем единый стиль (brand guidelines)\n"
            "• помогаем выделиться (позиционирование)\n\n"
            "✅ <b>Результат:</b> <b>узнаваемость +80%</b>, узнаваемый и сильный бренд."
        ),
    },

    "service_7_6": {
        "uz": (
            "🔄 <b>Savdo voronkasi (Sales Funnel)</b>\n\n"
            "Mijoz keladi, lekin sotib olmay ketayaptimi?\n"
            "<b>Haqiqiy misol:</b> to'g'ri voronka siz conversion 4-5 baravar oshiradi\n\n"
            "Biz (10-14 kundan):\n"
            "• mijoz yo'lini to'liq loyihalaymiz (customer journey)\n"
            "• har bosqichni optimallashtiramiz (conversion optimization)\n"
            "• avtomatlashtirilgan voronka quramiz (automation)\n\n"
            "✅ <b>Natija:</b> <b>conversion 4-5 baravar oshadi</b>, tizimli va barqaror sotuv."
        ),
        "ru": (
            "🔄 <b>Воронка продаж (Sales Funnel)</b>\n\n"
            "Клиенты приходят, но не покупают?\n"
            "<b>Реальный пример:</b> правильная воронка увеличивает конверсию в 4-5 раз\n\n"
            "Мы (от 10-14 дней):\n"
            "• проектируем путь клиента (customer journey)\n"
            "• оптимизируем каждый этап (оптимизация конверсии)\n"
            "• автоматизируем воронку (автоматизация)\n\n"
            "✅ <b>Результат:</b> <b>конверсия +400-500%</b>, стабильные прогнозируемые продажи."
        ),
    },

    "service_7_7": {
        "uz": (
            "🧠 <b>CRM orqali sotuvni oshirish</b>\n\n"
            "Mijozlar bazasi bor, lekin ishlamayaptimi?\n"
            "<b>Haqiqiy misol:</b> CRM orqali qayta sotuv 50% oshadi\n\n"
            "Biz (7-10 kundan):\n"
            "• CRM orqali mijozlar bilan ishlashni yo'lga qo'yamiz (setup)\n"
            "• qayta sotuv mexanizmlarini sozlaymiz (repeat sales)\n"
            "• menejerlar faoliyatini nazorat qilamiz (daily reporting)\n\n"
            "✅ <b>Natija:</b> <b>qayta sotuv 50% oshadi</b>, har bir mijozdan maksimal foyda."
        ),
        "ru": (
            "🧠 <b>Увеличение продаж через CRM</b>\n\n"
            "Есть база клиентов, но она не работает?\n"
            "<b>Реальный пример:</b> правильная CRM увеличивает повторные продажи на 50%\n\n"
            "Мы (от 7-10 дней):\n"
            "• настраиваем работу с клиентами (установка CRM)\n"
            "• внедряем повторные продажи (repeat sales)\n"
            "• контролируем менеджеров (ежедневные отчеты)\n\n"
            "✅ <b>Результат:</b> <b>повторные продажи +50%</b>, максимум прибыли с каждого клиента."
        ),
    },

    "service_7_8": {
        "uz": (
            "🧪 <b>Konsultatsiya va marketing audit</b>\n\n"
            "Qayerdan boshlashni bilmayapsizmi?\n"
            "<b>Haqiqiy misol:</b> audit orqali 50+ marketing xatolar aniqlash mumkin\n\n"
            "Biz (5-7 kundan):\n"
            "• marketing holatingizni tahlil qilamiz (detailed audit)\n"
            "• xatolar va imkoniyatlarni ko'rsatamiz (50+ findings)\n"
            "• aniq tavsiyalar beramiz (action plan)\n\n"
            "✅ <b>Natija:</b> ongli strategiya va aniq reja, <b>50+ improvement points</b> aniqlandi."
        ),
        "ru": (
            "🧪 <b>Консультации и маркетинговый аудит</b>\n\n"
            "Не знаете, с чего начать?\n"
            "<b>Реальный пример:</b> аудит выявляет 50+ ошибок и возможностей\n\n"
            "Мы (от 5-7 дней):\n"
            "• анализируем маркетинг (детальный аудит)\n"
            "• выявляем ошибки и возможности (50+ находок)\n"
            "• даем четкие рекомендации (план действий)\n\n"
            "✅ <b>Результат:</b> понятная стратегия, четкий план, <b>50+ точек улучшения</b> определены."
        ),
    },
}
