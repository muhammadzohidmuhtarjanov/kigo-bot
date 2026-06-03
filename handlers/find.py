from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from db.queries import get_user, get_user_sports, get_candidates, create_invite
from utils.keyboards import sport_select_kb, matches_list_kb
from utils.matching import rank_candidates
from utils.texts import t, sport_name, times_display

router = Router()


@router.message(Command("find"))
async def cmd_find(message: Message):
    user_id = message.from_user.id
    user = await get_user(user_id)

    if not user:
        await message.answer(t("uz", "profile_not_found"))
        return

    lang = user["lang"]
    sports = await get_user_sports(user_id)

    if not sports:
        await message.answer(t(lang, "profile_not_found"))
        return

    if len(sports) == 1:
        await _do_search(message, user, sports[0], lang)
    else:
        await message.answer(
            t(lang, "choose_sport_find"),
            reply_markup=sport_select_kb(lang, sports),
        )


@router.callback_query(F.data.startswith("find_sport:"))
async def find_sport_selected(callback: CallbackQuery):
    sport_key = callback.data.split(":")[1]
    user_id = callback.from_user.id
    user = await get_user(user_id)

    if not user:
        await callback.answer()
        return

    lang = user["lang"]
    sports = await get_user_sports(user_id)
    sport_record = next((s for s in sports if s["sport"] == sport_key), None)

    if not sport_record:
        await callback.answer()
        return

    await callback.message.edit_text("🔍 Qidirilmoqda... / Ищем...")
    await _do_search(callback.message, user, sport_record, lang, edit=True)
    await callback.answer()


@router.callback_query(F.data.startswith("find_refresh:"))
async def find_refresh(callback: CallbackQuery):
    sport_key = callback.data.split(":")[1]
    user_id = callback.from_user.id
    user = await get_user(user_id)

    if not user:
        await callback.answer()
        return

    lang = user["lang"]
    sports = await get_user_sports(user_id)
    sport_record = next((s for s in sports if s["sport"] == sport_key), None)

    if sport_record:
        await callback.message.edit_text("🔍 Qidirilmoqda... / Ищем...")
        await _do_search(callback.message, user, sport_record, lang, edit=True)

    await callback.answer()


@router.callback_query(F.data.startswith("invite:"))
async def send_invite(callback: CallbackQuery):
    parts = callback.data.split(":")
    to_user_id = int(parts[1])
    sport = parts[2]
    from_user_id = callback.from_user.id

    if to_user_id == from_user_id:
        await callback.answer("⚠️", show_alert=True)
        return

    from_user = await get_user(from_user_id)
    to_user = await get_user(to_user_id)

    if not from_user or not to_user:
        await callback.answer()
        return

    lang = from_user["lang"]
    invite = await create_invite(from_user_id, to_user_id, sport)

    if invite is None:
        await callback.answer(t(lang, "already_invited"), show_alert=True)
        return

    await callback.answer(t(lang, "invite_sent", name=to_user["name"]), show_alert=True)

    from db.queries import get_user_sports as gus
    to_lang = to_user["lang"]
    from_sports = await gus(from_user_id)
    sport_record = next((s for s in from_sports if s["sport"] == sport), None)

    from utils.keyboards import invite_action_kb
    from utils.texts import sport_name, level_name, format_name

    await callback.bot.send_message(
        chat_id=to_user_id,
        text=t(to_lang, "invite_received",
               name=from_user["name"],
               city=from_user["city"],
               sport=sport_name(sport, to_lang),
               level=level_name(sport_record["level"] if sport_record else "?", to_lang),
               format=format_name(sport_record.get("format", "any") if sport_record else "any", to_lang)),
        parse_mode="HTML",
        reply_markup=invite_action_kb(to_lang, invite["id"]),
    )


async def _do_search(message, user: dict, sport_record: dict, lang: str, edit: bool = False):
    user_id = user["id"]
    sport = sport_record["sport"]

    candidates_raw = await get_candidates(user_id, sport)
    if not candidates_raw:
        text = t(lang, "no_matches")
        if edit:
            await message.edit_text(text, parse_mode="HTML")
        else:
            await message.answer(text, parse_mode="HTML")
        return

    ranked = rank_candidates(user, sport_record, candidates_raw, lang)
    top = ranked[:10]

    header = t(lang, "matches_header", count=len(ranked))
    lines = []
    for i, c in enumerate(top, 1):
        lines.append(t(lang, "match_item",
                       num=i,
                       name=c["name"],
                       city=c["city"],
                       sport=c["sport_display"],
                       level=c["level_display"],
                       format=c["format_display"],
                       times=c["times_display"],
                       score=c["score"]))

    text = header + "".join(lines)
    kb = matches_list_kb(lang, top, sport)

    if edit:
        await message.edit_text(text, parse_mode="HTML", reply_markup=kb)
    else:
        await message.answer(text, parse_mode="HTML", reply_markup=kb)
