"""
Тестовый скрипт для проверки подключения и структуры БД
"""
import asyncio
import os
from sqlalchemy import text
from bot.database.session import async_session_maker, engine

async def check_enum_type():
    """Проверить существующий enum тип и его значения"""
    async with engine.connect() as conn:
        # Проверяем существующие enum типы
        result = await conn.execute(text("""
            SELECT typname, enumlabel 
            FROM pg_type 
            JOIN pg_enum ON pg_type.oid = pg_enum.enumtypid
            WHERE typname = 'ticketstatus'
            ORDER BY enumsortorder
        """))
        rows = result.fetchall()
        if rows:
            print("\n📊 Текущие значения enum 'ticketstatus':")
            for row in rows:
                print(f"   - {row[1]}")
        else:
            print("\n❌ Enum тип 'ticketstatus' не найден в БД")

async def check_tickets_schema():
    """Проверить схему таблицы tickets"""
    async with engine.connect() as conn:
        result = await conn.execute(text("""
            SELECT column_name, data_type, is_nullable
            FROM information_schema.columns
            WHERE table_name = 'tickets'
            ORDER BY ordinal_position
        """))
        rows = result.fetchall()
        if rows:
            print("\n📋 Схема таблицы 'tickets':")
            for row in rows:
                print(f"   {row[0]}: {row[1]} (nullable: {row[2]})")
        else:
            print("\n❌ Таблица 'tickets' не найдена в БД")

async def test_session():
    """Проверить сессию БД"""
    async with async_session_maker() as session:
        print("\n✅ Сессия БД успешно создана")
        return True

async def main():
    print("🔍 Проверка БД...")
    try:
        await test_session()
        await check_enum_type()
        await check_tickets_schema()
        print("\n✅ Проверка завершена!")
    except Exception as e:
        print(f"\n❌ ОШИБКА: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())

