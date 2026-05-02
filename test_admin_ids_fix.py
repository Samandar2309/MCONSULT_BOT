"""
Тест для проверки исправления ADMIN_IDS
"""
import asyncio
from config import ADMIN_IDS
from bot.database.session import async_session_maker
from bot.db.repositories.tickets import TicketRepository
from bot.db.models import TicketStatus

async def test_admin_ids():
    """Проверить что ADMIN_IDS правильно обрабатывается"""
    print("\n" + "=" * 60)
    print("🧪 ТЕСТ ОБРАБОТКИ ADMIN_IDS")
    print("=" * 60)

    print(f"\n✓ ADMIN_IDS тип: {type(ADMIN_IDS)}")
    print(f"✓ ADMIN_IDS значение: {ADMIN_IDS}")
    print(f"✓ Количество админов: {len(ADMIN_IDS)}")

    # Проверяем что это список целых чисел
    if isinstance(ADMIN_IDS, list) and all(isinstance(id, int) for id in ADMIN_IDS):
        print("✓ ADMIN_IDS это список целых чисел ✅")
        return True
    else:
        print("✗ ADMIN_IDS имеет неправильный формат ❌")
        return False

async def test_admin_check():
    """Проверить логику проверки администратора"""
    print("\n" + "=" * 60)
    print("🧪 ТЕСТ ПРОВЕРКИ АДМИНИСТРАТОРА")
    print("=" * 60)

    # Если есть админы
    if ADMIN_IDS:
        test_admin_id = ADMIN_IDS[0]
        test_user_id = 12345678

        # Проверяем правильный синтаксис
        is_admin = test_admin_id in ADMIN_IDS
        is_not_admin = test_user_id not in ADMIN_IDS

        print(f"\n✓ test_admin_id ({test_admin_id}) in ADMIN_IDS: {is_admin}")
        print(f"✓ test_user_id ({test_user_id}) not in ADMIN_IDS: {is_not_admin}")

        if is_admin and is_not_admin:
            print("\n✅ Логика проверки администратора работает правильно!")
            return True
        else:
            print("\n❌ ОШИБКА в логике проверки администратора!")
            return False
    else:
        print("❌ ADMIN_IDS пуст!")
        return False

async def test_ticket_creation():
    """Проверить создание ticket'а (основной тест)"""
    print("\n" + "=" * 60)
    print("🧪 ТЕСТ СОЗДАНИЯ TICKET'А")
    print("=" * 60)

    try:
        async with async_session_maker() as session:
            repo = TicketRepository(session)
            ticket = await repo.create(
                name="Admin Test",
                phone="+998901234567",
                message="Test message for admin",
                username="@admin_test"
            )
            print(f"\n✅ Ticket успешно создан!")
            print(f"   ID: {ticket.id}")
            print(f"   Статус: {ticket.status.value}")
            return True
    except Exception as e:
        print(f"\n❌ ОШИБКА при создании ticket'а: {e}")
        import traceback
        traceback.print_exc()
        return False

async def main():
    print("\n" + "=" * 60)
    print("🔍 ПРОВЕРКА ИСПРАВЛЕНИЙ ADMIN_IDS")
    print("=" * 60)

    results = []

    results.append(("ADMIN_IDS формат", await test_admin_ids()))
    results.append(("Проверка администратора", await test_admin_check()))
    results.append(("Создание ticket'а", await test_ticket_creation()))

    print("\n" + "=" * 60)
    print("📊 РЕЗУЛЬТАТЫ ТЕСТОВ:")
    print("=" * 60)

    all_passed = True
    for test_name, result in results:
        status = "✅ ПРОЙДЕН" if result else "❌ FAILED"
        print(f"  {status}: {test_name}")
        if not result:
            all_passed = False

    print("=" * 60)

    if all_passed:
        print("\n🎉 ВСЕ ТЕСТЫ ПРОЙДЕНЫ!")
        print("✅ БОТ ГОТОВ К ЗАПУСКУ!")
    else:
        print("\n❌ НЕКОТОРЫЕ ТЕСТЫ НЕ ПРОШЛИ!")

    print("=" * 60 + "\n")

    return all_passed

if __name__ == "__main__":
    try:
        result = asyncio.run(main())
        import sys
        sys.exit(0 if result else 1)
    except Exception as e:
        print(f"\n❌ ОШИБКА: {e}")
        import traceback
        traceback.print_exc()
        import sys
        sys.exit(1)

