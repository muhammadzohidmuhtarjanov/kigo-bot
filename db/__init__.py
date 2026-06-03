"""
Auto-selects backend:
  DATABASE_URL set  →  asyncpg (PostgreSQL, Railway)
  DATABASE_URL not set  →  aiosqlite (SQLite, local)
"""
import os
import re

_USE_PG: bool = bool(os.getenv("DATABASE_URL"))

# ── PostgreSQL (asyncpg) ──────────────────────────────────────────────────────
if _USE_PG:
    import asyncpg

    _pool: "asyncpg.Pool | None" = None

    async def _get_pool() -> "asyncpg.Pool":
        global _pool
        if _pool is None:
            _pool = await asyncpg.create_pool(os.environ["DATABASE_URL"])
        return _pool

    async def close_db():
        global _pool
        if _pool:
            await _pool.close()
            _pool = None

    async def fetchrow(sql: str, *args):
        pool = await _get_pool()
        async with pool.acquire() as conn:
            row = await conn.fetchrow(sql, *args)
            return dict(row) if row else None

    async def fetch(sql: str, *args) -> list[dict]:
        pool = await _get_pool()
        async with pool.acquire() as conn:
            rows = await conn.fetch(sql, *args)
            return [dict(r) for r in rows]

    async def execute(sql: str, *args):
        pool = await _get_pool()
        async with pool.acquire() as conn:
            await conn.execute(sql, *args)

    async def executemany(sql: str, args_list: list):
        pool = await _get_pool()
        async with pool.acquire() as conn:
            await conn.executemany(sql, args_list)

# ── SQLite (aiosqlite) ────────────────────────────────────────────────────────
else:
    import aiosqlite
    from config import settings

    _db: "aiosqlite.Connection | None" = None

    def _pg2lite(sql: str) -> str:
        """Replace $1, $2 … with ? for SQLite."""
        return re.sub(r"\$\d+", "?", sql)

    async def _get_db() -> "aiosqlite.Connection":
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
