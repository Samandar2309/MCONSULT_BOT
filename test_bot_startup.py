"""
Короткий тест для проверки, что приложение запускается без errors
"""
import asyncio
import sys
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage

from config import BOT_TOKEN
from bot.database.base import Base
from bot.database.session import engine

async def init_db():
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        print("✅ Ma'lumotlar bazasi jadvallari tayyor.")
    except Exception as e:
        print(f"❌ Bazani ishga tushirishda xatolik: {e}")
        sys.exit(1)

async def main():
    print("🔍 TЕСТИРОВАНИЕ ЗАПУСКА БОТА...")
    print("=" * 50)

    # Инициализируем БД
    await init_db()

    # Проверяем, что можно создать бота
    try:
        bot = Bot(
            token=BOT_TOKEN,
            default=DefaultBotProperties(parse_mode=ParseMode.HTML)
        )
        dispatcher = Dispatcher(storage=MemoryStorage())
        print("✅ Bot успешно инициализирован")
        print("=" * 50)
        print("✅ ВСЕ ПРОВЕРКИ ПРОЙДЕНЫ - БОТ ГОТОВ К ЗАПУСКУ!")
        print("=" * 50)
        return True
    except Exception as e:
        print(f"❌ ОШИБКА: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    try:
        result = asyncio.run(main())
        sys.exit(0 if result else 1)
    except Exception as e:
        print(f"❌ ФАТАЛЬНАЯ ОШИБКА: {e}")
        sys.exit(1)

