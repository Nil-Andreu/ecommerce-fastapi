import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = 'fastapi-ecommerce'
    APP_DESCRIPTION: str = 'Ecommerce developed with FastAPI'
    APP_VERSION: float = 1.0

    DOCS_URL = os.getenv('DOCS_URL', '/docs')


def get_settings():
    return Settings()