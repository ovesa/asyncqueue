import asyncpg
from app.config import settings

pool = None

async def get_pool():
    global pool
    if pool is None:
        pool = await asyncpg.create_pool(
            settings.database_url,
            min_size=2,
            max_size=10
        )
    return pool

async def close_pool():
    global pool
    if pool:
        await pool.close()
        pool = None