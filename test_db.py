import asyncio
from bot.db.database import engine

async def test():
    async with engine.begin():
        print("✅ Database connected")

if __name__ == "__main__":
    asyncio.run(test())
