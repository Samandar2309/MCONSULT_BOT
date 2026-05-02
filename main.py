import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage

from config import BOT_TOKEN
# ⬇️ Yangi importlar
from bot.database.base import Base
from bot.database.session import engine
from bot.handlers import start, menu, services, contact, operator, admin
from bot.middleware import BotMiddleware

# ⬇️ Jadvallarni yaratish funksiyasi
async def init_db():
    try:
        async with engine.begin() as conn:
            # Bu qator Ticket modeliga qarab jadvalni yaratadi
            await conn.run_sync(Base.metadata.create_all)
        print("✅ Ma'lumotlar bazasi jadvallari tayyor.")
    except Exception as e:
        print(f"❌ Bazani ishga tushirishda xatolik: {e}")

def create_dispatcher() -> Dispatcher:
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(start.router)
    dp.include_router(menu.router)
    dp.include_router(services.router)
    dp.include_router(contact.router)
    dp.include_router(operator.router)
    dp.include_router(admin.router)
    return dp

async def main():
    # ⬇️ 1. Avval bazani tekshiramiz/yaratamiz
    await init_db()

    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = create_dispatcher()

    # ⬇️ Middleware'ni qo'shamiz bot'ni aksesga qilish uchun
    dp.message.middleware(BotMiddleware(bot))
    dp.callback_query.middleware(BotMiddleware(bot))

    print("🤖 MC_MCHJ (MConsult) bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("⛔ Bot to‘xtatildi")