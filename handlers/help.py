from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from db.queries import get_user_lang
from utils.texts import t

router = Router()


@router.message(Command("help"))
async def cmd_help(message: Message):
    lang = await get_user_lang(message.from_user.id)
    await message.answer(t(lang, "help_text"), parse_mode="HTML")
