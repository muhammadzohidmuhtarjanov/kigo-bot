import json
from typing import Optional
import db


def _dec(row: Optional[dict]) -> Optional[dict]:
    if row and "available_times" in row:
        val = row["available_times"]
        if isinstance(val, str):
            try:
                row["available_times"] = json.loads(val)
            except Exception:
                row["available_times"] = []
    return row


async def get_user(user_id: int) -> Optional[dict]:
    return _dec(await db.fetchrow("SELECT * FROM users WHERE id = $1", user_id))


async def create_or_update_user(
    user_id: int,
    username: Optional[str],
    name: str,
    age_group: str,
    city: str,
    lat: Optional[float],
    lon: Optional[float],
    available_times: list,
    lang: str,
) -> dict:
    times_json = json.dumps(available_times)
    await db.execute(
        """
        INSERT INTO users (id, username, name, age_group, city, lat, lon, available_times, lang)
        VALUES ($1,$2,$3,$4,$5,$6,$7,$8,$9)
        ON CONFLICT(id) DO UPDATE SET
            username        = EXCLUDED.username,
            name            = EXCLUDED.name,
            age_group       = EXCLUDED.age_group,
            city            = EXCLUDED.city,
            lat             = EXCLUDED.lat,
            lon             = EXCLUDED.lon,
            available_times = EXCLUDED.available_times,
            lang            = EXCLUDED.lang,
            updated_at      = CURRENT_TIMESTAMP
        """,
        user_id, username, name, age_group, city, lat, lon, times_json, lang,
    )
    return await get_user(user_id)


async def get_user_sports(user_id: int) -> list[dict]:
    return await db.fetch("SELECT * FROM user_sports WHERE user_id = $1", user_id)


async def delete_user_sports(user_id: int):
    await db.execute("DELETE FROM user_sports WHERE user_id = $1", user_id)


async def save_user_sport(user_id: int, sport: str, level: str, format: str = "any"):
    await db.execute(
        """
        INSERT INTO user_sports (user_id, sport, level, format)
        VALUES ($1,$2,$3,$4)
        ON CONFLICT(user_id, sport) DO UPDATE SET
            level  = EXCLUDED.level,
            format = EXCLUDED.format
        """,
        user_id, sport, level, format,
    )


async def get_candidates(user_id: int, sport: str) -> list[dict]:
    rows = await db.fetch(
        """
        SELECT u.*, us.sport AS us_sport, us.level AS us_level, us.format AS us_format
        FROM users u
        JOIN user_sports us ON u.id = us.user_id
        WHERE us.sport = $1 AND u.id != $2 AND u.is_active = 1
        """,
        sport, user_id,
    )
    for r in rows:
        _dec(r)
    return rows


async def get_user_lang(user_id: int) -> str:
    row = await db.fetchrow("SELECT lang FROM users WHERE id = $1", user_id)
    return row["lang"] if row else "uz"


async def create_invite(from_user_id: int, to_user_id: int, sport: str) -> Optional[dict]:
    existing = await db.fetchrow(
        "SELECT id FROM invites WHERE from_user_id=$1 AND to_user_id=$2 AND sport=$3 AND status='pending'",
        from_user_id, to_user_id, sport,
    )
    if existing:
        return None
    await db.execute(
        "INSERT INTO invites (from_user_id, to_user_id, sport) VALUES ($1,$2,$3)",
        from_user_id, to_user_id, sport,
    )
    return await db.fetchrow(
        "SELECT * FROM invites WHERE from_user_id=$1 AND to_user_id=$2 AND sport=$3 ORDER BY id DESC LIMIT 1",
        from_user_id, to_user_id, sport,
    )


async def get_invite(invite_id: int) -> Optional[dict]:
    return await db.fetchrow("SELECT * FROM invites WHERE id = $1", invite_id)


async def update_invite_status(invite_id: int, status: str):
    await db.execute(
        "UPDATE invites SET status=$1, updated_at=CURRENT_TIMESTAMP WHERE id=$2",
        status, invite_id,
    )


async def get_pending_invites(user_id: int) -> list[dict]:
    return await db.fetch(
        """
        SELECT i.*, u.name AS from_name, u.username AS from_username,
               u.city AS from_city, u.age_group AS from_age_group,
               us.level AS from_level, us.format AS from_format
        FROM invites i
        JOIN users u ON u.id = i.from_user_id
        LEFT JOIN user_sports us ON us.user_id = i.from_user_id AND us.sport = i.sport
        WHERE i.to_user_id = $1 AND i.status = 'pending'
        ORDER BY i.created_at DESC
        """,
        user_id,
    )


async def save_rating(from_user_id: int, to_user_id: int, invite_id: int, stars: int, comment: Optional[str] = None):
    await db.execute(
        """
        INSERT INTO game_ratings (from_user_id, to_user_id, invite_id, stars, comment)
        VALUES ($1,$2,$3,$4,$5)
        ON CONFLICT(from_user_id, invite_id) DO UPDATE SET
            stars   = EXCLUDED.stars,
            comment = EXCLUDED.comment
        """,
        from_user_id, to_user_id, invite_id, stars, comment,
    )
    await db.execute(
        """
        UPDATE users SET
            rating       = (SELECT AVG(stars)  FROM game_ratings WHERE to_user_id = $1),
            rating_count = (SELECT COUNT(*)    FROM game_ratings WHERE to_user_id = $1)
        WHERE id = $1
        """,
        to_user_id,
    )
