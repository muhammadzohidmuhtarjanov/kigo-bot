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
        "weekend":   "🏖️ Dam olish kuni",
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

TEXTS = {
    "uz": {
        "choose_lang": "🌐 Tilni tanlang / Выберите язык:",
        "welcome": (
            "👋 <b>Kigo ga xush kelibsiz!</b>\n\n"
            "Sport hamkor topish botiman.\n"
            "Keling, profilingizni 2 daqiqada to'ldiramiz."
        ),
        "ask_name": "1/6 — <b>Ismingiz nima?</b>\n\n<i>(2–30 belgi)</i>",
        "invalid_name": "❌ Ism 2–30 belgi bo'lishi kerak. Qaytadan kiriting:",
        "ask_age": "2/6 — <b>Yoshingizni tanlang:</b>",
        "ask_sports": (
            "3/6 — <b>Qaysi sportlar bilan shug'ullanasiz?</b>\n\n"
            "<i>Ko'p tanlash mumkin. ✅ = tanlangan.</i>"
        ),
        "min_sport": "⚠️ Kamida 1 ta sport tanlang!",
        "ask_level": "4/6 — <b>{sport}</b> bo'yicha darajangiz:",
        "ask_city": (
            "5/6 — <b>Shahringiz?</b>\n\n"
            "<i>Shahar nomini yozing yoki 📍 GPS tugmasini bosing.</i>"
        ),
        "ask_times": (
            "6/6 — <b>Qachon o'ynashga qulay?</b>\n\n"
            "<i>Ko'p tanlash mumkin. ✅ = tanlangan.</i>"
        ),
        "min_time": "⚠️ Kamida 1 ta vaqt tanlang!",
        "profile_saved": (
            "✅ <b>Profil saqlandi!</b>\n\n"
            "/find — Hamkor qidirish\n"
            "/profile — Profilni ko'rish\n"
            "/invites — Takliflar"
        ),
        "profile_not_found": "❌ Profil topilmadi. /start buyrug'ini yuboring.",
        "your_profile": (
            "👤 <b>Sizning profilingiz</b>\n\n"
            "👤 Ism: <b>{name}</b>\n"
            "🎂 Yosh: <b>{age}</b>\n"
            "📍 Shahar: <b>{city}</b>\n"
            "⏰ Qulay vaqt: <b>{times}</b>\n"
            "⭐ Reyting: <b>{rating}</b> ({rating_count} baho)\n\n"
            "<b>Sportlar:</b>\n{sports}"
        ),
        "no_matches": (
            "😔 Hozircha mos hamkor topilmadi.\n\n"
            "Ko'proq foydalanuvchi qo'shilgach qayta urinib ko'ring."
        ),
        "choose_sport_find": "🔍 Qaysi sport bo'yicha hamkor qidirasiz?",
        "matches_header": "🎯 <b>{count} ta mos hamkor topildi!</b>\n\n",
        "match_item": "{num}. <b>{name}</b> — {city}\n   {sport} | {level} | {format}\n   ⏰ {times}\n   Mos: <b>{score}%</b>\n\n",
        "invite_sent": "✅ Taklif yuborildi! <b>{name}</b> qabul qilsa xabar beraman.",
        "already_invited": "⚠️ Siz bu foydalanuvchiga allaqachon taklif yuborgansiz.",
        "invite_received": (
            "🏆 <b>Sizga hamkor taklifi keldi!</b>\n\n"
            "👤 <b>{name}</b> ({city}) siz bilan {sport} o'ynashni taklif qilmoqda.\n"
            "📊 Daraja: <b>{level}</b> | Format: <b>{format}</b>"
        ),
        "invite_accepted_sender": (
            "🎉 <b>{name}</b> taklifingizni qabul qildi!\n\n"
            "Ulaning: @{username}"
        ),
        "invite_accepted_sender_no_username": (
            "🎉 <b>{name}</b> taklifingizni qabul qildi!\n\n"
            "Username yo'q, lekin ular siz bilan bog'lanishadi."
        ),
        "invite_rejected_sender": "😔 <b>{name}</b> taklifingizni rad etdi.",
        "you_accepted": (
            "✅ Siz taklifni qabul qildingiz!\n\n"
            "📱 Hamkoringiz: @{username}"
        ),
        "you_accepted_no_username": "✅ Siz taklifni qabul qildingiz! Hamkoringiz siz bilan bog'lanadi.",
        "you_rejected": "❌ Siz taklifni rad etdingiz.",
        "no_invites": "📭 Hozircha kelgan taklif yo'q.",
        "invites_header": "📩 <b>Kelgan takliflar:</b>\n\n",
        "invite_list_item": "{num}. <b>{name}</b> — {sport} ({level})\n",
        "rate_partner": "⭐ <b>{name}</b> bilan o'yin qanday o'tdi? Baho bering:",
        "rating_saved": "✅ Bahoyingiz saqlandi! Rahmat.",
        "already_rated": "⚠️ Siz bu o'yin uchun allaqachon baho bergansiz.",
        "help_text": (
            "📖 <b>Kigo Bot — Qo'llanma</b>\n\n"
            "/start — Profilni boshlash yoki yangilash\n"
            "/find — Hamkor qidirish\n"
            "/profile — Profilni ko'rish\n"
            "/invites — Kelgan takliflar\n"
            "/help — Shu qo'llanma\n\n"
            "<b>Qidiruv algoritmi:</b>\n"
            "• Bir xil shahar: +40 ball\n"
            "• Bir xil daraja: +30 ball\n"
            "• Mos vaqt (har biri): +15 ball\n"
            "• Bir xil format: +10 ball\n"
            "• Yosh guruhi: +5 ball"
        ),
        "profile_edit_prompt": "Nima o'zgartirmoqchisiz?",
        "send_gps": "📍 GPS yuborish",
        "skip_gps": "✏️ Matn yozish",
        "btn_done": "✅ Tayyor",
        "btn_invite": "📨 Taklif yuborish",
        "btn_accept": "✅ Qabul qilish",
        "btn_reject": "❌ Rad etish",
        "btn_edit_profile": "✏️ Profilni tahrirlash",
        "btn_refresh": "🔄 Qayta qidirish",
    },
    "ru": {
        "choose_lang": "🌐 Tilni tanlang / Выберите язык:",
        "welcome": (
            "👋 <b>Добро пожаловать в Kigo!</b>\n\n"
            "Я бот для поиска партнёра по спорту.\n"
            "Заполним ваш профиль за 2 минуты."
        ),
        "ask_name": "1/6 — <b>Как вас зовут?</b>\n\n<i>(2–30 символов)</i>",
        "invalid_name": "❌ Имя должно быть 2–30 символов. Введите снова:",
        "ask_age": "2/6 — <b>Выберите ваш возраст:</b>",
        "ask_sports": (
            "3/6 — <b>Какими видами спорта вы занимаетесь?</b>\n\n"
            "<i>Можно выбрать несколько. ✅ = выбрано.</i>"
        ),
        "min_sport": "⚠️ Выберите хотя бы 1 вид спорта!",
        "ask_level": "4/6 — Ваш уровень в <b>{sport}</b>:",
        "ask_city": (
            "5/6 — <b>Ваш город?</b>\n\n"
            "<i>Напишите название города или нажмите 📍 GPS.</i>"
        ),
        "ask_times": (
            "6/6 — <b>Когда удобно играть?</b>\n\n"
            "<i>Можно выбрать несколько. ✅ = выбрано.</i>"
        ),
        "min_time": "⚠️ Выберите хотя бы 1 время!",
        "profile_saved": (
            "✅ <b>Профиль сохранён!</b>\n\n"
            "/find — Найти партнёра\n"
            "/profile — Посмотреть профиль\n"
            "/invites — Приглашения"
        ),
        "profile_not_found": "❌ Профиль не найден. Отправьте /start",
        "your_profile": (
            "👤 <b>Ваш профиль</b>\n\n"
            "👤 Имя: <b>{name}</b>\n"
            "🎂 Возраст: <b>{age}</b>\n"
            "📍 Город: <b>{city}</b>\n"
            "⏰ Время: <b>{times}</b>\n"
            "⭐ Рейтинг: <b>{rating}</b> ({rating_count} оценок)\n\n"
            "<b>Виды спорта:</b>\n{sports}"
        ),
        "no_matches": (
            "😔 Пока подходящих партнёров не найдено.\n\n"
            "Попробуйте снова, когда появятся новые пользователи."
        ),
        "choose_sport_find": "🔍 По какому виду спорта ищете партнёра?",
        "matches_header": "🎯 <b>Найдено {count} подходящих партнёров!</b>\n\n",
        "match_item": "{num}. <b>{name}</b> — {city}\n   {sport} | {level} | {format}\n   ⏰ {times}\n   Совпадение: <b>{score}%</b>\n\n",
        "invite_sent": "✅ Приглашение отправлено! Сообщу, когда <b>{name}</b> примет.",
        "already_invited": "⚠️ Вы уже отправляли приглашение этому пользователю.",
        "invite_received": (
            "🏆 <b>Вам пришло приглашение!</b>\n\n"
            "👤 <b>{name}</b> ({city}) хочет сыграть с вами в {sport}.\n"
            "📊 Уровень: <b>{level}</b> | Формат: <b>{format}</b>"
        ),
        "invite_accepted_sender": (
            "🎉 <b>{name}</b> принял ваше приглашение!\n\n"
            "Напишите: @{username}"
        ),
        "invite_accepted_sender_no_username": (
            "🎉 <b>{name}</b> принял ваше приглашение!\n\n"
            "Username не указан, они свяжутся с вами сами."
        ),
        "invite_rejected_sender": "😔 <b>{name}</b> отклонил ваше приглашение.",
        "you_accepted": (
            "✅ Вы приняли приглашение!\n\n"
            "📱 Партнёр: @{username}"
        ),
        "you_accepted_no_username": "✅ Вы приняли приглашение! Партнёр свяжется с вами.",
        "you_rejected": "❌ Вы отклонили приглашение.",
        "no_invites": "📭 Пока нет входящих приглашений.",
        "invites_header": "📩 <b>Входящие приглашения:</b>\n\n",
        "invite_list_item": "{num}. <b>{name}</b> — {sport} ({level})\n",
        "rate_partner": "⭐ Как прошла игра с <b>{name}</b>? Поставьте оценку:",
        "rating_saved": "✅ Оценка сохранена! Спасибо.",
        "already_rated": "⚠️ Вы уже оценивали эту игру.",
        "help_text": (
            "📖 <b>Kigo Bot — Справка</b>\n\n"
            "/start — Начать или обновить профиль\n"
            "/find — Найти партнёра\n"
            "/profile — Посмотреть профиль\n"
            "/invites — Входящие приглашения\n"
            "/help — Эта справка\n\n"
            "<b>Алгоритм поиска:</b>\n"
            "• Один город: +40 очков\n"
            "• Одинаковый уровень: +30 очков\n"
            "• Подходящее время (каждое): +15 очков\n"
            "• Одинаковый формат: +10 очков\n"
            "• Возрастная группа: +5 очков"
        ),
        "profile_edit_prompt": "Что хотите изменить?",
        "send_gps": "📍 Отправить GPS",
        "skip_gps": "✏️ Ввести текст",
        "btn_done": "✅ Готово",
        "btn_invite": "📨 Пригласить",
        "btn_accept": "✅ Принять",
        "btn_reject": "❌ Отклонить",
        "btn_edit_profile": "✏️ Изменить профиль",
        "btn_refresh": "🔄 Обновить поиск",
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


def time_name(time: str, lang: str) -> str:
    return TIME_NAMES.get(lang, TIME_NAMES["uz"]).get(time, time)


def times_display(times: list, lang: str) -> str:
    return ", ".join(time_name(t_item, lang) for t_item in times)
