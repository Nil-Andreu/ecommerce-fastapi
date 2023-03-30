from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = 'fastapi-ecommerce'
    APP_DESCRIPTION: str = 'Ecommerce developed with FastAPI'
    APP_VERSION: float = 1.0


def get_settings():
    return Settings()