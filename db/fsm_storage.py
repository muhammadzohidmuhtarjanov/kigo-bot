import json
from typing import Optional, Dict, Any
from aiogram.fsm.storage.base import BaseStorage, StorageKey, StateType

import db


class SQLiteStorage(BaseStorage):
    """Persistent FSM storage backed by SQLite — survives bot restarts."""

    async def set_state(self, key: StorageKey, state: StateType = None) -> None:
        state_str = state.state if hasattr(state, "state") else state
        await db.execute(
            """
            INSERT INTO fsm_state (bot_id, chat_id, user_id, destiny, state)
            VALUES ($1, $2, $3, $4, $5)
            ON CONFLICT(bot_id, chat_id, user_id, destiny)
            DO UPDATE SET state = EXCLUDED.state
            """,
            key.bot_id, key.chat_id, key.user_id, key.destiny, state_str,
        )

    async def get_state(self, key: StorageKey) -> Optional[str]:
        row = await db.fetchrow(
            "SELECT state FROM fsm_state "
            "WHERE bot_id=$1 AND chat_id=$2 AND user_id=$3 AND destiny=$4",
            key.bot_id, key.chat_id, key.user_id, key.destiny,
        )
        return row["state"] if row else None

    async def set_data(self, key: StorageKey, data: Dict[str, Any]) -> None:
        await db.execute(
            """
            INSERT INTO fsm_state (bot_id, chat_id, user_id, destiny, data)
            VALUES ($1, $2, $3, $4, $5)
            ON CONFLICT(bot_id, chat_id, user_id, destiny)
            DO UPDATE SET data = EXCLUDED.data
            """,
            key.bot_id, key.chat_id, key.user_id, key.destiny, json.dumps(data),
        )

    async def get_data(self, key: StorageKey) -> Dict[str, Any]:
        row = await db.fetchrow(
            "SELECT data FROM fsm_state "
            "WHERE bot_id=$1 AND chat_id=$2 AND user_id=$3 AND destiny=$4",
            key.bot_id, key.chat_id, key.user_id, key.destiny,
        )
        if row and row["data"]:
            try:
                return json.loads(row["data"])
            except Exception:
                return {}
        return {}

    async def close(self) -> None:
        pass
