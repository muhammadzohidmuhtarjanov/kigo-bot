from aiogram.types import (
    InlineKeyboardMarkup, InlineKeyboardButton,
    ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from utils.texts import SPORTS, LEVELS, FORMATS, TIMES, AGE_GROUPS
from utils.texts import sport_name, level_name, format_name, time_name, t


def lang_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="🇺🇿 O'zbek", callback_data="lang:uz")
    builder.button(text="🇷🇺 Русский", callback_data="lang:ru")
    builder.adjust(2)
    return builder.as_markup()


def age_kb(lang: str) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for group in AGE_GROUPS:
        builder.button(text=group, callback_data=f"age:{group}")
    builder.adjust(2)
    return builder.as_markup()


def sports_kb(lang: str, selected: list) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for sport in SPORTS:
        mark = "✅ " if sport in selected else "⬜ "
        builder.button(
            text=mark + sport_name(sport, lang),
            callback_data=f"toggle_sport:{sport}",
        )
    builder.button(text=t(lang, "btn_done"), callback_data="sports_done")
    builder.adjust(2, 2, 2, 2, 1)
    return builder.as_markup()


def level_kb(lang: str, sport: str) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for lvl in LEVELS:
        builder.button(
            text=level_name(lvl, lang),
            callback_data=f"level:{sport}:{lvl}",
        )
    builder.adjust(3)
    return builder.as_markup()


def city_kb(lang: str) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=t(lang, "send_gps"), request_location=True)]],
        resize_keyboard=True,
        one_time_keyboard=True,
    )


def times_kb(lang: str, selected: list) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for time in TIMES:
        mark = "✅ " if time in selected else "⬜ "
        builder.button(
            text=mark + time_name(time, lang),
            callback_data=f"toggle_time:{time}",
        )
    builder.button(text=t(lang, "btn_done"), callback_data="times_done")
    builder.adjust(2, 2, 1)
    return builder.as_markup()


def match_kb(lang: str, to_user_id: int, sport: str) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text=t(lang, "btn_invite"),
        callback_data=f"invite:{to_user_id}:{sport}",
    )
    return builder.as_markup()


def matches_list_kb(lang: str, candidates: list, sport: str) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for c in candidates:
        builder.button(
            text=f"📨 {c['name']} ({c['score']}%)",
            callback_data=f"invite:{c['id']}:{sport}",
        )
    builder.button(text=t(lang, "btn_refresh"), callback_data=f"find_refresh:{sport}")
    builder.adjust(1)
    return builder.as_markup()


def invite_action_kb(lang: str, invite_id: int) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text=t(lang, "btn_accept"), callback_data=f"inv_accept:{invite_id}")
    builder.button(text=t(lang, "btn_reject"), callback_data=f"inv_reject:{invite_id}")
    builder.adjust(2)
    return builder.as_markup()


def rate_kb(lang: str, invite_id: int, to_user_id: int) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    stars_map = {"1": "⭐", "2": "⭐⭐", "3": "⭐⭐⭐", "4": "⭐⭐⭐⭐", "5": "⭐⭐⭐⭐⭐"}
    for s, label in stars_map.items():
        builder.button(text=label, callback_data=f"rate:{invite_id}:{to_user_id}:{s}")
    builder.adjust(5)
    return builder.as_markup()


def sport_select_kb(lang: str, user_sports: list) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for us in user_sports:
        builder.button(
            text=sport_name(us["sport"], lang),
            callback_data=f"find_sport:{us['sport']}",
        )
    builder.adjust(2)
    return builder.as_markup()


def profile_kb(lang: str) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text=t(lang, "btn_edit_profile"), callback_data="edit_profile")
    return builder.as_markup()


def remove_kb() -> ReplyKeyboardRemove:
    return ReplyKeyboardRemove()
