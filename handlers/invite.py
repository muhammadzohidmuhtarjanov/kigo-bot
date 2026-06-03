from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from db.queries import (
    get_user, get_pending_invites, get_invite,
    update_invite_status, save_rating,
)
from utils.keyboards import invite_action_kb, rate_kb
from utils.texts import t, sport_name, level_name, format_name


def _contact_text(lang: str, prefix: str, partner: dict) -> str:
    """Build accept notification with whatever contact info the partner shared."""
    phone = partner.get("phone")
    username = partner.get("username")
    name = partner["name"]

    if phone and username:
        return t(lang, prefix, name=name, phone=phone, username=username)
    elif phone:
        return t(lang, f"{prefix}_phone_only", name=name, phone=phone)
    elif username:
        return t(lang, f"{prefix}_username_only", name=name, username=username)
    else:
        return t(lang, f"{prefix}_no_contact", name=name)

router = Router()


@router.message(Command("invites"))
async def cmd_invites(message: Message):
    user_id = message.from_user.id
    user = await get_user(user_id)

    if not user:
        await message.answer(t("uz", "profile_not_found"))
        return

    lang = user["lang"]
    invites = await get_pending_invites(user_id)

    if not invites:
        await message.answer(t(lang, "no_invites"))
        return

    text = t(lang, "invites_header")
    for i, inv in enumerate(invites, 1):
        text += t(lang, "invite_list_item",
                  num=i,
                  name=inv["from_name"],
                  sport=sport_name(inv["sport"], lang),
                  level=level_name(inv.get("from_level") or "beginner", lang))
        text += f"   <i>#{inv['id']}</i>\n\n"

    text += "\n" + ("Qabul/rad qilish uchun tugmalardan foydalaning." if lang == "uz" else "Используйте кнопки для принятия/отклонения.")

    for inv in invites:
        inv_lang = lang
        await message.answer(
            t(inv_lang, "invite_received",
              name=inv["from_name"],
              city=inv["from_city"],
              sport=sport_name(inv["sport"], inv_lang),
              level=level_name(inv.get("from_level") or "beginner", inv_lang),
              format=format_name(inv.get("from_format") or "any", inv_lang)),
            parse_mode="HTML",
            reply_markup=invite_action_kb(inv_lang, inv["id"]),
        )


@router.callback_query(F.data.startswith("inv_accept:"))
async def accept_invite(callback: CallbackQuery):
    invite_id = int(callback.data.split(":")[1])
    invite = await get_invite(invite_id)

    if not invite or invite["status"] != "pending":
        await callback.answer()
        return

    if invite["to_user_id"] != callback.from_user.id:
        await callback.answer()
        return

    await update_invite_status(invite_id, "accepted")

    acceptor = await get_user(invite["to_user_id"])
    sender = await get_user(invite["from_user_id"])

    if not acceptor or not sender:
        await callback.answer()
        return

    acceptor_lang = acceptor["lang"]
    sender_lang = sender["lang"]

    # acceptor ni sender ga yuborish
    await callback.message.edit_text(
        _contact_text(sender_lang, "you_accepted", sender),
        parse_mode="HTML",
    )

    # sender ni acceptor ga yuborish
    await callback.bot.send_message(
        chat_id=invite["from_user_id"],
        text=_contact_text(acceptor_lang, "invite_accepted_sender", acceptor),
        parse_mode="HTML",
    )

    await _send_rating_request(callback.bot, acceptor, sender, invite_id, sender_lang)
    await _send_rating_request(callback.bot, sender, acceptor, invite_id, acceptor_lang)

    await callback.answer()


@router.callback_query(F.data.startswith("inv_reject:"))
async def reject_invite(callback: CallbackQuery):
    invite_id = int(callback.data.split(":")[1])
    invite = await get_invite(invite_id)

    if not invite or invite["status"] != "pending":
        await callback.answer()
        return

    if invite["to_user_id"] != callback.from_user.id:
        await callback.answer()
        return

    await update_invite_status(invite_id, "rejected")

    rejector = await get_user(invite["to_user_id"])
    sender = await get_user(invite["from_user_id"])

    if rejector:
        await callback.message.edit_text(
            t(rejector["lang"], "you_rejected"), parse_mode="HTML"
        )

    if sender and rejector:
        await callback.bot.send_message(
            chat_id=invite["from_user_id"],
            text=t(sender["lang"], "invite_rejected_sender", name=rejector["name"]),
            parse_mode="HTML",
        )

    await callback.answer()


@router.callback_query(F.data.startswith("rate:"))
async def rate_partner(callback: CallbackQuery):
    parts = callback.data.split(":")
    invite_id = int(parts[1])
    to_user_id = int(parts[2])
    stars = int(parts[3])

    from_user_id = callback.from_user.id
    from_user = await get_user(from_user_id)
    to_user = await get_user(to_user_id)

    if not from_user or not to_user:
        await callback.answer()
        return

    lang = from_user["lang"]

    await save_rating(from_user_id, to_user_id, invite_id, stars)
    await callback.message.edit_text(t(lang, "rating_saved"), parse_mode="HTML")
    await callback.answer()


async def _send_rating_request(bot, rater: dict, ratee: dict, invite_id: int, lang: str):
    await bot.send_message(
        chat_id=rater["id"],
        text=t(lang, "rate_partner", name=ratee["name"]),
        parse_mode="HTML",
        reply_markup=rate_kb(lang, invite_id, ratee["id"]),
    )
