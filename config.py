from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BOT_TOKEN: str
    DB_PATH: str = "kigo.db"

    model_config = {"env_file": ".env"}


settings = Settings()
