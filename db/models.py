import db

_SQL = """
CREATE TABLE IF NOT EXISTS users (
    id              INTEGER PRIMARY KEY,
    username        TEXT,
    phone           TEXT,
    name            TEXT    NOT NULL,
    age_group       TEXT    NOT NULL,
    city            TEXT    NOT NULL,
    lat             REAL,
    lon             REAL,
    available_times TEXT    DEFAULT '[]',
    lang            TEXT    DEFAULT 'uz',
    rating          REAL    DEFAULT 0,
    rating_count    INTEGER DEFAULT 0,
    is_active       INTEGER DEFAULT 1,
    created_at      TEXT    DEFAULT (datetime('now')),
    updated_at      TEXT    DEFAULT (datetime('now'))
);
CREATE TABLE IF NOT EXISTS user_sports (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    sport   TEXT NOT NULL,
    level   TEXT NOT NULL,
    format  TEXT DEFAULT 'any',
    UNIQUE(user_id, sport)
);
CREATE TABLE IF NOT EXISTS invites (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    from_user_id INTEGER REFERENCES users(id),
    to_user_id   INTEGER REFERENCES users(id),
    sport        TEXT NOT NULL,
    status       TEXT DEFAULT 'pending',
    created_at   TEXT DEFAULT (datetime('now')),
    updated_at   TEXT DEFAULT (datetime('now'))
);
CREATE TABLE IF NOT EXISTS game_ratings (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    from_user_id INTEGER REFERENCES users(id),
    to_user_id   INTEGER REFERENCES users(id),
    invite_id    INTEGER REFERENCES invites(id),
    stars        INTEGER CHECK (stars BETWEEN 1 AND 5),
    comment      TEXT,
    created_at   TEXT DEFAULT (datetime('now')),
    UNIQUE(from_user_id, invite_id)
);
"""


async def init_db():
    conn = await db._get_db()
    await conn.executescript(_SQL)
    await conn.commit()
