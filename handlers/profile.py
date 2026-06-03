from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from db.queries import get_user, get_user_sports
from utils.keyboards import profile_kb
from utils.texts import t, sport_name, level_name, format_name, times_display

router = Router()


@router.message(Command("profile"))
async def cmd_profile(message: Message):
    user_id = message.from_user.id
    user = await get_user(user_id)

    if not user:
        await message.answer(t("uz", "profile_not_found"))
        return

    lang = user["lang"]
    sports = await get_user_sports(user_id)
    sports_text = _format_sports(sports, lang)
    rating_str = f"{user['rating']:.1f}" if user["rating_count"] > 0 else "—"

    await message.answer(
        t(lang, "your_profile",
          name=user["name"],
          age=user["age_group"],
          city=user["city"],
          times=times_display(user["available_times"] or [], lang),
          rating=rating_str,
          rating_count=user["rating_count"],
          sports=sports_text),
        parse_mode="HTML",
        reply_markup=profile_kb(lang),
    )


@router.callback_query(F.data == "edit_profile")
async def edit_profile(callback: CallbackQuery):
    await callback.message.answer("/start buyrug'ini yuboring profilni yangilash uchun.\n\nОтправьте /start чтобы обновить профиль.")
    await callback.answer()


def _format_sports(sports: list, lang: str) -> str:
    if not sports:
        return "—"
    lines = []
    for s in sports:
        lines.append(
            f"• {sport_name(s['sport'], lang)} — "
            f"{level_name(s['level'], lang)} | "
            f"{format_name(s.get('format', 'any'), lang)}"
        )
    return "\n".join(lines)
