"""SQLite backend via aiosqlite — works on any Python version, no C extensions needed."""
import re
import aiosqlite
from config import settings

_db: "aiosqlite.Connection | None" = None
_USE_PG = False  # kept for models.py compatibility


def _pg2lite(sql: str) -> str:
    return re.sub(r"\$\d+", "?", sql)


async def _get_db() -> aiosqlite.Connection:
    global _db
    if _db is None:
        _db = await aiosqlite.connect(settings.DB_PATH)
        _db.row_factory = aiosqlite.Row
        await _db.execute("PRAGMA journal_mode=WAL")
        await _db.execute("PRAGMA foreign_keys=ON")
    return _db


async def close_db():
    global _db
    if _db:
        await _db.close()
        _db = None


async def fetchrow(sql: str, *args):
    db = await _get_db()
    async with db.execute(_pg2lite(sql), args) as cur:
        row = await cur.fetchone()
        return dict(row) if row else None


async def fetch(sql: str, *args) -> list[dict]:
    db = await _get_db()
    async with db.execute(_pg2lite(sql), args) as cur:
        return [dict(r) for r in await cur.fetchall()]


async def execute(sql: str, *args):
    db = await _get_db()
    await db.execute(_pg2lite(sql), args)
    await db.commit()


async def executemany(sql: str, args_list: list):
    db = await _get_db()
    await db.executemany(_pg2lite(sql), args_list)
    await db.commit()
