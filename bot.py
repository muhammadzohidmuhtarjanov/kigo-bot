import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import settings
from db import close_db
from db.models import init_db
from handlers import start, profile, find, invite, help as help_handler

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
log = logging.getLogger(__name__)


async def main():
    log.info("Initialising database...")
    await init_db()

    bot = Bot(
        token=settings.BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(start.router)
    dp.include_router(profile.router)
    dp.include_router(find.router)
    dp.include_router(invite.router)
    dp.include_router(help_handler.router)

    # catch-all: stale inline buttons after bot restart
    from aiogram import F as AF
    from aiogram.types import CallbackQuery as CQ

    @dp.callback_query()
    async def _stale_callback(cb: CQ):
        await cb.answer(
            "⚠️ Session eskirdi. /start yuboring. | Сессия устарела. Отправьте /start",
            show_alert=True,
        )

    log.info("Bot started.")
    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await close_db()
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
