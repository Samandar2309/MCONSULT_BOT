#!/bin/bash

# 🚀 ИНСТРУКЦИЯ ДЛЯ РАЗВЁРТЫВАНИЯ НА СЕРВЕРЕ
# Исправление ошибки PostgreSQL ENUM ticketstatus

echo "🔧 Развёртывание исправления на сервер..."

# Проверяем, что мы находимся в правильной директории
if [ ! -f "bot/db/models.py" ]; then
    echo "❌ ОШИБКА: bot/db/models.py не найден!"
    echo "   Пожалуйста, выполняйте команду из директории mcbot/MCONSULT_BOT"
    exit 1
fi

echo ""
echo "=" * 60
echo "ШАГИ ДЛЯ ИСПРАВЛЕНИЯ:"
echo "=" * 60

# Шаг 1: Резервная копия
echo ""
echo "1️⃣ СОЗДАНИЕ РЕЗЕРВНОЙ КОПИИ БД..."
BACKUP_FILE="mc_mchj_backup_$(date +%Y%m%d_%H%M%S).sql"
if pg_dump mc_mchj > "$BACKUP_FILE"; then
    echo "   ✅ Резервная копия создана: $BACKUP_FILE"
else
    echo "   ❌ Ошибка при создании резервной копии!"
    exit 1
fi

# Шаг 2: Активируем виртуальное окружение
echo ""
echo "2️⃣ АКТИВАЦИЯ ВИРТУАЛЬНОГО ОКРУЖЕНИЯ..."
if [ -d ".venv" ]; then
    source .venv/bin/activate
    echo "   ✅ Виртуальное окружение активировано"
else
    echo "   ⚠️  Виртуальное окружение не найдено, предполагается, что оно уже активировано"
fi

# Шаг 3: Выполняем миграцию enum
echo ""
echo "3️⃣ ВЫПОЛНЕНИЕ МИГРАЦИИ ENUM..."
if python migrate_enum.py; then
    echo "   ✅ Миграция enum успешно завершена"
else
    echo "   ❌ ОШИБКА при выполнении миграции!"
    echo "   Восстанавливаем БД из резервной копии..."
    psql mc_mchj < "$BACKUP_FILE"
    exit 1
fi

# Шаг 4: Перезагружаем сервис
echo ""
echo "4️⃣ ПЕРЕЗАГРУЗКА СЕРВИСА БОТА..."
if sudo systemctl restart mcbot; then
    echo "   ✅ Сервис перезагружен"
else
    echo "   ⚠️  Не удалось перезагрузить сервис автоматически"
    echo "   Пожалуйста, выполните вручную: sudo systemctl restart mcbot"
fi

# Шаг 5: Проверяем логи
echo ""
echo "5️⃣ ПРОВЕРКА ЛОГОВ СЕРВИСА (первые 20 строк)..."
echo "   (нажмите Ctrl+C для выхода)"
sleep 2
sudo journalctl -u mcbot -n 20 --no-pager
echo ""

echo ""
echo "=" * 60
echo "✅ РАЗВЁРТЫВАНИЕ ЗАВЕРШЕНО!"
echo "=" * 60
echo ""
echo "📝 ПРИМЕЧАНИЯ:"
echo "   • В случае ошибки можно восстановить БД из резервной копии:"
echo "     psql mc_mchj < $BACKUP_FILE"
echo "   • Полная диагностика: sudo journalctl -u mcbot -f"
echo ""

