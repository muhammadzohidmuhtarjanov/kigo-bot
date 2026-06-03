import aiohttp
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import CommandStart

from db.queries import (
    create_or_update_user, delete_user_sports, save_user_sport, get_user,
    get_user_sports, get_pending_invites,
)
from utils.keyboards import (
    lang_kb, age_kb, sports_kb, level_kb, city_kb, times_kb, phone_kb,
    remove_kb, main_menu_kb, sport_select_kb, invite_action_kb, profile_kb,
)
from utils.texts import (
    t, SPORTS, sport_name, level_name, format_name, times_display,
)

router = Router()


class ProfileFSM(StatesGroup):
    name = State()
    age_group = State()
    sports = State()
    sport_level = State()
    city = State()
    times = State()
    phone = State()


# ── helpers ──────────────────────────────────────────────────────────────────

def _fmt_sports(sports: list, lang: str) -> str:
    if not sports:
        return "—"
    return "\n".join(
        f"• {sport_name(s['sport'], lang)} — {level_name(s['level'], lang)}"
        for s in sports
    )


async def _send_main_menu(target: Message, user: dict):
    """Send welcome_back + main menu. target must be a Message (or callback.message)."""
    lang = user["lang"]
    user_sports = await get_user_sports(user["id"])
    rating_str = f"{user['rating']:.1f}" if user["rating_count"] > 0 else "—"
    sports_line = "  ·  ".join(
        sport_name(s["sport"], lang) for s in user_sports
    ) if user_sports else "—"

    await target.answer(
        t(lang, "welcome_back",
          name=user["name"],
          city=user["city"],
          rating=rating_str,
          sports_line=sports_line),
        parse_mode="HTML",
        reply_markup=main_menu_kb(lang),
    )


# ── /start ───────────────────────────────────────────────────────────────────

@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    user = await get_user(message.from_user.id)

    if user:
        await _send_main_menu(message, user)
        return

    await message.answer(t("uz", "choose_lang"), reply_markup=lang_kb())


@router.callback_query(F.data.startswith("lang:"))
async def set_lang(callback: CallbackQuery, state: FSMContext):
    lang = callback.data.split(":")[1]
    current_state = await state.get_state()
    if current_state is not None and not current_state.startswith("ProfileFSM"):
        await callback.answer()
        return

    await state.update_data(lang=lang)
    await callback.message.edit_text(t(lang, "welcome"), parse_mode="HTML")
    await callback.message.answer(t(lang, "ask_name"), parse_mode="HTML")
    await state.set_state(ProfileFSM.name)
    await callback.answer()


