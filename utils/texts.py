SPORT_NAMES = {
    "uz": {
        "football":    "⚽ Futbol",
        "basketball":  "🏀 Basketbol",
        "tennis":      "🎾 Tennis",
        "volleyball":  "🏐 Voleybol",
        "tabletennis": "🏓 Stol tennis",
        "chess":       "♟️ Shaxmat",
        "boxing":      "🥊 Boks",
        "fitness":     "💪 Fitness",
    },
    "ru": {
        "football":    "⚽ Футбол",
        "basketball":  "🏀 Баскетбол",
        "tennis":      "🎾 Теннис",
        "volleyball":  "🏐 Волейбол",
        "tabletennis": "🏓 Настольный теннис",
        "chess":       "♟️ Шахматы",
        "boxing":      "🥊 Бокс",
        "fitness":     "💪 Фитнес",
    },
}

LEVEL_NAMES = {
    "uz": {"beginner": "🟢 Yangi", "middle": "🟡 O'rta", "pro": "🔴 Pro"},
    "ru": {"beginner": "🟢 Новичок", "middle": "🟡 Средний", "pro": "🔴 Про"},
}

FORMAT_NAMES = {
    "uz": {"1x1": "1×1", "2x2": "2×2", "5x5": "5×5", "any": "🔀 Istalgan"},
    "ru": {"1x1": "1×1", "2x2": "2×2", "5x5": "5×5", "any": "🔀 Любой"},
}

TIME_NAMES = {
    "uz": {
        "morning":   "🌅 Ertalab",
        "afternoon": "☀️ Tushdan keyin",
        "evening":   "🌙 Kechqurun",
        "weekend":   "🏖️ Dam olish",
    },
    "ru": {
        "morning":   "🌅 Утром",
        "afternoon": "☀️ Днём",
        "evening":   "🌙 Вечером",
        "weekend":   "🏖️ В выходные",
    },
}

AGE_GROUPS = ["15-18", "19-25", "26-35", "36+"]
SPORTS = ["football", "basketball", "tennis", "volleyball", "tabletennis", "chess", "boxing", "fitness"]
LEVELS = ["beginner", "middle", "pro"]
FORMATS = ["1x1", "2x2", "5x5", "any"]
TIMES = ["morning", "afternoon", "evening", "weekend"]

_D = "─────────────────────"

