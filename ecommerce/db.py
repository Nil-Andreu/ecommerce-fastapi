from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ecommerce.config import get_settings

settings = get_settings()

engine = create_engine(settings.DATABASE_URI)
session = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def get_db():
    db = session()

    try:
        yield db
    finally:
        db.close()
