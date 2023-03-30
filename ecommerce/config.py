import os
from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    APP_NAME: str = 'fastapi-ecommerce'
    APP_DESCRIPTION: str = 'Ecommerce developed with FastAPI'
    APP_VERSION: float = 1.0

    DOCS_URL: str = os.getenv('DOCS_URL', '/docs')

    # For database configuration
    DATABASE_USERNAME: str = os.getenv('DATABASE_USERNAME')
    DATABASE_PASSWORD: str = os.getenv('DATABASE_PASSWORD')
    DATABASE_NAME: str = os.getenv('DATABASE_NAME')
    DATABASE_HOST: str = os.getenv('DATABASE_HOST')
    DATABASE_PORT: str = os.getenv('DATABASE_PORT', 5432)

    DATABASE_URI: PostgresDsn = f'postgresq.://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}:{DATABASE_PORT}'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


def get_settings():
    return Settings()
