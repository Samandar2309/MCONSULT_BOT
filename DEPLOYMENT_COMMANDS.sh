#!/bin/bash
# 🚀 ТОЧНЫЕ КОМАНДЫ ДЛЯ РАЗВЁРТЫВАНИЯ НА СЕРВЕРЕ vps07936.eskiz.uz
# Дата: 2 мая 2026
# Версия: v1.0

echo "🚀 РАЗВЁРТЫВАНИЕ ИСПРАВЛЕНИЙ НА СЕРВЕР"
echo "═══════════════════════════════════════════════════════════════════════"

# ШАГИ:
# 1. СКОПИРОВАТЬ ФАЙЛЫ (выполнить на локальной машине)
# 2. ВЫПОЛНИТЬ МИГРАЦИЮ (выполнить на сервере)
# 3. ПЕРЕЗАГРУЗИТЬ СЕРВИС (выполнить на сервере)

echo ""
echo "📋 ШАГ 1: СКОПИРОВАТЬ ФАЙЛЫ НА СЕРВЕР"
echo "───────────────────────────────────────────────────────────────────────"
echo ""
echo "Выполните эти команды на ЛОКАЛЬНОЙ машине:"
echo ""

cat << 'EOF'
# Критические файлы (ОБЯЗАТЕЛЬНО)
scp bot/handlers/contact.py root@vps07936.eskiz.uz:~/mcbot/MCONSULT_BOT/bot/handlers/
scp bot/handlers/start.py root@vps07936.eskiz.uz:~/mcbot/MCONSULT_BOT/bot/handlers/
scp bot/db/models.py root@vps07936.eskiz.uz:~/mcbot/MCONSULT_BOT/bot/db/

# Миграция enum (НУЖНА ДЛЯ МИГРАЦИИ БД)
scp migrate_enum.py root@vps07936.eskiz.uz:~/mcbot/MCONSULT_BOT/

EOF

echo ""
echo "📋 ШАГ 2: ПОДКЛЮЧИТЬСЯ К СЕРВЕРУ И ВЫПОЛНИТЬ МИГРАЦИЮ"
echo "───────────────────────────────────────────────────────────────────────"
echo ""
echo "Выполните эти команды на СЕРВЕРЕ:"
echo ""

cat << 'EOF'
# Подключиться к серверу
ssh root@vps07936.eskiz.uz

# Перейти в директорию проекта
cd ~/mcbot/MCONSULT_BOT

# Активировать виртуальное окружение
source .venv/bin/activate

# ВАЖНО: Сделайте резервную копию БД (если ещё не делали)
pg_dump mc_mchj > mc_mchj_backup_$(date +%Y%m%d_%H%M%S).sql

# Выполнить миграцию enum (если enum в БД имеет старые значения)
python migrate_enum.py

# Если миграция успешна, вы увидите:
# ✅ Миграция успешно завершена!

EOF

echo ""
echo "📋 ШАГ 3: ПЕРЕЗАГРУЗИТЬ СЕРВИС И ПРОВЕРИТЬ"
echo "───────────────────────────────────────────────────────────────────────"
echo ""

cat << 'EOF'
# Перезагрузить сервис
sudo systemctl restart mcbot

# Подождите 2-3 секунды
sleep 3

# Проверить логи (нажмите Ctrl+C для выхода)
journalctl -u mcbot -f

# ОЖИДАЕМЫЙ РЕЗУЛЬТАТ:
# ✅ Ma'lumotlar bazasi jadvallari tayyor.
# 🤖 MC_MCHJ (MConsult) bot ishga tushdi...
# (БЕЗ ОШИБОК с enum или ADMIN_IDS)

EOF

echo ""
echo "═══════════════════════════════════════════════════════════════════════"
echo "✅ РАЗВЁРТЫВАНИЕ ГОТОВО"
echo ""
echo "Все команды выше готовы к копированию и выполнению!"
echo ""