TEXTS = {
    "uz": {
        # ── Til tanlash ──────────────────────────────────────────────────────
        "choose_lang": (
            "🌐  <b>Tilni tanlang</b>\n"
            "     <i>Выберите язык</i>"
        ),

        # ── Yangi foydalanuvchi ───────────────────────────────────────────────
        "welcome": (
            f"🏆  <b>KIGO BOT</b>\n"
            f"{_D}\n"
            "Sport hamkor topish uchun\n"
            "eng qulay Telegram bot!\n\n"
            "✅  Darajaga mos\n"
            "✅  Shahringizda\n"
            "✅  Qulay vaqtingizda\n\n"
            f"{_D}\n"
            "<i>Keling, profilingizni to'ldiramiz — atigi 2 daqiqa!</i>"
        ),

        # ── Qaytib kelgan foydalanuvchi ───────────────────────────────────────
        "welcome_back": (
            f"👋  <b>Salom, {'{name}'}!</b>\n"
            f"{_D}\n"
            "🏆  <b>KIGO BOT</b>  —  Sport hamkor\n\n"
            "📍  {city}   |   ⭐  {rating}\n"
            "{sports_line}\n"
            f"{_D}"
        ),

        # ── Registratsiya bosqichlari ─────────────────────────────────────────
        "ask_name": (
            f"{_D}\n"
            "✏️   <b>1 / 6  —  Ism</b>\n"
            f"{_D}\n\n"
            "Ismingizni kiriting:\n"
            "<i>(2–30 belgi)</i>"
        ),
        "invalid_name": (
            "⚠️  Ism <b>2–30</b> belgi bo'lishi kerak.\n"
            "Qaytadan kiriting:"
        ),
        "ask_age": (
            f"{_D}\n"
            "🎂   <b>2 / 6  —  Yosh</b>\n"
            f"{_D}\n\n"
            "Yosh guruhingizni tanlang:"
        ),
        "ask_sports": (
            f"{_D}\n"
            "🏅   <b>3 / 6  —  Sportlar</b>\n"
            f"{_D}\n\n"
            "Qaysi sportlar bilan shug'ullanasiz?\n"
            "<i>Ko'p tanlash mumkin  ·  ✅ = tanlangan</i>"
        ),
        "min_sport": "⚠️  Kamida <b>1 ta</b> sport tanlang!",
        "ask_level": (
            f"{_D}\n"
            "📊   <b>4 / 6  —  Daraja</b>\n"
            f"{_D}\n\n"
            "<b>{sport}</b> bo'yicha darajangiz:"
        ),
        "ask_city": (
            f"{_D}\n"
            "📍   <b>5 / 6  —  Shahar</b>\n"
            f"{_D}\n\n"
            "Shahringizni yozing yoki\n"
            "📍 GPS tugmasini bosing:"
        ),
        "ask_times": (
            f"{_D}\n"
            "⏰   <b>6 / 6  —  Vaqt</b>\n"
            f"{_D}\n\n"
            "Qachon o'ynashga qulay?\n"
            "<i>Ko'p tanlash mumkin  ·  ✅ = tanlangan</i>"
        ),
        "min_time": "⚠️  Kamida <b>1 ta</b> vaqt tanlang!",
        "ask_phone": (
            f"{_D}\n"
            "📱   <b>Telefon raqam</b>\n"
            f"{_D}\n\n"
            "Hamkor taklif qabul qilganda,\n"
            "telefon raqamingiz unga yuboriladi.\n\n"
            "<i>⏭️ O'tkazib yuborish ham mumkin</i>"
        ),
        "phone_skip": "⏭️  O'tkazib yuborish",
        "btn_share_phone": "📱  Raqamni ulashish",

        # ── Profil saqlandi ───────────────────────────────────────────────────
        "profile_saved": (
            f"🎉  <b>Profil tayyor!</b>\n"
            f"{_D}\n\n"
            "Endi sport hamkor qidira olasiz.\n\n"
            "🔍  /find  —  Hamkor qidirish\n"
            "👤  /profile  —  Profilni ko'rish\n"
            "📩  /invites  —  Takliflar\n"
            "❓  /help  —  Yordam"
        ),
        "profile_not_found": (
            "⚠️  <b>Profil topilmadi</b>\n\n"
            "Boshlash uchun /start yuboring."
        ),

        # ── Profil ko'rinishi ─────────────────────────────────────────────────
        "your_profile": (
            f"👤  <b>Sizning profilingiz</b>\n"
            f"{_D}\n\n"
            "🏷  Ism:       <b>{name}</b>\n"
            "🎂  Yosh:      <b>{age}</b>\n"
            "📍  Shahar:   <b>{city}</b>\n"
            "📱  Tel:        <b>{phone}</b>\n"
            "⏰  Vaqt:      <b>{times}</b>\n"
            "⭐  Reyting:  <b>{rating}</b>  <i>({rating_count} baho)</i>\n\n"
            f"{_D}\n"
            "<b>🏅 Sportlar:</b>\n"
            "{sports}"
        ),

        # ── Qidirish ──────────────────────────────────────────────────────────
        "no_matches": (
            f"😔  <b>Hozircha mos hamkor topilmadi</b>\n"
            f"{_D}\n\n"
            "Ko'proq foydalanuvchi qo'shilgach\n"
            "qayta urinib ko'ring.\n\n"
            "<i>Botni do'stlaringizga ulashing!</i>"
        ),
        "choose_sport_find": (
            f"🔍  <b>Hamkor qidirish</b>\n"
            f"{_D}\n\n"
            "Qaysi sport bo'yicha hamkor qidirasiz?"
        ),
        "matches_header": (
            f"🎯  <b>{'{count}'} ta mos hamkor topildi!</b>\n"
            f"{_D}\n\n"
        ),
        "match_item": (
            "👤  <b>{name}</b>  —  📍 {city}\n"
            "    {sport}  ·  {level}\n"
            "    ⏰ {times}\n"
            "    🎯  Mos: <b>{score}%</b>\n\n"
        ),

        # ── Taklif ────────────────────────────────────────────────────────────
        "invite_sent": (
            "📨  <b>Taklif yuborildi!</b>\n\n"
            "<b>{name}</b> qabul qilsa xabar beraman. 🔔"
        ),
        "already_invited": "⚠️  Bu foydalanuvchiga allaqachon taklif yuborgansiz.",
        "invite_received": (
            f"🔔  <b>Yangi hamkor taklifi!</b>\n"
            f"{_D}\n\n"
            "👤  <b>{name}</b>\n"
            "📍  {city}\n"
            "🏅  {sport}  ·  {level}\n\n"
            "<i>Qabul qilasizmi?</i>"
        ),
        "invite_accepted_sender": (
            f"🎉  <b>Taklif qabul qilindi!</b>\n"
            f"{_D}\n\n"
            "👤  <b>{name}</b>\n"
            "📱  Tel:  <code>{phone}</code>\n"
            "💬  Telegram:  @{username}\n\n"
            "<i>Bog'laning va o'yin belgilang! 🏆</i>"
        ),
        "invite_accepted_sender_phone_only": (
            f"🎉  <b>Taklif qabul qilindi!</b>\n"
            f"{_D}\n\n"
            "👤  <b>{name}</b>\n"
            "📱  Tel:  <code>{phone}</code>\n\n"
            "<i>Bog'laning va o'yin belgilang! 🏆</i>"
        ),
        "invite_accepted_sender_username_only": (
            f"🎉  <b>Taklif qabul qilindi!</b>\n"
            f"{_D}\n\n"
            "👤  <b>{name}</b>\n"
            "💬  Telegram:  @{username}\n\n"
            "<i>Bog'laning va o'yin belgilang! 🏆</i>"
        ),
        "invite_accepted_sender_no_contact": (
            f"🎉  <b>Taklif qabul qilindi!</b>\n"
            f"{_D}\n\n"
            "👤  <b>{name}</b>\n\n"
            "<i>Ular siz bilan bog'lanishadi.</i>"
        ),
        "invite_rejected_sender": (
            "😔  <b>{name}</b> taklifingizni rad etdi.\n\n"
            "<i>Boshqa hamkor qidiring!</i>"
        ),
        "you_accepted": (
            f"✅  <b>Taklif qabul qilindi!</b>\n"
            f"{_D}\n\n"
            "👤  <b>{name}</b>\n"
            "📱  Tel:  <code>{phone}</code>\n"
            "💬  Telegram:  @{username}\n\n"
            "<i>Bog'laning va o'yin belgilang! 🏆</i>"
        ),
        "you_accepted_phone_only": (
            f"✅  <b>Taklif qabul qilindi!</b>\n"
            f"{_D}\n\n"
            "👤  <b>{name}</b>\n"
            "📱  Tel:  <code>{phone}</code>\n\n"
            "<i>Bog'laning va o'yin belgilang! 🏆</i>"
        ),
        "you_accepted_username_only": (
            f"✅  <b>Taklif qabul qilindi!</b>\n"
            f"{_D}\n\n"
            "👤  <b>{name}</b>\n"
            "💬  Telegram:  @{username}\n\n"
            "<i>Bog'laning va o'yin belgilang! 🏆</i>"
        ),
        "you_accepted_no_contact": (
            "✅  <b>Taklif qabul qilindi!</b>\n\n"
            "<i>Hamkoringiz siz bilan bog'lanadi.</i>"
        ),
        "you_rejected": "❌  Siz taklifni rad etdingiz.",

        # ── Takliflar ro'yxati ────────────────────────────────────────────────
        "no_invites": (
            f"📭  <b>Takliflar yo'q</b>\n"
            f"{_D}\n\n"
            "Hozircha hech kim taklif yubormagani.\n"
            "<i>🔍 /find orqali o'zingiz qidiring!</i>"
        ),
        "invites_header": f"📩  <b>Kelgan takliflar</b>\n{_D}\n\n",
        "invite_list_item": "▸  <b>{name}</b>  —  {sport}  ·  {level}\n",

        # ── Reyting ───────────────────────────────────────────────────────────
        "rate_partner": (
            f"⭐  <b>O'yin qanday o'tdi?</b>\n"
            f"{_D}\n\n"
            "<b>{name}</b> ga baho bering:"
        ),
        "rating_saved": "✅  Bahoyingiz saqlandi! Rahmat 🙏",
        "already_rated": "⚠️  Siz bu o'yin uchun allaqachon baho bergansiz.",

        # ── Yordam ────────────────────────────────────────────────────────────
        "help_text": (
            f"❓  <b>KIGO BOT  —  Qo'llanma</b>\n"
            f"{_D}\n\n"
            "🔍  /find      —  Hamkor qidirish\n"
            "👤  /profile  —  Profilni ko'rish\n"
            "📩  /invites  —  Kelgan takliflar\n"
            "🔄  /start     —  Profilni yangilash\n"
            "❓  /help      —  Shu qo'llanma\n\n"
            f"{_D}\n"
            "📊  <b>Qidiruv algoritmi:</b>\n\n"
            "📍  Bir xil shahar          +40 ball\n"
            "🎯  Bir xil daraja           +30 ball\n"
            "⏰  Mos vaqt (har biri)   +15 ball\n"
            "🔀  Bir xil format            +10 ball\n"
            "🎂  Yosh guruhi              +5 ball"
        ),

        # ── Tugmalar ──────────────────────────────────────────────────────────
        "send_gps": "📍  GPS yuborish",
        "btn_done": "✅  Tayyor",
        "btn_invite": "📨  Taklif yuborish",
        "btn_accept": "✅  Qabul qilish",
        "btn_reject": "❌  Rad etish",
        "btn_edit_profile": "✏️  Profilni yangilash",
        "btn_refresh": "🔄  Qayta qidirish",
        "btn_find": "🔍  Hamkor topish",
        "btn_profile": "👤  Profilim",
        "btn_invites": "📩  Takliflar",
        "btn_help": "❓  Yordam",
        "btn_update_profile": "✏️  Profilni yangilash",
    },

    "ru": {
        # ── Язык ─────────────────────────────────────────────────────────────
        "choose_lang": (
            "🌐  <b>Tilni tanlang</b>\n"
            "     <i>Выберите язык</i>"
        ),

        # ── Новый пользователь ────────────────────────────────────────────────
        "welcome": (
            f"🏆  <b>KIGO BOT</b>\n"
            f"{_D}\n"
            "Бот для поиска партнёра по спорту!\n\n"
            "✅  По уровню игры\n"
            "✅  В вашем городе\n"
            "✅  В удобное время\n\n"
            f"{_D}\n"
            "<i>Заполним профиль за 2 минуты!</i>"
        ),

        # ── Возвращающийся пользователь ───────────────────────────────────────
        "welcome_back": (
            f"👋  <b>Привет, {'{name}'}!</b>\n"
            f"{_D}\n"
            "🏆  <b>KIGO BOT</b>  —  Поиск партнёра\n\n"
            "📍  {city}   |   ⭐  {rating}\n"
            "{sports_line}\n"
            f"{_D}"
        ),

        # ── Регистрация ───────────────────────────────────────────────────────
        "ask_name": (
            f"{_D}\n"
            "✏️   <b>1 / 6  —  Имя</b>\n"
            f"{_D}\n\n"
            "Введите ваше имя:\n"
            "<i>(2–30 символов)</i>"
        ),
        "invalid_name": (
            "⚠️  Имя должно быть <b>2–30</b> символов.\n"
            "Введите снова:"
        ),
        "ask_age": (
            f"{_D}\n"
            "🎂   <b>2 / 6  —  Возраст</b>\n"
            f"{_D}\n\n"
            "Выберите возрастную группу:"
        ),
        "ask_sports": (
            f"{_D}\n"
            "🏅   <b>3 / 6  —  Виды спорта</b>\n"
            f"{_D}\n\n"
            "Какими видами спорта занимаетесь?\n"
            "<i>Можно несколько  ·  ✅ = выбрано</i>"
        ),
        "min_sport": "⚠️  Выберите хотя бы <b>1</b> вид спорта!",
        "ask_level": (
            f"{_D}\n"
            "📊   <b>4 / 6  —  Уровень</b>\n"
            f"{_D}\n\n"
            "Ваш уровень в <b>{sport}</b>:"
        ),
        "ask_city": (
            f"{_D}\n"
            "📍   <b>5 / 6  —  Город</b>\n"
            f"{_D}\n\n"
            "Напишите город или нажмите\n"
            "📍 GPS:"
        ),
        "ask_times": (
            f"{_D}\n"
            "⏰   <b>6 / 6  —  Время</b>\n"
            f"{_D}\n\n"
            "Когда удобно играть?\n"
            "<i>Можно несколько  ·  ✅ = выбрано</i>"
        ),
        "min_time": "⚠️  Выберите хотя бы <b>1</b> время!",
        "ask_phone": (
            f"{_D}\n"
            "📱   <b>Номер телефона</b>\n"
            f"{_D}\n\n"
            "При принятии приглашения\n"
            "партнёр получит ваш номер.\n\n"
            "<i>⏭️ Можно пропустить</i>"
        ),
        "phone_skip": "⏭️  Пропустить",
        "btn_share_phone": "📱  Поделиться номером",

        # ── Профиль сохранён ──────────────────────────────────────────────────
        "profile_saved": (
            f"🎉  <b>Профиль готов!</b>\n"
            f"{_D}\n\n"
            "Теперь можно искать партнёра!\n\n"
            "🔍  /find      —  Найти партнёра\n"
            "👤  /profile  —  Мой профиль\n"
            "📩  /invites  —  Приглашения\n"
            "❓  /help      —  Справка"
        ),
        "profile_not_found": (
            "⚠️  <b>Профиль не найден</b>\n\n"
            "Отправьте /start чтобы начать."
        ),

        # ── Просмотр профиля ─────────────────────────────────────────────────
        "your_profile": (
            f"👤  <b>Ваш профиль</b>\n"
            f"{_D}\n\n"
            "🏷  Имя:         <b>{name}</b>\n"
            "🎂  Возраст:    <b>{age}</b>\n"
            "📍  Город:       <b>{city}</b>\n"
            "📱  Тел:           <b>{phone}</b>\n"
            "⏰  Время:       <b>{times}</b>\n"
            "⭐  Рейтинг:    <b>{rating}</b>  <i>({rating_count} оценок)</i>\n\n"
            f"{_D}\n"
            "<b>🏅 Виды спорта:</b>\n"
            "{sports}"
        ),

        # ── Поиск ─────────────────────────────────────────────────────────────
        "no_matches": (
            f"😔  <b>Партнёров пока нет</b>\n"
            f"{_D}\n\n"
            "Попробуйте позже, когда появятся\n"
            "новые пользователи.\n\n"
            "<i>Расскажите друзьям о боте!</i>"
        ),
        "choose_sport_find": (
            f"🔍  <b>Поиск партнёра</b>\n"
            f"{_D}\n\n"
            "По какому виду спорта ищете?"
        ),
        "matches_header": (
            f"🎯  <b>Найдено {'{count}'} партнёров!</b>\n"
            f"{_D}\n\n"
        ),
        "match_item": (
            "👤  <b>{name}</b>  —  📍 {city}\n"
            "    {sport}  ·  {level}\n"
            "    ⏰ {times}\n"
            "    🎯  Совпадение: <b>{score}%</b>\n\n"
        ),

        # ── Приглашения ───────────────────────────────────────────────────────
        "invite_sent": (
            "📨  <b>Приглашение отправлено!</b>\n\n"
            "Сообщу, когда <b>{name}</b> примет. 🔔"
        ),
        "already_invited": "⚠️  Вы уже отправляли приглашение этому пользователю.",
        "invite_received": (
            f"🔔  <b>Новое приглашение!</b>\n"
            f"{_D}\n\n"
            "👤  <b>{name}</b>\n"
            "📍  {city}\n"
            "🏅  {sport}  ·  {level}\n\n"
            "<i>Принять приглашение?</i>"
        ),
        "invite_accepted_sender": (
            f"🎉  <b>Приглашение принято!</b>\n"
            f"{_D}\n\n"
            "👤  <b>{name}</b>\n"
            "📱  Тел:  <code>{phone}</code>\n"
            "💬  Telegram:  @{username}\n\n"
            "<i>Свяжитесь и назначьте игру! 🏆</i>"
        ),
        "invite_accepted_sender_phone_only": (
            f"🎉  <b>Приглашение принято!</b>\n"
            f"{_D}\n\n"
            "👤  <b>{name}</b>\n"
            "📱  Тел:  <code>{phone}</code>\n\n"
            "<i>Свяжитесь и назначьте игру! 🏆</i>"
        ),
        "invite_accepted_sender_username_only": (
            f"🎉  <b>Приглашение принято!</b>\n"
            f"{_D}\n\n"
            "👤  <b>{name}</b>\n"
            "💬  Telegram:  @{username}\n\n"
            "<i>Свяжитесь и назначьте игру! 🏆</i>"
        ),
        "invite_accepted_sender_no_contact": (
            f"🎉  <b>Приглашение принято!</b>\n"
            f"{_D}\n\n"
            "👤  <b>{name}</b>\n\n"
            "<i>Они свяжутся с вами сами.</i>"
        ),
        "invite_rejected_sender": (
            "😔  <b>{name}</b> отклонил приглашение.\n\n"
            "<i>Поищите другого партнёра!</i>"
        ),
        "you_accepted": (
            f"✅  <b>Приглашение принято!</b>\n"
            f"{_D}\n\n"
            "👤  <b>{name}</b>\n"
            "📱  Тел:  <code>{phone}</code>\n"
            "💬  Telegram:  @{username}\n\n"
            "<i>Свяжитесь и назначьте игру! 🏆</i>"
        ),
        "you_accepted_phone_only": (
            f"✅  <b>Приглашение принято!</b>\n"
            f"{_D}\n\n"
            "👤  <b>{name}</b>\n"
            "📱  Тел:  <code>{phone}</code>\n\n"
            "<i>Свяжитесь и назначьте игру! 🏆</i>"
        ),
        "you_accepted_username_only": (
            f"✅  <b>Приглашение принято!</b>\n"
            f"{_D}\n\n"
            "👤  <b>{name}</b>\n"
            "💬  Telegram:  @{username}\n\n"
            "<i>Свяжитесь и назначьте игру! 🏆</i>"
        ),
        "you_accepted_no_contact": (
            "✅  <b>Приглашение принято!</b>\n\n"
            "<i>Партнёр свяжется с вами.</i>"
        ),
        "you_rejected": "❌  Вы отклонили приглашение.",

        "no_invites": (
            f"📭  <b>Приглашений нет</b>\n"
            f"{_D}\n\n"
            "Пока никто не приглашал.\n"
            "<i>🔍 Поищите сами через /find!</i>"
        ),
        "invites_header": f"📩  <b>Входящие приглашения</b>\n{_D}\n\n",
        "invite_list_item": "▸  <b>{name}</b>  —  {sport}  ·  {level}\n",

        "rate_partner": (
            f"⭐  <b>Как прошла игра?</b>\n"
            f"{_D}\n\n"
            "Оцените <b>{name}</b>:"
        ),
        "rating_saved": "✅  Оценка сохранена! Спасибо 🙏",
        "already_rated": "⚠️  Вы уже оценивали эту игру.",

        "help_text": (
            f"❓  <b>KIGO BOT  —  Справка</b>\n"
            f"{_D}\n\n"
            "🔍  /find      —  Найти партнёра\n"
            "👤  /profile  —  Мой профиль\n"
            "📩  /invites  —  Приглашения\n"
            "🔄  /start     —  Обновить профиль\n"
            "❓  /help      —  Справка\n\n"
            f"{_D}\n"
            "📊  <b>Алгоритм поиска:</b>\n\n"
            "📍  Один город                   +40 очков\n"
            "🎯  Одинаковый уровень      +30 очков\n"
            "⏰  Совпадение по времени  +15 очков\n"
            "🔀  Одинаковый формат        +10 очков\n"
            "🎂  Возрастная группа          +5 очков"
        ),

        "send_gps": "📍  Отправить GPS",
        "btn_done": "✅  Готово",
        "btn_invite": "📨  Пригласить",
        "btn_accept": "✅  Принять",
        "btn_reject": "❌  Отклонить",
        "btn_edit_profile": "✏️  Изменить профиль",
        "btn_refresh": "🔄  Обновить поиск",
        "btn_find": "🔍  Найти партнёра",
        "btn_profile": "👤  Мой профиль",
        "btn_invites": "📩  Приглашения",
        "btn_help": "❓  Справка",
        "btn_update_profile": "✏️  Обновить профиль",
    },
}


def t(lang: str, key: str, **kwargs) -> str:
    text = TEXTS.get(lang, TEXTS["uz"]).get(key, key)
    return text.format(**kwargs) if kwargs else text


def sport_name(sport: str, lang: str) -> str:
    return SPORT_NAMES.get(lang, SPORT_NAMES["uz"]).get(sport, sport)


def level_name(level: str, lang: str) -> str:
    return LEVEL_NAMES.get(lang, LEVEL_NAMES["uz"]).get(level, level)


def format_name(fmt: str, lang: str) -> str:
    return FORMAT_NAMES.get(lang, FORMAT_NAMES["uz"]).get(fmt, fmt)


def time_name(time_key: str, lang: str) -> str:
    return TIME_NAMES.get(lang, TIME_NAMES["uz"]).get(time_key, time_key)


def times_display(times: list, lang: str) -> str:
    return "  ·  ".join(time_name(t_item, lang) for t_item in times)
