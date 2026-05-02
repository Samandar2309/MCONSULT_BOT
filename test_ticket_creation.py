"""
Тестовый скрипт для проверки создания ticket'а
"""
import asyncio
from bot.database.session import async_session_maker
from bot.db.repositories.tickets import TicketRepository

async def test_create_ticket():
    """Попытаться создать ticket и проверить, что нет enum ошибок"""
    async with async_session_maker() as session:
        repo = TicketRepository(session)

        try:
            print("🎫 Пытаюсь создать ticket...")
            ticket = await repo.create(
                name="Test User",
                phone="+998901234567",
                message="Test message",
                username="@test_user"
            )
            print(f"✅ Ticket успешно создан!")
            print(f"   ID: {ticket.id}")
            print(f"   Статус: {ticket.status}")
            print(f"   Имя: {ticket.name}")
            print(f"   Телефон: {ticket.phone}")
            return True
        except Exception as e:
            print(f"❌ ОШИБКА при создании ticket: {e}")
            import traceback
            traceback.print_exc()
            return False

async def main():
    print("=" * 50)
    print("🔍 ТЕСТИРОВАНИЕ СОЗДАНИЯ TICKET'а")
    print("=" * 50)

    success = await test_create_ticket()

    print("\n" + "=" * 50)
    if success:
        print("✅ ВСЕ ТЕСТЫ ПРОЙДЕНЫ!")
    else:
        print("❌ ТЕСТЫ НЕ ПРОЙДЕНЫ!")
    print("=" * 50)

if __name__ == "__main__":
    asyncio.run(main())

