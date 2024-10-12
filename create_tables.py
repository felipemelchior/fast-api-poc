import asyncio
import models.__all_models

from core.configs import settings
from core.database import engine

async def create_tables() -> None:  
    print("Creating tables...")

    async with engine.begin() as conn:
        await conn.run_sync(settings.DB_BASE_MODEL.metadata.drop_all)
        await conn.run_sync(settings.DB_BASE_MODEL.metadata.create_all)
    print("Tables created sucessfully")

if __name__ == '__main__':
    asyncio.run(create_tables())