@router.message(ProfileFSM.name)
async def get_name(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get("lang", "uz")
    name = (message.text or "").strip()

    if len(name) < 2 or len(name) > 30:
        await message.answer(t(lang, "invalid_name"))
        return

    await state.update_data(name=name)
    await message.answer(t(lang, "ask_age"), reply_markup=age_kb(lang))
    await state.set_state(ProfileFSM.age_group)


@router.callback_query(ProfileFSM.age_group, F.data.startswith("age:"))
async def get_age(callback: CallbackQuery, state: FSMContext):
    age_group = callback.data.split(":")[1]
    data = await state.get_data()
    lang = data.get("lang", "uz")

    await state.update_data(age_group=age_group, selected_sports=[])
    await callback.message.edit_text(
        t(lang, "ask_sports"), parse_mode="HTML",
        reply_markup=sports_kb(lang, []),
    )
    await state.set_state(ProfileFSM.sports)
    await callback.answer()


@router.callback_query(ProfileFSM.sports, F.data.startswith("toggle_sport:"))
async def toggle_sport(callback: CallbackQuery, state: FSMContext):
    sport = callback.data.split(":")[1]
    data = await state.get_data()
    lang = data.get("lang", "uz")

    selected = list(data.get("selected_sports", []))
    if sport in selected:
        selected.remove(sport)
    else:
        selected.append(sport)

    await state.update_data(selected_sports=selected)
    try:
        await callback.message.edit_reply_markup(reply_markup=sports_kb(lang, selected))
    except Exception:
        pass
    count = len(selected)
    if lang == "uz":
        await callback.answer(f"✅ {count} ta tanlandi" if count else "⬜ Bekor qilindi")
    else:
        await callback.answer(f"✅ Выбрано: {count}" if count else "⬜ Снято")


@router.callback_query(ProfileFSM.sports, F.data == "sports_done")
async def sports_done(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    lang = data.get("lang", "uz")
    selected = data.get("selected_sports", [])

    if not selected:
        await callback.answer(t(lang, "min_sport"), show_alert=True)
        return

    await state.update_data(sport_levels={}, current_sport_idx=0)
    sport = selected[0]
    await callback.message.edit_text(
        t(lang, "ask_level", sport=sport_name(sport, lang)),
        parse_mode="HTML",
        reply_markup=level_kb(lang, sport),
    )
    await state.set_state(ProfileFSM.sport_level)
    await callback.answer()


@router.callback_query(ProfileFSM.sport_level, F.data.startswith("level:"))
async def get_level(callback: CallbackQuery, state: FSMContext):
    _, sport, level = callback.data.split(":")
    data = await state.get_data()
    lang = data.get("lang", "uz")
    selected = data.get("selected_sports", [])

    sport_levels = dict(data.get("sport_levels", {}))
    sport_levels[sport] = level

    try:
        next_idx = selected.index(sport) + 1
    except ValueError:
        next_idx = len(selected)

    await state.update_data(sport_levels=sport_levels)

    if next_idx < len(selected):
        next_sport = selected[next_idx]
        await callback.message.edit_text(
            t(lang, "ask_level", sport=sport_name(next_sport, lang)),
            parse_mode="HTML",
            reply_markup=level_kb(lang, next_sport),
        )
    else:
        await callback.message.edit_text(t(lang, "ask_city"), parse_mode="HTML")
        await callback.message.answer("👇", reply_markup=city_kb(lang))
        await state.set_state(ProfileFSM.city)

    await callback.answer()


_IGNORE_TEXTS = {"👇", "📍 GPS yuborish", "📍 Отправить GPS"}

@router.message(ProfileFSM.city, F.text)
async def get_city_text(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get("lang", "uz")
    city = (message.text or "").strip()

    if not city or len(city) < 2 or city in _IGNORE_TEXTS:
        return

    await state.update_data(city=city, lat=None, lon=None)
    await message.answer(
        t(lang, "ask_times"), parse_mode="HTML",
        reply_markup=times_kb(lang, []),
    )
    await state.set_state(ProfileFSM.times)


@router.message(ProfileFSM.city, F.location)
async def get_city_gps(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get("lang", "uz")
    lat = message.location.latitude
    lon = message.location.longitude
    city = await _reverse_geocode(lat, lon)

    await state.update_data(city=city, lat=lat, lon=lon)
    await message.answer(
        t(lang, "ask_times"), parse_mode="HTML",
        reply_markup=times_kb(lang, []),
    )
    await state.set_state(ProfileFSM.times)


@router.callback_query(ProfileFSM.times, F.data.startswith("toggle_time:"))
async def toggle_time(callback: CallbackQuery, state: FSMContext):
    time = callback.data.split(":")[1]
    data = await state.get_data()
    lang = data.get("lang", "uz")

    selected = list(data.get("selected_times", []))
    if time in selected:
        selected.remove(time)
    else:
        selected.append(time)

    await state.update_data(selected_times=selected)
    try:
        await callback.message.edit_reply_markup(reply_markup=times_kb(lang, selected))
    except Exception:
        pass
    count = len(selected)
    if lang == "uz":
        await callback.answer(f"✅ {count} ta tanlandi" if count else "⬜ Bekor qilindi")
    else:
        await callback.answer(f"✅ Выбрано: {count}" if count else "⬜ Снято")


@router.callback_query(ProfileFSM.times, F.data == "times_done")
async def times_done(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    lang = data.get("lang", "uz")
    selected = data.get("selected_times", [])

    if not selected:
        await callback.answer(t(lang, "min_time"), show_alert=True)
        return

    await state.update_data(selected_times=selected)
    await callback.message.edit_text(t(lang, "ask_phone"), parse_mode="HTML")
    await callback.message.answer("👇", reply_markup=phone_kb(lang))
    await state.set_state(ProfileFSM.phone)
    await callback.answer()


@router.message(ProfileFSM.phone, F.contact)
async def get_phone_contact(message: Message, state: FSMContext):
    phone = message.contact.phone_number
    if not phone.startswith("+"):
        phone = "+" + phone
    await state.update_data(phone=phone)
    await _save_profile(message, state)


@router.message(ProfileFSM.phone, F.text)
async def get_phone_skip(message: Message, state: FSMContext):
    await state.update_data(phone=None)
    await _save_profile(message, state)


async def _save_profile(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get("lang", "uz")
    user_id = message.from_user.id
    username = message.from_user.username

    await create_or_update_user(
        user_id=user_id,
        username=username,
        name=data["name"],
        age_group=data["age_group"],
        city=data["city"],
        lat=data.get("lat"),
        lon=data.get("lon"),
        available_times=data.get("selected_times", []),
        lang=lang,
        phone=data.get("phone"),
    )

    await delete_user_sports(user_id)
    for sport, level in data.get("sport_levels", {}).items():
        await save_user_sport(user_id, sport, level)

    await message.answer(
        t(lang, "profile_saved"),
        parse_mode="HTML",
        reply_markup=remove_kb(),
    )

    user = await get_user(user_id)
    if user:
        await _send_main_menu(message, user)

    await state.clear()


# ── main menu callbacks ───────────────────────────────────────────────────────

@router.callback_query(F.data == "menu:find")
async def menu_find(callback: CallbackQuery):
    user_id = callback.from_user.id
    user = await get_user(user_id)
    if not user:
        await callback.answer()
        return
    lang = user["lang"]
    user_sports = await get_user_sports(user_id)
    if not user_sports:
        await callback.message.answer(t(lang, "profile_not_found"), parse_mode="HTML")
        await callback.answer()
        return
    await callback.message.answer(
        t(lang, "choose_sport_find"),
        parse_mode="HTML",
        reply_markup=sport_select_kb(lang, user_sports),
    )
    await callback.answer()


@router.callback_query(F.data == "menu:profile")
async def menu_profile(callback: CallbackQuery):
    user_id = callback.from_user.id
    user = await get_user(user_id)
    if not user:
        await callback.answer()
        return
    lang = user["lang"]
    user_sports = await get_user_sports(user_id)
    rating_str = f"{user['rating']:.1f}" if user["rating_count"] > 0 else "—"
    phone = user.get("phone") or "—"
    times = times_display(user["available_times"] or [], lang)
    await callback.message.answer(
        t(lang, "your_profile",
          name=user["name"],
          age=user["age_group"],
          city=user["city"],
          phone=phone,
          times=times,
          rating=rating_str,
          rating_count=user["rating_count"],
          sports=_fmt_sports(user_sports, lang)),
        parse_mode="HTML",
        reply_markup=profile_kb(lang),
    )
    await callback.answer()


@router.callback_query(F.data == "menu:invites")
async def menu_invites(callback: CallbackQuery):
    user_id = callback.from_user.id
    user = await get_user(user_id)
    if not user:
        await callback.answer()
        return
    lang = user["lang"]
    invites = await get_pending_invites(user_id)
    if not invites:
        await callback.message.answer(t(lang, "no_invites"), parse_mode="HTML")
        await callback.answer()
        return
    for inv in invites:
        await callback.message.answer(
            t(lang, "invite_received",
              name=inv["from_name"],
              city=inv["from_city"],
              sport=sport_name(inv["sport"], lang),
              level=level_name(inv.get("from_level") or "beginner", lang),
              format=format_name(inv.get("from_format") or "any", lang)),
            parse_mode="HTML",
            reply_markup=invite_action_kb(lang, inv["id"]),
        )
    await callback.answer()


@router.callback_query(F.data == "menu:help")
async def menu_help(callback: CallbackQuery):
    user_id = callback.from_user.id
    user = await get_user(user_id)
    lang = user["lang"] if user else "uz"
    await callback.message.answer(t(lang, "help_text"), parse_mode="HTML")
    await callback.answer()


@router.callback_query(F.data == "menu:update")
async def menu_update(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.answer(t("uz", "choose_lang"), reply_markup=lang_kb())
    await callback.answer()


# ── reverse geocode ───────────────────────────────────────────────────────────

async def _reverse_geocode(lat: float, lon: float) -> str:
    try:
        url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json"
        headers = {"User-Agent": "KigoBot/1.0 (sport partner bot)"}
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, timeout=aiohttp.ClientTimeout(total=5)) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    addr = data.get("address", {})
                    city = (
                        addr.get("city")
                        or addr.get("town")
                        or addr.get("village")
                        or addr.get("county")
                        or addr.get("state")
                    )
                    if city:
                        return city
    except Exception:
        pass
    return f"{lat:.4f},{lon:.4f}"
