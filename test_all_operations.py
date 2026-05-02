"""
Комплексный тест для проверки всех операций с ticket'ом
"""
import asyncio
from bot.database.session import async_session_maker
from bot.db.repositories.tickets import TicketRepository
from bot.db.models import TicketStatus

async def test_ticket_operations():
    """Тестировать все операции с ticket'ом"""
    async with async_session_maker() as session:
        repo = TicketRepository(session)

        print("\n" + "=" * 50)
        print("🎫 ТЕСТ ОПЕРАЦИЙ С TICKET'ОМ")
        print("=" * 50)

        # 1. Создание ticket'а
        print("\n1️⃣  Создание нового ticket'а...")
        try:
            ticket = await repo.create(
                name="John Doe",
                phone="+998901234567",
                message="Help me with issue",
                username="@john_doe"
            )
            ticket_id = ticket.id
            print(f"   ✅ Ticket создан: ID={ticket_id}, Статус={ticket.status.value}")
        except Exception as e:
            print(f"   ❌ Ошибка: {e}")
            return False

        # 2. Получение ticket'а по ID
        print("\n2️⃣  Получение ticket'а по ID...")
        try:
            ticket = await repo.get(ticket_id)
            if ticket:
                print(f"   ✅ Ticket получен: {ticket.name}, Статус={ticket.status.value}")
            else:
                print(f"   ❌ Ticket не найден")
                return False
        except Exception as e:
            print(f"   ❌ Ошибка: {e}")
            return False

        # 3. Взять ticket (в работу)
        print("\n3️⃣  Взять ticket в работу...")
        try:
            result = await repo.take(
                ticket_id=ticket_id,
                operator_id=123456789,
                operator_name="Operator A"
            )
            if result:
                ticket = await repo.get(ticket_id)
                print(f"   ✅ Ticket взят: Статус={ticket.status.value}, Оператор={ticket.operator_name}")
            else:
                print(f"   ❌ Не удалось взять ticket (может быть уже взят)")
                return False
        except Exception as e:
            print(f"   ❌ Ошибка: {e}")
            return False

        # 4. Закрыть ticket (успешно)
        print("\n4️⃣  Закрыть ticket как успешный...")
        try:
            result = await repo.close(
                ticket_id=ticket_id,
                status=TicketStatus.SUCCESS
            )
            if result:
                ticket = await repo.get(ticket_id)
                print(f"   ✅ Ticket закрыт: Статус={ticket.status.value}")
            else:
                print(f"   ❌ Не удалось закрыть ticket")
                return False
        except Exception as e:
            print(f"   ❌ Ошибка: {e}")
            return False

        # 5. Получить статистику
        print("\n5️⃣  Получить статистику tickets'ов...")
        try:
            stats = await repo.total_stats()
            print(f"   ✅ Статистика:")
            print(f"      Total: {stats['total']}")
            print(f"      New: {stats['new']}")
            print(f"      In Progress: {stats['in_progress']}")
            print(f"      Success: {stats['success']}")
            print(f"      Rejected: {stats['rejected']}")
        except Exception as e:
            print(f"   ❌ Ошибка: {e}")
            return False

        print("\n" + "=" * 50)
        print("✅ ВСЕ ОПЕРАЦИИ С TICKET'ОМ РАБОТАЮТ ПРАВИЛЬНО!")
        print("=" * 50)
        return True

async def main():
    success = await test_ticket_operations()
    return success

if __name__ == "__main__":
    import sys
    try:
        result = asyncio.run(main())
        sys.exit(0 if result else 1)
    except Exception as e:
        print(f"\n❌ ФАТАЛЬНАЯ ОШИБКА: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

