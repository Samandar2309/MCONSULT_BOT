import asyncio
from bot.database.session import async_session_maker


async def test():
    async with async_session_maker() as session:
        print("✅ DB session ishlayapti:", session)


asyncio.run(test())
