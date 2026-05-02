"""
Миграция для исправления enum ticketstatus с неправильными значениями
Преобразует enum значения из ВЕРХНЕГО в нижний регистр
"""
import asyncio
from sqlalchemy import text
from bot.database.session import engine

async def migrate_enum():
    """Пересоздать enum с правильными значениями в нижнем регистре"""
    async with engine.begin() as conn:
        print("🔄 Началась миграция enum ticketstatus...")

        try:
            # Шаг 1: Создаём новый enum тип с правильными значениями
            print("   1️⃣ Создаём новый enum тип...")
            await conn.execute(text("""
                CREATE TYPE ticketstatus_new AS ENUM ('new', 'in_progress', 'success', 'rejected');
            """))

            # Шаг 2: Преобразуем данные в колонке tickets.status
            print("   2️⃣ Преобразуем существующие данные...")
            await conn.execute(text("""
                ALTER TABLE tickets
                ALTER COLUMN status TYPE ticketstatus_new
                USING (
                    CASE status::text
                        WHEN 'NEW' THEN 'new'
                        WHEN 'IN_PROGRESS' THEN 'in_progress'
                        WHEN 'SUCCESS' THEN 'success'
                        WHEN 'REJECTED' THEN 'rejected'
                        ELSE 'new'
                    END
                )::ticketstatus_new;
            """))

            # Шаг 3: Удаляем старый enum тип
            print("   3️⃣ Удаляем старый enum тип...")
            await conn.execute(text("""
                DROP TYPE ticketstatus;
            """))

            # Шаг 4: Переименовываем новый enum в исходное имя
            print("   4️⃣ Переименовываем новый enum...")
            await conn.execute(text("""
                ALTER TYPE ticketstatus_new RENAME TO ticketstatus;
            """))

            print("✅ Миграция успешно завершена!")

        except Exception as e:
            print(f"❌ Ошибка при миграции: {e}")
            raise

if __name__ == "__main__":
    asyncio.run(migrate_enum())

