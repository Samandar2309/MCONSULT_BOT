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
        "Biz quyidagi yo‘nalishlarda faoliyat yuritamiz:\n"
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
# 📋 XIZMATLAR — UMUMIY TA’RIFLAR
# (asosan fallback yoki qisqa ko‘rsatish uchun)
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
            "bilan ishlash bo‘yicha xizmatlar."
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
            "Kadrlar uchun o‘quv kurslari, treninglar "
            "va amaliy mashg‘ulotlar."
        ),
        "5": (
            "📜 Litsenziya olishga yordam\n\n"
            "Faoliyatni qonuniy yo‘lga qo‘yish uchun "
            "to‘liq hujjatlashtirish va amaliy ko‘mak."
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
            "Biznesda pul bor, lekin qayerga ketayotganini aniq bilmaysizmi?\n\n"
            "Ushbu xizmat orqali:\n"
            "• barcha tushum va xarajatlar tartib bilan hisobga olinadi\n"
            "• keraksiz va yashirin xarajatlar aniqlanadi\n"
            "• pul oqimi doimiy nazorat ostida bo‘ladi\n\n"
            "Biz sizga:\n"
            "✔️ kunlik, oylik va umumiy hisobni yuritamiz\n"
            "✔️ aniq raqamlar asosida tahlil beramiz\n"
            "✔️ moliyaviy chalkashliklarni yo‘q qilamiz\n\n"
            "✅ <b>Natija:</b> pulingiz qayerga ketayotganini bilasiz va foydani ongli boshqarasiz."
        ),
        "ru": (
            "💰 <b>Учет доходов и расходов</b>\n\n"
            "В бизнесе есть деньги, но вы не понимаете, куда они уходят?\n\n"
            "Данная услуга позволяет:\n"
            "• вести точный учет всех доходов и расходов\n"
            "• выявлять лишние и скрытые затраты\n"
            "• держать денежный поток под постоянным контролем\n\n"
            "Мы для вас:\n"
            "✔️ ведем ежедневный, месячный и общий учет\n"
            "✔️ предоставляем анализ на основе точных данных\n"
            "✔️ устраняем финансовый хаос\n\n"
            "✅ <b>Результат:</b> вы точно знаете, куда уходят деньги, и осознанно управляете прибылью."
        ),
    },

    "acc_profit": {
        "uz": (
            "📊 <b>Daromad va xarajatlar tahlili</b>\n\n"
            "Biznesingiz haqiqatan foyda keltiryaptimi yoki faqat aylanma bormi?\n\n"
            "Biz:\n"
            "• daromad va xarajatlarni chuqur tahlil qilamiz\n"
            "• qaysi yo‘nalish foydali, qaysisi zararli ekanini ko‘rsatamiz\n"
            "• foydani oshirish uchun aniq tavsiyalar beramiz\n\n"
            "Bu xizmat:\n"
            "✔️ noto‘g‘ri qarorlarning oldini oladi\n"
            "✔️ biznesni raqamlar asosida boshqarishga o‘rgatadi\n\n"
            "✅ <b>Natija:</b> tasodifiy emas, aniq hisob-kitob asosidagi rivojlanish."
        ),
        "ru": (
            "📊 <b>Анализ доходов и расходов</b>\n\n"
            "Ваш бизнес действительно приносит прибыль или только оборот?\n\n"
            "Мы:\n"
            "• проводим глубокий анализ доходов и расходов\n"
            "• показываем прибыльные и убыточные направления\n"
            "• даем конкретные рекомендации по увеличению прибыли\n\n"
            "Эта услуга:\n"
            "✔️ предотвращает ошибочные решения\n"
            "✔️ помогает управлять бизнесом на основе цифр\n\n"
            "✅ <b>Результат:</b> развитие на основе точных расчетов, а не случайности."
        ),
    },

    "acc_salary": {
        "uz": (
            "👨‍💼 <b>Xodimlar oyligi va ish haqi hisobi</b>\n\n"
            "Oylikdagi xato — xodim noroziligi va ishonchsizlik demakdir.\n\n"
            "Biz:\n"
            "• oylik, bonus va ushlab qolishlarni aniq hisoblaymiz\n"
            "• kechikish va kelishmovchiliklarni yo‘q qilamiz\n"
            "• rahbar uchun qulay nazorat tizimini yaratamiz\n\n"
            "Bu xizmat orqali:\n"
            "✔️ xodimlar bilan munosabat mustahkamlanadi\n"
            "✔️ ichki tartib va intizom yaxshilanadi\n\n"
            "✅ <b>Natija:</b> xodimlar ishonchi va barqaror jamoa."
        ),
        "ru": (
            "👨‍💼 <b>Расчет заработной платы сотрудников</b>\n\n"
            "Ошибка в зарплате — это недовольство и потеря доверия.\n\n"
            "Мы:\n"
            "• точно рассчитываем зарплаты, бонусы и удержания\n"
            "• устраняем задержки и разногласия\n"
            "• создаем удобную систему контроля для руководства\n\n"
            "Эта услуга:\n"
            "✔️ укрепляет отношения с сотрудниками\n"
            "✔️ улучшает дисциплину и порядок\n\n"
            "✅ <b>Результат:</b> доверие сотрудников и стабильная команда."
        ),
    },

    "acc_tax": {
        "uz": (
            "🧾 <b>Soliq hisobotlari</b>\n\n"
            "Soliq xatolari — jarima, tekshiruv va stress.\n\n"
            "Biz:\n"
            "• soliq hisobotlarini o‘z vaqtida tayyorlaymiz\n"
            "• qonunchilikka to‘liq mos topshiramiz\n"
            "• jarima va muammolarning oldini olamiz\n\n"
            "Siz:\n"
            "✔️ soliq haqida bosh qotirmaysiz\n"
            "✔️ tekshiruvlardan xotirjam o‘tasiz\n\n"
            "✅ <b>Natija:</b> xavfsiz va qonuniy yuritiladigan biznes."
        ),
        "ru": (
            "🧾 <b>Налоговая отчетность</b>\n\n"
            "Ошибки в налогах — это штрафы, проверки и стресс.\n\n"
            "Мы:\n"
            "• готовим отчетность в установленные сроки\n"
            "• сдаем ее в полном соответствии с законом\n"
            "• предотвращаем штрафы и проблемы\n\n"
            "Вы:\n"
            "✔️ не переживаете из-за налогов\n"
            "✔️ спокойно проходите проверки\n\n"
            "✅ <b>Результат:</b> безопасный и законный бизнес."
        ),
    },

    "acc_reports": {
        "uz": (
            "📑 <b>Moliyaviy hisobotlar</b>\n\n"
            "Biznes holatini aniq ko‘rish uchun hisobotlar muhim.\n\n"
            "Biz:\n"
            "• oylik, choraklik va yillik hisobotlar tayyorlaymiz\n"
            "• biznesning real holatini ko‘rsatamiz\n"
            "• rivojlanish va muammo nuqtalarini aniqlaymiz\n\n"
            "Bu hisobotlar:\n"
            "✔️ rahbar uchun aniq qarorlar qabul qilishga yordam beradi\n"
            "✔️ investor va banklar uchun ishonch yaratadi\n\n"
            "✅ <b>Natija:</b> biznesingiz raqamlar orqali boshqariladi."
        ),
        "ru": (
            "📑 <b>Финансовые отчеты</b>\n\n"
            "Чтобы видеть реальное состояние бизнеса, нужны отчеты.\n\n"
            "Мы:\n"
            "• готовим месячные, квартальные и годовые отчеты\n"
            "• показываем реальную картину бизнеса\n"
            "• выявляем точки роста и проблемы\n\n"
            "Эти отчеты:\n"
            "✔️ помогают руководителю принимать точные решения\n"
            "✔️ повышают доверие инвесторов и банков\n\n"
            "✅ <b>Результат:</b> управление бизнесом на основе цифр."
        ),
    },

    "acc_consult": {
        "uz": (
            "🧠 <b>Buxgalteriya konsultatsiyasi</b>\n\n"
            "Qanday tizim foydaliroq? Qanday ishlash xavfsiz?\n\n"
            "Biz:\n"
            "• biznesingizni chuqur tahlil qilamiz\n"
            "• individual maslahat beramiz\n"
            "• eng to‘g‘ri buxgalteriya yechimini taklif qilamiz\n\n"
            "Bu xizmat:\n"
            "✔️ xatolarni oldindan ko‘rishga yordam beradi\n"
            "✔️ noto‘g‘ri qarorlardan saqlaydi\n\n"
            "✅ <b>Natija:</b> ishonchli va xotirjam rivojlanish."
        ),
        "ru": (
            "🧠 <b>Бухгалтерская консультация</b>\n\n"
            "Какая система выгоднее? Как работать безопасно?\n\n"
            "Мы:\n"
            "• анализируем ваш бизнес\n"
            "• даем индивидуальные консультации\n"
            "• предлагаем оптимальное бухгалтерское решение\n\n"
            "Эта услуга:\n"
            "✔️ помогает заранее увидеть ошибки\n"
            "✔️ защищает от неверных решений\n\n"
            "✅ <b>Результат:</b> уверенное и спокойное развитие."
        ),
    },
}
BROKER_TEXTS = {
    "broker_docs": {
        "uz": (
            "📦 <b>Import hujjatlarini rasmiylashtirish</b>\n\n"
            "Tovar olib kirishda bitta noto‘g‘ri hujjat — kechikish va jarima degani.\n\n"
            "Biz:\n"
            "• import uchun zarur barcha hujjatlarni aniqlaymiz\n"
            "• hujjatlarni qonunchilikka mos rasmiylashtiramiz\n"
            "• bojxona talablariga to‘liq moslab topshiramiz\n\n"
            "Bu xizmat:\n"
            "✔️ tovarlaringiz ushlanib qolmasligini ta’minlaydi\n"
            "✔️ vaqt va ortiqcha xarajatlarni tejaydi\n\n"
            "✅ <b>Natija:</b> import jarayoni tez, xavfsiz va muammosiz."
        ),
        "ru": (
            "📦 <b>Оформление импортных документов</b>\n\n"
            "Одна ошибка в документах — задержка и штраф.\n\n"
            "Мы:\n"
            "• определяем полный перечень необходимых документов\n"
            "• оформляем их в соответствии с законодательством\n"
            "• подаем документы с учетом всех требований таможни\n\n"
            "Эта услуга:\n"
            "✔️ предотвращает задержку товара\n"
            "✔️ экономит время и лишние расходы\n\n"
            "✅ <b>Результат:</b> быстрый и безопасный импорт."
        ),
    },

    "broker_customs": {
        "uz": (
            "🛃 <b>Bojxona deklaratsiyasi</b>\n\n"
            "Bojxona deklaratsiyasidagi xato — tovarning ushlanishi yoki jarima.\n\n"
            "Biz:\n"
            "• deklaratsiyani to‘g‘ri va aniq rasmiylashtiramiz\n"
            "• kodlar va toifalarni to‘g‘ri tanlaymiz\n"
            "• bojxona jarayonini tezlashtiramiz\n\n"
            "Bu xizmat:\n"
            "✔️ bojxona nazoratidan muammosiz o‘tishga yordam beradi\n"
            "✔️ ortiqcha to‘lovlarni kamaytiradi\n\n"
            "✅ <b>Natija:</b> tezkor va qonuniy bojxona rasmiylashtiruvi."
        ),
        "ru": (
            "🛃 <b>Таможенная декларация</b>\n\n"
            "Ошибка в декларации — задержка товара или штраф.\n\n"
            "Мы:\n"
            "• оформляем декларацию точно и корректно\n"
            "• правильно подбираем коды и категории\n"
            "• ускоряем прохождение таможни\n\n"
            "Эта услуга:\n"
            "✔️ обеспечивает беспрепятственное прохождение контроля\n"
            "✔️ снижает лишние платежи\n\n"
            "✅ <b>Результат:</b> законное и быстрое таможенное оформление."
        ),
    },

    "broker_cert": {
        "uz": (
            "📜 <b>Sertifikat va ruxsatnomalarni olish</b>\n\n"
            "Ruxsatnomasiz tovar — katta huquqiy muammo.\n\n"
            "Biz:\n"
            "• qaysi sertifikat va ruxsatnoma kerakligini aniqlaymiz\n"
            "• ularni olish jarayonini tezlashtiramiz\n"
            "• hujjatlarni to‘liq tayyorlab beramiz\n\n"
            "Bu xizmat:\n"
            "✔️ tekshiruvlarda muammosiz o‘tishni ta’minlaydi\n"
            "✔️ savdoni qonuniy qiladi\n\n"
            "✅ <b>Natija:</b> xotirjam va qonuniy savdo faoliyati."
        ),
        "ru": (
            "📜 <b>Получение сертификатов и разрешений</b>\n\n"
            "Товар без разрешений — серьезный юридический риск.\n\n"
            "Мы:\n"
            "• определяем необходимые сертификаты и разрешения\n"
            "• ускоряем процесс их получения\n"
            "• полностью подготавливаем документы\n\n"
            "Эта услуга:\n"
            "✔️ гарантирует успешное прохождение проверок\n"
            "✔️ делает торговлю законной\n\n"
            "✅ <b>Результат:</b> спокойная и легальная торговая деятельность."
        ),
    },

    "broker_contract": {
        "uz": (
            "📝 <b>Shartnomalarni tekshirish va tayyorlash</b>\n\n"
            "Noto‘g‘ri shartnoma — katta moliyaviy xavf.\n\n"
            "Biz:\n"
            "• shartnomalarni professional tahlil qilamiz\n"
            "• xavfli bandlarni aniqlaymiz\n"
            "• manfaatlaringizni himoya qiladigan shartnoma tayyorlaymiz\n\n"
            "Bu xizmat:\n"
            "✔️ kelishmovchiliklarning oldini oladi\n"
            "✔️ huquqiy xavfsizlikni ta’minlaydi\n\n"
            "✅ <b>Natija:</b> ishonchli va himoyalangan bitimlar."
        ),
        "ru": (
            "📝 <b>Проверка и подготовка договоров</b>\n\n"
            "Неправильный договор — серьезный финансовый риск.\n\n"
            "Мы:\n"
            "• профессионально анализируем договоры\n"
            "• выявляем рисковые пункты\n"
            "• готовим договор с защитой ваших интересов\n\n"
            "Эта услуга:\n"
            "✔️ предотвращает споры\n"
            "✔️ обеспечивает юридическую безопасность\n\n"
            "✅ <b>Результат:</b> надежные и защищенные сделки."
        ),
    },

    "broker_logistics": {
        "uz": (
            "🚚 <b>Tovarni rasmiy olib kirish / chiqarish</b>\n\n"
            "Noto‘g‘ri rasmiylashtirish — tovar yo‘qotilishi yoki jarima.\n\n"
            "Biz:\n"
            "• tovarni qonuniy va rasmiy yo‘l bilan olib kiramiz yoki chiqaramiz\n"
            "• barcha hujjatlarni to‘g‘ri yuritamiz\n"
            "• jarayonni to‘liq nazorat qilamiz\n\n"
            "Bu xizmat:\n"
            "✔️ xavfsiz va tezkor logistika yaratadi\n"
            "✔️ muammosiz savdoni ta’minlaydi\n\n"
            "✅ <b>Natija:</b> tovaringiz xavfsiz va qonuniy harakatlanadi."
        ),
        "ru": (
            "🚚 <b>Официальный ввоз / вывоз товара</b>\n\n"
            "Неправильное оформление — риск потери товара или штрафа.\n\n"
            "Мы:\n"
            "• организуем официальный и законный ввоз или вывоз\n"
            "• ведем всю документацию корректно\n"
            "• полностью контролируем процесс\n\n"
            "Эта услуга:\n"
            "✔️ обеспечивает безопасную и быструю логистику\n"
            "✔️ гарантирует бесперебойную торговлю\n\n"
            "✅ <b>Результат:</b> товар движется законно и безопасно."
        ),
    },

    "broker_consult": {
        "uz": (
            "🧠 <b>Brokerlik konsultatsiyasi</b>\n\n"
            "Qaysi yo‘l xavfsizroq? Qanday rasmiylashtirish foydaliroq?\n\n"
            "Biz:\n"
            "• holatingizni chuqur tahlil qilamiz\n"
            "• individual maslahat beramiz\n"
            "• eng xavfsiz va tejamkor yechimni taklif qilamiz\n\n"
            "Bu xizmat:\n"
            "✔️ xatolarni oldindan ko‘rishga yordam beradi\n"
            "✔️ risklarni kamaytiradi\n\n"
            "✅ <b>Natija:</b> ishonchli va barqaror tashqi savdo faoliyati."
        ),
        "ru": (
            "🧠 <b>Брокерская консультация</b>\n\n"
            "Какой путь безопаснее? Как оформить выгоднее?\n\n"
            "Мы:\n"
            "• глубоко анализируем вашу ситуацию\n"
            "• предоставляем индивидуальные консультации\n"
            "• предлагаем безопасные и экономичные решения\n\n"
            "Эта услуга:\n"
            "✔️ помогает заранее избежать ошибок\n"
            "✔️ снижает риски\n\n"
            "✅ <b>Результат:</b> надежная и стабильная внешнеторговая деятельность."
        ),
    },
}
IT_TEXTS = {
    "it_crm": {
        "uz": (
            "🧠 <b>CRM tizimlari</b>\n\n"
            "Mijozlar ko‘p, lekin nazorat yo‘qmi? Savdo jarayoni tartibsizmi?\n\n"
            "CRM tizimi orqali:\n"
            "• barcha mijozlar yagona bazada saqlanadi\n"
            "• savdo jarayonlari avtomatlashtiriladi\n"
            "• menejerlar faoliyati nazorat qilinadi\n\n"
            "Biz:\n"
            "✔️ biznesingizga mos CRM yaratamiz\n"
            "✔️ hisobot va tahlillarni avtomatlashtiramiz\n"
            "✔️ Telegram bot va to‘lov tizimlari bilan integratsiya qilamiz\n\n"
            "✅ <b>Natija:</b> tartibli savdo, ko‘proq mijoz va o‘sishga tayyor biznes."
        ),
        "ru": (
            "🧠 <b>CRM-системы</b>\n\n"
            "Много клиентов, но нет контроля? Продажи хаотичны?\n\n"
            "CRM позволяет:\n"
            "• хранить всех клиентов в единой базе\n"
            "• автоматизировать продажи\n"
            "• контролировать работу менеджеров\n\n"
            "Мы:\n"
            "✔️ разрабатываем CRM под ваш бизнес\n"
            "✔️ автоматизируем отчеты и аналитику\n"
            "✔️ интегрируем Telegram-ботов и платежные системы\n\n"
            "✅ <b>Результат:</b> упорядоченные продажи и рост бизнеса."
        ),
    },

    "it_hrm": {
        "uz": (
            "👨‍💼 <b>HRM tizimi</b>\n\n"
            "Xodimlar bilan bog‘liq muammolar ko‘p vaqt olyaptimi?\n\n"
            "HRM orqali:\n"
            "• xodimlar hisobi yuritiladi\n"
            "• ish haqi va faoliyat nazorat qilinadi\n"
            "• hujjatlar avtomatlashtiriladi\n\n"
            "Biz:\n"
            "✔️ kompaniyangizga mos HRM yaratamiz\n"
            "✔️ rahbar uchun qulay panel beramiz\n"
            "✔️ inson omili sabab xatolarni kamaytiramiz\n\n"
            "✅ <b>Natija:</b> intizomli va boshqarilishi oson jamoa."
        ),
        "ru": (
            "👨‍💼 <b>HRM-система</b>\n\n"
            "Проблемы с персоналом отнимают много времени?\n\n"
            "HRM позволяет:\n"
            "• вести учет сотрудников\n"
            "• контролировать зарплаты и эффективность\n"
            "• автоматизировать документы\n\n"
            "Мы:\n"
            "✔️ разрабатываем HRM под вашу компанию\n"
            "✔️ даем удобную панель для руководителя\n"
            "✔️ уменьшаем ошибки из-за человеческого фактора\n\n"
            "✅ <b>Результат:</b> дисциплинированная команда и простой контроль."
        ),
    },

    "it_bot": {
        "uz": (
            "🤖 <b>Telegram botlar</b>\n\n"
            "Mijozlarga doimiy javob berish qiyinmi?\n\n"
            "Telegram bot orqali:\n"
            "• murojaatlar va buyurtmalar avtomatik qabul qilinadi\n"
            "• 24/7 aloqa yo‘lga qo‘yiladi\n"
            "• operatorlar yuklamasi kamayadi\n\n"
            "Biz:\n"
            "✔️ maxsus bot ishlab chiqamiz\n"
            "✔️ CRM va to‘lov tizimlari bilan bog‘laymiz\n"
            "✔️ admin va operator paneli qo‘shamiz\n\n"
            "✅ <b>Natija:</b> tezkor aloqa va avtomatlashtirilgan savdo."
        ),
        "ru": (
            "🤖 <b>Telegram-боты</b>\n\n"
            "Сложно постоянно отвечать клиентам?\n\n"
            "Telegram-бот:\n"
            "• принимает заявки автоматически\n"
            "• работает 24/7\n"
            "• снижает нагрузку операторов\n\n"
            "Мы:\n"
            "✔️ создаем бота под ваш бизнес\n"
            "✔️ интегрируем CRM и платежи\n"
            "✔️ добавляем админ и оператор панель\n\n"
            "✅ <b>Результат:</b> быстрый сервис и автоматизация продаж."
        ),
    },

    "it_web": {
        "uz": (
            "🌐 <b>Veb-saytlar va platformalar</b>\n\n"
            "Agar saytingiz bo‘lmasa — sizni internetda topishmaydi.\n\n"
            "Biz:\n"
            "• zamonaviy dizayn yaratamiz\n"
            "• korporativ va sotuvga yo‘naltirilgan saytlar qilamiz\n"
            "• barcha qurilmalarga moslaymiz\n\n"
            "✅ <b>Natija:</b> internetda ishonchli biznes imiji."
        ),
        "ru": (
            "🌐 <b>Веб-сайты и платформы</b>\n\n"
            "Если у вас нет сайта — вас не найдут в интернете.\n\n"
            "Мы:\n"
            "• создаем современный дизайн\n"
            "• делаем корпоративные и продающие сайты\n"
            "• адаптируем под все устройства\n\n"
            "✅ <b>Результат:</b> надежный онлайн-имидж бизнеса."
        ),
    },

    "it_internet": {
        "uz": (
            "🛒 <b>Internet do‘konlar</b>\n\n"
            "Onlayn savdo qilmaslik — imkoniyatni yo‘qotish demak.\n\n"
            "Biz:\n"
            "• tez va qulay do‘kon yaratamiz\n"
            "• buyurtma va to‘lovlarni avtomatlashtiramiz\n"
            "• yetkazib berishni integratsiya qilamiz\n\n"
            "✅ <b>Natija:</b> barqaror va avtomatlashtirilgan savdo."
        ),
        "ru": (
            "🛒 <b>Интернет-магазины</b>\n\n"
            "Отказ от онлайн-продаж — потеря возможностей.\n\n"
            "Мы:\n"
            "• создаем быстрые и удобные магазины\n"
            "• автоматизируем заказы и оплаты\n"
            "• интегрируем доставку\n\n"
            "✅ <b>Результат:</b> стабильные онлайн-продажи."
        ),
    },

    "it_marketplace": {
        "uz": (
            "🏬 <b>Marketplace platformalar</b>\n\n"
            "Bir nechta sotuvchi — bitta platformada.\n\n"
            "Biz:\n"
            "• marketplace tizimlar yaratamiz\n"
            "• sotuvchi va xaridorlar uchun qulay interfeys qilamiz\n"
            "• to‘lov va buyurtmalarni avtomatlashtiramiz\n\n"
            "✅ <b>Natija:</b> kengayishga tayyor platforma."
        ),
        "ru": (
            "🏬 <b>Маркетплейс платформы</b>\n\n"
            "Несколько продавцов — одна платформа.\n\n"
            "Мы:\n"
            "• разрабатываем маркетплейсы\n"
            "• создаем удобную систему для продавцов и клиентов\n"
            "• автоматизируем заказы и оплаты\n\n"
            "✅ <b>Результат:</b> масштабируемый бизнес."
        ),
    },

    "it_mobile": {
        "uz": (
            "📱 <b>Mobil ilovalar</b>\n\n"
            "Mijozlar telefonda — biznes ham telefonda bo‘lishi kerak.\n\n"
            "Biz:\n"
            "• Android va iOS ilovalar yaratamiz\n"
            "• real vaqt monitoring va to‘lov qo‘shamiz\n\n"
            "✅ <b>Natija:</b> zamonaviy va qulay raqamli biznes."
        ),
        "ru": (
            "📱 <b>Мобильные приложения</b>\n\n"
            "Клиенты в телефоне — бизнес тоже должен быть там.\n\n"
            "Мы:\n"
            "• создаем Android и iOS приложения\n"
            "• добавляем мониторинг и оплаты\n\n"
            "✅ <b>Результат:</b> современный цифровой бизнес."
        ),
    },

    "it_automation": {
        "uz": (
            "⚙️ <b>Biznes jarayonlarni avtomatlashtirish</b>\n\n"
            "Qo‘lda ishlar ko‘p vaqt olyaptimi?\n\n"
            "Biz:\n"
            "• jarayonlarni tahlil qilamiz\n"
            "• qo‘lda ishlarni avtomatlashtiramiz\n"
            "• xatolarni kamaytiramiz\n\n"
            "✅ <b>Natija:</b> tezkor va samarali biznes."
        ),
        "ru": (
            "⚙️ <b>Автоматизация бизнес-процессов</b>\n\n"
            "Ручная работа отнимает много времени?\n\n"
            "Мы:\n"
            "• анализируем процессы\n"
            "• автоматизируем ручной труд\n"
            "• уменьшаем ошибки\n\n"
            "✅ <b>Результат:</b> эффективный и управляемый бизнес."
        ),
    },

    "it_payment": {
        "uz": (
            "💳 <b>To‘lov tizimlari integratsiyasi</b>\n\n"
            "Qulay to‘lov — ko‘proq sotuv.\n\n"
            "Biz:\n"
            "• Click, Payme, Uzum va bank to‘lovlarini ulaymiz\n"
            "• xavfsiz va tezkor tizim yaratamiz\n\n"
            "✅ <b>Natija:</b> ishonchli va tez to‘lov."
        ),
        "ru": (
            "💳 <b>Интеграция платежных систем</b>\n\n"
            "Удобная оплата — больше продаж.\n\n"
            "Мы:\n"
            "• подключаем Click, Payme, Uzum и банки\n"
            "• создаем безопасную систему\n\n"
            "✅ <b>Результат:</b> быстрые и надежные платежи."
        ),
    },

    "it_tech": {
        "uz": (
            "🔧 <b>Texnik qo‘llab-quvvatlash va IT konsultatsiya</b>\n\n"
            "Tizim ishlamasa — biznes to‘xtaydi.\n\n"
            "Biz:\n"
            "• texnik muammolarni tez hal qilamiz\n"
            "• tizimlarni nazorat qilamiz\n"
            "• rivojlanish bo‘yicha maslahat beramiz\n\n"
            "✅ <b>Natija:</b> barqaror va xavfsiz IT infratuzilma."
        ),
        "ru": (
            "🔧 <b>Техническая поддержка и IT-консультации</b>\n\n"
            "Если система не работает — бизнес останавливается.\n\n"
            "Мы:\n"
            "• быстро решаем технические проблемы\n"
            "• контролируем системы\n"
            "• консультируем по развитию\n\n"
            "✅ <b>Результат:</b> стабильная и безопасная IT-инфраструктура."
        ),
    },
}
SERVICE_4_TEXTS = {
    "service_4_1": {
        "uz": (
            "📊 <b>Buxgalteriya bo‘yicha treninglar</b>\n\n"
            "Xodimlar xatolari moliyaviy yo‘qotishlarga olib kelayaptimi?\n\n"
            "Ushbu trening orqali:\n"
            "• buxgalteriya asoslari chuqur o‘rgatiladi\n"
            "• real amaliy misollar bilan ishlanadi\n"
            "• xatolarni oldindan ko‘rish ko‘nikmasi shakllanadi\n\n"
            "Biz:\n"
            "✔️ zamonaviy qonunchilik asosida o‘qitamiz\n"
            "✔️ nazariya va amaliyotni birlashtiramiz\n\n"
            "✅ <b>Natija:</b> ishonchli va xatosiz ishlaydigan buxgalter."
        ),
        "ru": (
            "📊 <b>Тренинги по бухгалтерскому учёту</b>\n\n"
            "Ошибки сотрудников приводят к финансовым потерям?\n\n"
            "На тренинге:\n"
            "• изучаются основы бухгалтерии\n"
            "• разбираются реальные практические кейсы\n"
            "• формируется навык предотвращения ошибок\n\n"
            "Мы:\n"
            "✔️ обучаем по актуальному законодательству\n"
            "✔️ совмещаем теорию и практику\n\n"
            "✅ <b>Результат:</b> уверенный и грамотный бухгалтер."
        ),
    },

    "service_4_2": {
        "uz": (
            "📣 <b>Savdo va marketing treninglari</b>\n\n"
            "Yaxshi mahsulot bor, lekin sotuv pastmi?\n\n"
            "Biz:\n"
            "• mijoz bilan to‘g‘ri ishlashni o‘rgatamiz\n"
            "• savdo texnikalarini amalda ko‘rsatamiz\n"
            "• marketing fikrlashni shakllantiramiz\n\n"
            "Bu trening:\n"
            "✔️ sotuvchilarni kuchaytiradi\n"
            "✔️ daromadni oshiradi\n\n"
            "✅ <b>Natija:</b> faol va natija beradigan savdo jamoasi."
        ),
        "ru": (
            "📣 <b>Тренинги по продажам и маркетингу</b>\n\n"
            "Хороший продукт есть, а продажи низкие?\n\n"
            "Мы:\n"
            "• учим правильной работе с клиентами\n"
            "• показываем техники продаж на практике\n"
            "• формируем маркетинговое мышление\n\n"
            "Тренинг:\n"
            "✔️ усиливает продавцов\n"
            "✔️ увеличивает доход\n\n"
            "✅ <b>Результат:</b> эффективная команда продаж."
        ),
    },

    "service_4_3": {
        "uz": (
            "🧭 <b>Menejment va boshqaruv ko‘nikmalari</b>\n\n"
            "Rahbar bor, lekin tizim yo‘qmi?\n\n"
            "Biz:\n"
            "• to‘g‘ri rejalashtirishni o‘rgatamiz\n"
            "• jamoani boshqarish usullarini ko‘rsatamiz\n"
            "• mas’uliyat va nazoratni tizimlashtiramiz\n\n"
            "Bu trening:\n"
            "✔️ rahbarlik salohiyatini oshiradi\n"
            "✔️ ichki tartibni mustahkamlaydi\n\n"
            "✅ <b>Natija:</b> boshqariladigan va samarali jamoa."
        ),
        "ru": (
            "🧭 <b>Навыки менеджмента и управления</b>\n\n"
            "Есть руководитель, но нет системы?\n\n"
            "Мы:\n"
            "• обучаем планированию\n"
            "• показываем методы управления командой\n"
            "• систематизируем контроль и ответственность\n\n"
            "Тренинг:\n"
            "✔️ развивает управленческие навыки\n"
            "✔️ укрепляет внутренний порядок\n\n"
            "✅ <b>Результат:</b> эффективная и управляемая команда."
        ),
    },

    "service_4_4": {
        "uz": (
            "💻 <b>IT va raqamli savodxonlik treninglari</b>\n\n"
            "Xodimlar texnologiyadan to‘liq foydalana olmayaptimi?\n\n"
            "Biz:\n"
            "• kompyuter va raqamli vositalarni o‘rgatamiz\n"
            "• CRM va online tizimlar bilan ishlashni ko‘rsatamiz\n"
            "• texnologiyadan samarali foydalanishni o‘rgatamiz\n\n"
            "✅ <b>Natija:</b> zamonaviy va raqamli fikrlaydigan xodimlar."
        ),
        "ru": (
            "💻 <b>IT-тренинги и цифровая грамотность</b>\n\n"
            "Сотрудники не умеют эффективно использовать технологии?\n\n"
            "Мы:\n"
            "• обучаем работе с компьютером и цифровыми инструментами\n"
            "• показываем работу с CRM и онлайн-системами\n"
            "• повышаем цифровую эффективность\n\n"
            "✅ <b>Результат:</b> современные и цифрово грамотные сотрудники."
        ),
    },

    "service_4_5": {
        "uz": (
            "👥 <b>HR va kadrlar boshqaruvi bo‘yicha o‘qitish</b>\n\n"
            "Xodimlarni tanlash va saqlab qolish muammo bo‘lyaptimi?\n\n"
            "Biz:\n"
            "• HR tizimini o‘rgatamiz\n"
            "• baholash va motivatsiya usullarini ko‘rsatamiz\n"
            "• hujjatlar bilan ishlashni tushuntiramiz\n\n"
            "✅ <b>Natija:</b> kuchli va barqaror jamoa."
        ),
        "ru": (
            "👥 <b>Обучение HR и управлению персоналом</b>\n\n"
            "Проблемы с подбором и удержанием сотрудников?\n\n"
            "Мы:\n"
            "• обучаем HR-системам\n"
            "• показываем методы оценки и мотивации\n"
            "• объясняем кадровые процессы\n\n"
            "✅ <b>Результат:</b> сильная и стабильная команда."
        ),
    },

    "service_4_6": {
        "uz": (
            "🏢 <b>Korporativ treninglar</b>\n\n"
            "Jamoa bor, lekin hamjihatlik yo‘qmi?\n\n"
            "Biz:\n"
            "• kompaniya ehtiyojiga mos trening o‘tkazamiz\n"
            "• jamoaviy ishlashni rivojlantiramiz\n"
            "• ichki muammolarni aniqlaymiz\n\n"
            "✅ <b>Natija:</b> bir maqsad sari ishlaydigan kuchli jamoa."
        ),
        "ru": (
            "🏢 <b>Корпоративные тренинги</b>\n\n"
            "Есть команда, но нет сплоченности?\n\n"
            "Мы:\n"
            "• проводим тренинги под задачи компании\n"
            "• развиваем командную работу\n"
            "• выявляем и решаем внутренние проблемы\n\n"
            "✅ <b>Результат:</b> сильная и сплоченная команда."
        ),
    },

    "service_4_7": {
        "uz": (
            "🧠 <b>Individual konsultatsiya va coaching</b>\n\n"
            "Professional yoki rahbar sifatida o‘sishni xohlaysizmi?\n\n"
            "Biz:\n"
            "• individual tahlil qilamiz\n"
            "• shaxsiy rivojlanish rejasini tuzamiz\n"
            "• qaror qabul qilishni kuchaytiramiz\n\n"
            "✅ <b>Natija:</b> ishonchli qaror qabul qiladigan mutaxassis."
        ),
        "ru": (
            "🧠 <b>Индивидуальные консультации и коучинг</b>\n\n"
            "Хотите профессионального роста?\n\n"
            "Мы:\n"
            "• проводим персональный анализ\n"
            "• составляем план развития\n"
            "• усиливаем навыки принятия решений\n\n"
            "✅ <b>Результат:</b> уверенный и сильный специалист."
        ),
    },
}
SERVICE_5_TEXTS = {
    "service_5_1": {
        "uz": (
            "🔍 <b>Litsenziya talablarini tahlil qilish</b>\n\n"
            "Qaysi hujjatlar kerak? Qanday shartlar bajarilishi lozim?\n\n"
            "Biz:\n"
            "• faoliyatingizni chuqur o‘rganamiz\n"
            "• aynan sizga kerak bo‘lgan litsenziya talablarini aniqlaymiz\n"
            "• noto‘g‘ri yoki ortiqcha talablarni oldindan bartaraf etamiz\n\n"
            "Bu xizmat:\n"
            "✔️ vaqtni tejaydi\n"
            "✔️ rad etilish xavfini kamaytiradi\n\n"
            "✅ <b>Natija:</b> aniq reja va xatosiz boshlang‘ich bosqich."
        ),
        "ru": (
            "🔍 <b>Анализ лицензионных требований</b>\n\n"
            "Какие документы нужны? Какие условия необходимо выполнить?\n\n"
            "Мы:\n"
            "• подробно изучаем вашу деятельность\n"
            "• определяем точные лицензионные требования\n"
            "• заранее устраняем лишние и ошибочные требования\n\n"
            "Эта услуга:\n"
            "✔️ экономит время\n"
            "✔️ снижает риск отказа\n\n"
            "✅ <b>Результат:</b> четкий план и правильный старт."
        ),
    },

    "service_5_2": {
        "uz": (
            "📑 <b>Hujjatlarni tayyorlash</b>\n\n"
            "Litsenziya olishda eng ko‘p xato hujjatlarda bo‘ladi.\n\n"
            "Biz:\n"
            "• barcha zarur hujjatlarni to‘liq ro‘yxatini shakllantiramiz\n"
            "• hujjatlarni qonunchilikka mos tayyorlaymiz\n"
            "• kamchilik va xatolarni oldindan tuzatamiz\n\n"
            "Bu xizmat:\n"
            "✔️ qayta topshirish holatlarini yo‘q qiladi\n"
            "✔️ jarayonni tezlashtiradi\n\n"
            "✅ <b>Natija:</b> to‘liq va mukammal hujjatlar paketi."
        ),
        "ru": (
            "📑 <b>Подготовка документов</b>\n\n"
            "Чаще всего отказ возникает из-за ошибок в документах.\n\n"
            "Мы:\n"
            "• формируем полный список необходимых документов\n"
            "• готовим их в соответствии с законодательством\n"
            "• заранее устраняем ошибки и недочеты\n\n"
            "Эта услуга:\n"
            "✔️ исключает повторную подачу\n"
            "✔️ ускоряет процесс\n\n"
            "✅ <b>Результат:</b> полный и корректный пакет документов."
        ),
    },

    "service_5_3": {
        "uz": (
            "🏛 <b>Davlat idoralariga topshirish</b>\n\n"
            "Davlat idoralari bilan ishlash ko‘p vaqt va asab talab qiladi.\n\n"
            "Biz:\n"
            "• hujjatlarni tegishli idoralarga o‘zimiz topshiramiz\n"
            "• to‘g‘ri bo‘lim va mutasaddilar bilan ishlaymiz\n"
            "• ortiqcha yurishlarni oldini olamiz\n\n"
            "Bu xizmat:\n"
            "✔️ byurokratik muammolardan xalos qiladi\n"
            "✔️ vaqtingizni tejaydi\n\n"
            "✅ <b>Natija:</b> tez va to‘g‘ri topshirilgan hujjatlar."
        ),
        "ru": (
            "🏛 <b>Подача документов в государственные органы</b>\n\n"
            "Работа с госорганами требует времени и нервов.\n\n"
            "Мы:\n"
            "• самостоятельно подаем документы в нужные органы\n"
            "• работаем с ответственными подразделениями\n"
            "• исключаем лишние хождения\n\n"
            "Эта услуга:\n"
            "✔️ избавляет от бюрократии\n"
            "✔️ экономит ваше время\n\n"
            "✅ <b>Результат:</b> быстро и правильно поданные документы."
        ),
    },

    "service_5_4": {
        "uz": (
            "🔄 <b>Jarayonni to‘liq kuzatib borish</b>\n\n"
            "Hujjat topshirildi, lekin javob yo‘qmi?\n\n"
            "Biz:\n"
            "• litsenziya jarayonini boshidan oxirigacha nazorat qilamiz\n"
            "• kechikish sabablarini aniqlaymiz\n"
            "• zarur bo‘lsa, tezlashtirish choralarini ko‘ramiz\n\n"
            "Bu xizmat:\n"
            "✔️ noaniqlikni yo‘q qiladi\n"
            "✔️ doimiy xabardorlikni ta’minlaydi\n\n"
            "✅ <b>Natija:</b> shaffof va nazoratdagi jarayon."
        ),
        "ru": (
            "🔄 <b>Полное сопровождение процесса</b>\n\n"
            "Документы поданы, но нет ответа?\n\n"
            "Мы:\n"
            "• контролируем процесс от начала до конца\n"
            "• выявляем причины задержек\n"
            "• при необходимости ускоряем процесс\n\n"
            "Эта услуга:\n"
            "✔️ устраняет неопределенность\n"
            "✔️ обеспечивает прозрачность\n\n"
            "✅ <b>Результат:</b> процесс под полным контролем."
        ),
    },

    "service_5_5": {
        "uz": (
            "❌➡️✅ <b>Rad etilgan litsenziyalarni qayta tiklash</b>\n\n"
            "Oldin rad etilgan litsenziya — oxiri emas.\n\n"
            "Biz:\n"
            "• rad etilish sabablarini tahlil qilamiz\n"
            "• xatolarni to‘g‘rilaymiz\n"
            "• hujjatlarni qayta mukammallashtiramiz\n\n"
            "Bu xizmat:\n"
            "✔️ ikkinchi imkoniyat beradi\n"
            "✔️ muvaffaqiyat ehtimolini oshiradi\n\n"
            "✅ <b>Natija:</b> to‘g‘ri va qayta topshirilgan ariza."
        ),
        "ru": (
            "❌➡️✅ <b>Восстановление отказанных лицензий</b>\n\n"
            "Отказ — это не конец.\n\n"
            "Мы:\n"
            "• анализируем причины отказа\n"
            "• исправляем ошибки\n"
            "• подготавливаем документы для повторной подачи\n\n"
            "Эта услуга:\n"
            "✔️ дает второй шанс\n"
            "✔️ повышает вероятность успеха\n\n"
            "✅ <b>Результат:</b> корректно повторно поданная заявка."
        ),
    },

    "service_5_6": {
        "uz": (
            "🏷 <b>Sertifikatlash xizmatlari</b>\n\n"
            "Sertifikatsiz faoliyat — katta huquqiy xavf.\n\n"
            "Biz:\n"
            "• kerakli sertifikatlarni aniqlaymiz\n"
            "• sertifikatlash jarayonini tashkil qilamiz\n"
            "• hujjatlarni tez va to‘g‘ri rasmiylashtiramiz\n\n"
            "Bu xizmat:\n"
            "✔️ tekshiruvlarda muammosiz o‘tishga yordam beradi\n"
            "✔️ biznesni qonuniy qiladi\n\n"
            "✅ <b>Natija:</b> sertifikatlangan va ishonchli faoliyat."
        ),
        "ru": (
            "🏷 <b>Сертификационные услуги</b>\n\n"
            "Работа без сертификатов — юридический риск.\n\n"
            "Мы:\n"
            "• определяем необходимые сертификаты\n"
            "• организуем процесс сертификации\n"
            "• оформляем документы быстро и правильно\n\n"
            "Эта услуга:\n"
            "✔️ помогает пройти проверки без проблем\n"
            "✔️ делает бизнес законным\n\n"
            "✅ <b>Результат:</b> сертифицированная деятельность."
        ),
    },

    "service_5_7": {
        "uz": (
            "⚖️ <b>Konsultatsiya va huquqiy yordam</b>\n\n"
            "Qonunchilikni bilmaslik — risk.\n\n"
            "Biz:\n"
            "• litsenziya va ruxsatnomalar bo‘yicha maslahat beramiz\n"
            "• huquqiy xavflarni tushuntiramiz\n"
            "• eng to‘g‘ri yo‘lni ko‘rsatamiz\n\n"
            "Bu xizmat:\n"
            "✔️ xatolarning oldini oladi\n"
            "✔️ qaror qabul qilishni osonlashtiradi\n\n"
            "✅ <b>Natija:</b> huquqiy himoyalangan biznes."
        ),
        "ru": (
            "⚖️ <b>Консультации и правовая поддержка</b>\n\n"
            "Незнание закона — это риск.\n\n"
            "Мы:\n"
            "• консультируем по лицензиям и разрешениям\n"
            "• объясняем юридические риски\n"
            "• предлагаем оптимальное решение\n\n"
            "Эта услуга:\n"
            "✔️ предотвращает ошибки\n"
            "✔️ упрощает принятие решений\n\n"
            "✅ <b>Результат:</b> юридически защищенный бизнес."
        ),
    },
}
SERVICE_6_TEXTS = {
    "service_6_1": {
        "uz": (
            "🔌 <b>Energiya iste’molini tahlil qilish</b>\n\n"
            "Elektr va energiya xarajatlari nazoratsiz ketayaptimi?\n\n"
            "Biz:\n"
            "• barcha energiya manbalarini tahlil qilamiz\n"
            "• qayerda va nima sabab ko‘p sarf bo‘layotganini aniqlaymiz\n"
            "• real raqamlar bilan holatni ko‘rsatamiz\n\n"
            "✅ <b>Natija:</b> energiya sarfining to‘liq va aniq manzarasi."
        ),
        "ru": (
            "🔌 <b>Анализ энергопотребления</b>\n\n"
            "Расходы на электроэнергию выходят из-под контроля?\n\n"
            "Мы:\n"
            "• анализируем все источники энергии\n"
            "• выявляем причины повышенного потребления\n"
            "• показываем реальную картину в цифрах\n\n"
            "✅ <b>Результат:</b> полная и точная картина энергопотребления."
        ),
    },

    "service_6_2": {
        "uz": (
            "🔥 <b>Ortiqcha energiya sarfini aniqlash</b>\n\n"
            "Keraksiz energiya sarfi — befoyda xarajat.\n\n"
            "Biz:\n"
            "• samarasiz uskunalarni aniqlaymiz\n"
            "• yo‘qotish nuqtalarini ko‘rsatamiz\n"
            "• texnik xatolarni ochib beramiz\n\n"
            "✅ <b>Natija:</b> ortiqcha xarajatlarni kamaytirish imkoniyati."
        ),
        "ru": (
            "🔥 <b>Выявление избыточного энергопотребления</b>\n\n"
            "Лишнее потребление энергии — это лишние расходы.\n\n"
            "Мы:\n"
            "• выявляем неэффективное оборудование\n"
            "• показываем точки потерь\n"
            "• обнаруживаем технические ошибки\n\n"
            "✅ <b>Результат:</b> возможность снизить лишние расходы."
        ),
    },

    "service_6_3": {
        "uz": (
            "💡 <b>Tejamkorlik bo‘yicha tavsiyalar</b>\n\n"
            "Kam sarflab, ko‘proq natija olish mumkin.\n\n"
            "Biz:\n"
            "• energiya tejamkor yechimlar taklif qilamiz\n"
            "• real sharoitga mos tavsiyalar beramiz\n"
            "• kam xarajatli yoki sarmoyasiz usullarni ko‘rsatamiz\n\n"
            "✅ <b>Natija:</b> kamroq to‘lov va yuqori samaradorlik."
        ),
        "ru": (
            "💡 <b>Рекомендации по энергосбережению</b>\n\n"
            "Можно тратить меньше и получать больше.\n\n"
            "Мы:\n"
            "• предлагаем энергоэффективные решения\n"
            "• даем рекомендации под реальные условия\n"
            "• показываем малозатратные способы экономии\n\n"
            "✅ <b>Результат:</b> меньшие затраты и высокая эффективность."
        ),
    },

    "service_6_4": {
        "uz": (
            "🏭 <b>Ishlab chiqarish uskunalarini tekshirish</b>\n\n"
            "Eskirgan yoki noto‘g‘ri sozlangan uskuna ko‘p energiya yutadi.\n\n"
            "Biz:\n"
            "• uskunalarni texnik tekshiramiz\n"
            "• samaradorlik darajasini baholaymiz\n"
            "• modernizatsiya bo‘yicha tavsiyalar beramiz\n\n"
            "✅ <b>Natija:</b> xavfsiz va samarali ishlaydigan uskunalar."
        ),
        "ru": (
            "🏭 <b>Проверка производственного оборудования</b>\n\n"
            "Изношенное или неправильно настроенное оборудование потребляет больше энергии.\n\n"
            "Мы:\n"
            "• проводим техническую проверку оборудования\n"
            "• оцениваем уровень эффективности\n"
            "• даем рекомендации по модернизации\n\n"
            "✅ <b>Результат:</b> безопасное и эффективное оборудование."
        ),
    },

    "service_6_5": {
        "uz": (
            "🚀 <b>Energiya samaradorligini oshirish loyihalari</b>\n\n"
            "Energiya tejamkorlik — uzoq muddatli foyda.\n\n"
            "Biz:\n"
            "• maxsus loyiha va yechimlar ishlab chiqamiz\n"
            "• energiya sarfini kamaytirish strategiyasini tuzamiz\n"
            "• iqtisodiy samarani hisoblab beramiz\n\n"
            "✅ <b>Natija:</b> barqaror va tejamkor ishlab chiqarish."
        ),
        "ru": (
            "🚀 <b>Проекты по повышению энергоэффективности</b>\n\n"
            "Энергоэффективность — это долгосрочная выгода.\n\n"
            "Мы:\n"
            "• разрабатываем специальные проекты и решения\n"
            "• формируем стратегию снижения энергопотребления\n"
            "• рассчитываем экономический эффект\n\n"
            "✅ <b>Результат:</b> устойчивое и экономичное производство."
        ),
    },

    "service_6_6": {
        "uz": (
            "📄 <b>Hisobot va texnik xulosa tayyorlash</b>\n\n"
            "Rasmiy hujjat — qaror qabul qilish asosi.\n\n"
            "Biz:\n"
            "• to‘liq energiya audit hisobotini tayyorlaymiz\n"
            "• texnik xulosalar beramiz\n"
            "• rahbar va tekshiruvlar uchun tayyorlaymiz\n\n"
            "✅ <b>Natija:</b> rasmiy va ishonchli texnik hujjatlar."
        ),
        "ru": (
            "📄 <b>Подготовка отчёта и технического заключения</b>\n\n"
            "Официальный отчет — основа для принятия решений.\n\n"
            "Мы:\n"
            "• готовим полный отчет по энергоаудиту\n"
            "• даем технические заключения\n"
            "• подготавливаем документы для руководства и проверок\n\n"
            "✅ <b>Результат:</b> официальные и надежные технические документы."
        ),
    },

    "service_6_7": {
        "uz": (
            "🧠 <b>Energiya audit bo‘yicha konsultatsiya</b>\n\n"
            "Qaysi yechim foydaliroq ekanini bilmoqchimisiz?\n\n"
            "Biz:\n"
            "• holatingizni tahlil qilamiz\n"
            "• individual maslahat beramiz\n"
            "• eng samarali yo‘lni ko‘rsatamiz\n\n"
            "✅ <b>Natija:</b> ongli qaror va uzoq muddatli tejamkorlik."
        ),
        "ru": (
            "🧠 <b>Консультации по энергетическому аудиту</b>\n\n"
            "Хотите выбрать наиболее выгодное решение?\n\n"
            "Мы:\n"
            "• анализируем вашу ситуацию\n"
            "• даем индивидуальные рекомендации\n"
            "• предлагаем самый эффективный путь\n\n"
            "✅ <b>Результат:</b> обоснованное решение и долгосрочная экономия."
        ),
    },
}
SERVICE_7_TEXTS = {
    "service_7_1": {
        "uz": (
            "📊 <b>Sotuv jarayonlarini tahlil qilish</b>\n\n"
            "Reklama bor, mijozlar bor, lekin sotuv pastmi?\n\n"
            "Biz:\n"
            "• sotuv jarayonini bosqichma-bosqich tahlil qilamiz\n"
            "• qayerda mijoz yo‘qolayotganini aniqlaymiz\n"
            "• zaif nuqtalarni aniq ko‘rsatamiz\n\n"
            "✅ <b>Natija:</b> sotuvni to‘xtatayotgan sabablar aniq bo‘ladi."
        ),
        "ru": (
            "📊 <b>Анализ процессов продаж</b>\n\n"
            "Реклама есть, клиенты есть, но продаж мало?\n\n"
            "Мы:\n"
            "• анализируем процесс продаж по этапам\n"
            "• выявляем места потери клиентов\n"
            "• показываем слабые точки\n\n"
            "✅ <b>Результат:</b> понятные причины низких продаж."
        ),
    },

    "service_7_2": {
        "uz": (
            "🧭 <b>Marketing strategiya ishlab chiqish</b>\n\n"
            "Tasodifiy reklama — tasodifiy natija.\n\n"
            "Biz:\n"
            "• biznes va bozorni tahlil qilamiz\n"
            "• maqsadli auditoriyani aniqlaymiz\n"
            "• ishlaydigan marketing strategiya tuzamiz\n\n"
            "✅ <b>Natija:</b> reja asosida ishlaydigan marketing."
        ),
        "ru": (
            "🧭 <b>Разработка маркетинговой стратегии</b>\n\n"
            "Случайная реклама — случайный результат.\n\n"
            "Мы:\n"
            "• анализируем бизнес и рынок\n"
            "• определяем целевую аудиторию\n"
            "• создаем эффективную стратегию\n\n"
            "✅ <b>Результат:</b> системный маркетинг с ростом."
        ),
    },

    "service_7_3": {
        "uz": (
            "🎯 <b>Target va reklama kampaniyalari</b>\n\n"
            "Reklamaga pul ketmoqda, lekin natija yo‘qmi?\n\n"
            "Biz:\n"
            "• to‘g‘ri auditoriyani aniqlaymiz\n"
            "• samarali reklama kampaniyalarini sozlaymiz\n"
            "• doimiy optimallashtiramiz\n\n"
            "✅ <b>Natija:</b> reklama orqali real mijozlar oqimi."
        ),
        "ru": (
            "🎯 <b>Таргетированная реклама и кампании</b>\n\n"
            "Деньги тратятся, а результата нет?\n\n"
            "Мы:\n"
            "• определяем нужную аудиторию\n"
            "• настраиваем эффективные кампании\n"
            "• постоянно оптимизируем рекламу\n\n"
            "✅ <b>Результат:</b> стабильный поток клиентов."
        ),
    },

    "service_7_4": {
        "uz": (
            "📱 <b>SMM — ijtimoiy tarmoqlar</b>\n\n"
            "Ijtimoiy tarmoqlarda bor bo‘lish yetarli emas — faol bo‘lish kerak.\n\n"
            "Biz:\n"
            "• kontent reja tuzamiz\n"
            "• sahifalarni professional yuritamiz\n"
            "• auditoriya bilan ishlaymiz\n\n"
            "✅ <b>Natija:</b> faol auditoriya va kuchli imij."
        ),
        "ru": (
            "📱 <b>SMM — социальные сети</b>\n\n"
            "Просто присутствовать недостаточно — нужно быть активными.\n\n"
            "Мы:\n"
            "• создаем контент-план\n"
            "• профессионально ведем страницы\n"
            "• работаем с аудиторией\n\n"
            "✅ <b>Результат:</b> активная аудитория и сильный бренд."
        ),
    },

    "service_7_5": {
        "uz": (
            "🏷 <b>Brendni rivojlantirish</b>\n\n"
            "Brend — bu faqat logo emas, bu ishonch.\n\n"
            "Biz:\n"
            "• brendingizni tahlil qilamiz\n"
            "• yagona vizual va kommunikatsiya uslubini yaratamiz\n"
            "• bozorda ajralib turishingizga yordam beramiz\n\n"
            "✅ <b>Natija:</b> ishonchli va esda qoladigan brend."
        ),
        "ru": (
            "🏷 <b>Развитие бренда</b>\n\n"
            "Бренд — это не только логотип, это доверие.\n\n"
            "Мы:\n"
            "• анализируем бренд\n"
            "• создаем единый стиль коммуникации\n"
            "• помогаем выделиться на рынке\n\n"
            "✅ <b>Результат:</b> узнаваемый и сильный бренд."
        ),
    },

    "service_7_6": {
        "uz": (
            "🔄 <b>Savdo voronkasi (Sales Funnel)</b>\n\n"
            "Mijoz keladi, lekin sotib olmay ketayaptimi?\n\n"
            "Biz:\n"
            "• mijoz yo‘lini to‘liq loyihalaymiz\n"
            "• har bosqichni optimallashtiramiz\n"
            "• avtomatlashtirilgan voronka quramiz\n\n"
            "✅ <b>Natija:</b> tizimli va barqaror sotuv."
        ),
        "ru": (
            "🔄 <b>Воронка продаж (Sales Funnel)</b>\n\n"
            "Клиенты приходят, но не покупают?\n\n"
            "Мы:\n"
            "• проектируем путь клиента\n"
            "• оптимизируем каждый этап\n"
            "• автоматизируем воронку\n\n"
            "✅ <b>Результат:</b> стабильные и прогнозируемые продажи."
        ),
    },

    "service_7_7": {
        "uz": (
            "🧠 <b>CRM orqali sotuvni oshirish</b>\n\n"
            "Mijozlar bazasi bor, lekin ishlamayaptimi?\n\n"
            "Biz:\n"
            "• CRM orqali mijozlar bilan ishlashni yo‘lga qo‘yamiz\n"
            "• qayta sotuv mexanizmlarini sozlaymiz\n"
            "• menejerlar faoliyatini nazorat qilamiz\n\n"
            "✅ <b>Natija:</b> har bir mijozdan maksimal foyda."
        ),
        "ru": (
            "🧠 <b>Увеличение продаж через CRM</b>\n\n"
            "Есть база клиентов, но она не работает?\n\n"
            "Мы:\n"
            "• настраиваем работу с клиентами через CRM\n"
            "• внедряем повторные продажи\n"
            "• контролируем работу менеджеров\n\n"
            "✅ <b>Результат:</b> максимум прибыли с каждого клиента."
        ),
    },

    "service_7_8": {
        "uz": (
            "🧪 <b>Konsultatsiya va marketing audit</b>\n\n"
            "Qayerdan boshlashni bilmayapsizmi?\n\n"
            "Biz:\n"
            "• marketing holatingizni tahlil qilamiz\n"
            "• xatolar va imkoniyatlarni ko‘rsatamiz\n"
            "• aniq tavsiyalar beramiz\n\n"
            "✅ <b>Natija:</b> ongli strategiya va aniq reja."
        ),
        "ru": (
            "🧪 <b>Консультации и маркетинговый аудит</b>\n\n"
            "Не знаете, с чего начать?\n\n"
            "Мы:\n"
            "• анализируем маркетинг\n"
            "• выявляем ошибки и возможности\n"
            "• даем четкие рекомендации\n\n"
            "✅ <b>Результат:</b> понятная стратегия и план действий."
        ),
    },
}
