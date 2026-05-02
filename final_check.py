"""
🎯 ФИНАЛЬНАЯ ПРОВЕРКА - ВСЕ ТЕСТЫ
Проверяет, что исправление enum полностью работает
"""
import asyncio
import sys
from bot.database.session import async_session_maker, engine
from bot.db.repositories.tickets import TicketRepository
from bot.db.models import Ticket, TicketStatus
from sqlalchemy import text, select

async def test_enum_values():
    """Проверка что enum имеет правильные значения в БД"""
    print("\n[1/5] Проверка enum типа в PostgreSQL...")
    try:
        async with engine.connect() as conn:
            result = await conn.execute(text("""
                SELECT enumlabel FROM pg_enum 
                WHERE enumtypid = 'ticketstatus'::regtype 
                ORDER BY enumsortorder
            """))
            rows = result.fetchall()
            expected = ['new', 'in_progress', 'success', 'rejected']
            actual = [row[0] for row in rows]

            if actual == expected:
                print(f"      ✅ Enum содержит правильные значения: {actual}")
                return True
            else:
                print(f"      ❌ Enum содержит неправильные значения!")
                print(f"         Ожидалось: {expected}")
                print(f"         Получено: {actual}")
                return False
    except Exception as e:
        print(f"      ❌ Ошибка при проверке enum: {e}")
        return False

async def test_session():
    """Проверка подключения к БД"""
    print("\n[2/5] Проверка подключения к БД...")
    try:
        async with async_session_maker() as session:
            print("      ✅ Сессия БД успешно создана")
            return True
    except Exception as e:
        print(f"      ❌ Ошибка подключения: {e}")
        return False

async def test_ticket_creation():
    """Проверка создания ticket'а"""
    print("\n[3/5] Проверка создания ticket'а...")
    try:
        async with async_session_maker() as session:
            repo = TicketRepository(session)
            ticket = await repo.create(
                name="Test Final",
                phone="+998901234567",
                message="Final test",
                username="@test_final"
            )
            if ticket.status == TicketStatus.NEW and ticket.status.value == 'new':
                print(f"      ✅ Ticket создан с правильным статусом: {ticket.status.value}")
                return ticket.id
            else:
                print(f"      ❌ Ticket имеет неправильный статус: {ticket.status}")
                return None
    except Exception as e:
        print(f"      ❌ Ошибка при создании ticket'а: {e}")
        return None

async def test_ticket_operations(ticket_id):
    """Проверка операций с ticket'ом"""
    print("\n[4/5] Проверка операций с ticket'ом...")
    try:
        async with async_session_maker() as session:
            repo = TicketRepository(session)

            # Получение
            ticket = await repo.get(ticket_id)
            if not ticket or ticket.status.value != 'new':
                print(f"      ❌ Ошибка при получении ticket'а")
                return False

            # Взятие в работу
            result = await repo.take(
                ticket_id=ticket_id,
                operator_id=999,
                operator_name="test_op"
            )
            if not result:
                print(f"      ❌ Ошибка при взятии ticket'а в работу")
                return False

            ticket = await repo.get(ticket_id)
            if ticket.status.value != 'in_progress':
                print(f"      ❌ Ticket имеет неправильный статус после взятия")
                return False

            # Закрытие
            result = await repo.close(ticket_id=ticket_id, status=TicketStatus.SUCCESS)
            if not result:
                print(f"      ❌ Ошибка при закрытии ticket'а")
                return False

            ticket = await repo.get(ticket_id)
            if ticket.status.value != 'success':
                print(f"      ❌ Ticket имеет неправильный статус после закрытия")
                return False

            print("      ✅ Все операции с ticket'ом работают правильно")
            return True

    except Exception as e:
        print(f"      ❌ Ошибка при операциях с ticket'ом: {e}")
        return False

async def test_stats():
    """Проверка статистики"""
    print("\n[5/5] Проверка работы статистики...")
    try:
        async with async_session_maker() as session:
            repo = TicketRepository(session)
            stats = await repo.total_stats()

            # Проверяем что все ключи есть
            required_keys = ['total', 'new', 'in_progress', 'success', 'rejected']
            if all(key in stats for key in required_keys):
                print(f"      ✅ Статистика работает: total={stats['total']}, "
                      f"new={stats['new']}, in_progress={stats['in_progress']}, "
                      f"success={stats['success']}, rejected={stats['rejected']}")
                return True
            else:
                print(f"      ❌ Статистика содержит неполные данные")
                return False

    except Exception as e:
        print(f"      ❌ Ошибка при получении статистики: {e}")
        return False

async def main():
    print("=" * 70)
    print("🎯 ФИНАЛЬНАЯ ПРОВЕРКА ИСПРАВЛЕНИЯ ENUM")
    print("=" * 70)

    # Тестируем все компоненты
    results = []

    results.append(("Enum в PostgreSQL", await test_enum_values()))
    results.append(("Подключение к БД", await test_session()))

    ticket_id = None
    result = await test_ticket_creation()
    results.append(("Создание ticket'а", result is not None))
    ticket_id = result

    if ticket_id:
        results.append(("Операции с ticket'ом", await test_ticket_operations(ticket_id)))

    results.append(("Статистика", await test_stats()))

    # Выводим результаты
    print("\n" + "=" * 70)
    print("📊 РЕЗУЛЬТАТЫ ТЕСТОВ:")
    print("=" * 70)

    all_passed = True
    for test_name, result in results:
        status = "✅ ПРОЙДЕН" if result else "❌ FAILED"
        print(f"  {status}: {test_name}")
        if not result:
            all_passed = False

    print("=" * 70)

    if all_passed:
        print("\n🎉 ВСЕ ТЕСТЫ ПРОЙДЕНЫ!")
        print("✅ ИСПРАВЛЕНИЕ ГОТОВО К РАЗВЁРТЫВАНИЮ НА СЕРВЕРЕ!")
        print("=" * 70)
        return True
    else:
        print("\n❌ НЕКОТОРЫЕ ТЕСТЫ НЕ ПРОШЛИ!")
        print("=" * 70)
        return False

if __name__ == "__main__":
    try:
        result = asyncio.run(main())
        sys.exit(0 if result else 1)
    except Exception as e:
        print(f"\n❌ КРИТИЧЕСКАЯ ОШИБКА: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

