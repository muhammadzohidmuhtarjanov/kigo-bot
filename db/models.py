"""
Works for both PostgreSQL and SQLite — uses CURRENT_TIMESTAMP and TEXT arrays
stored as JSON strings (decoded transparently in queries.py).
"""
import db

_PG_SQL = """
CREATE TABLE IF NOT EXISTS users (
    id              BIGINT PRIMARY KEY,
    username        VARCHAR(64),
    name            VARCHAR(30)  NOT NULL,
    age_group       VARCHAR(10)  NOT NULL,
    city            VARCHAR(100) NOT NULL,
    lat             FLOAT,
    lon             FLOAT,
    available_times TEXT         DEFAULT '[]',
    lang            VARCHAR(5)   DEFAULT 'uz',
    rating          FLOAT        DEFAULT 0,
    rating_count    INTEGER      DEFAULT 0,
    is_active       INTEGER      DEFAULT 1,
    created_at      TIMESTAMP    DEFAULT CURRENT_TIMESTAMP,
    updated_at      TIMESTAMP    DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS user_sports (
    id       SERIAL PRIMARY KEY,
    user_id  BIGINT REFERENCES users(id) ON DELETE CASCADE,
    sport    VARCHAR(30) NOT NULL,
    level    VARCHAR(10) NOT NULL,
    format   VARCHAR(10) DEFAULT 'any',
    UNIQUE(user_id, sport)
);
CREATE TABLE IF NOT EXISTS invites (
    id           SERIAL PRIMARY KEY,
    from_user_id BIGINT REFERENCES users(id),
    to_user_id   BIGINT REFERENCES users(id),
    sport        VARCHAR(30) NOT NULL,
    status       VARCHAR(10) DEFAULT 'pending',
    created_at   TIMESTAMP   DEFAULT CURRENT_TIMESTAMP,
    updated_at   TIMESTAMP   DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS game_ratings (
    id           SERIAL PRIMARY KEY,
    from_user_id BIGINT REFERENCES users(id),
    to_user_id   BIGINT REFERENCES users(id),
    invite_id    INTEGER REFERENCES invites(id),
    stars        INTEGER CHECK (stars BETWEEN 1 AND 5),
    comment      TEXT,
    created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(from_user_id, invite_id)
);
"""

_LITE_SQL = _PG_SQL.replace("BIGINT", "INTEGER").replace("SERIAL", "INTEGER").replace(
    "SERIAL PRIMARY KEY", "INTEGER PRIMARY KEY AUTOINCREMENT"
)


async def init_db():
    if db._USE_PG:
        import asyncpg, os
        pool = await db._get_pool()
        async with pool.acquire() as conn:
            await conn.execute(_PG_SQL)
    else:
        import aiosqlite
        conn = await db._get_db()
        await conn.executescript(_LITE_SQL)
        await conn.commit()
