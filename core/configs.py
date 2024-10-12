from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    BASE_URL: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://admin:admin@localhost:5432/university'
    DB_BASE_MODEL = declarative_base()

    class Config:
        case_sensitive = True

settings = Settings()