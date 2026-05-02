import logging
from aiogram import Router, F
from aiogram.types import Message
from sqlalchemy import select, func, and_

from config import ADMIN_IDS
from bot.keyboards.reply import main_menu

from bot.database.session import async_session_maker
from bot.db.repositories.tickets import TicketRepository
from bot.db.models import Ticket, TicketStatus

router = Router()


def is_admin(message: Message) -> bool:
    return message.from_user.id in ADMIN_IDS


# =====================================================
# 📋 JAMI MUROJAATLAR (Limit va chiroyli format bilan)
# =====================================================
@router.message(F.text.in_(["📋 Jami murojaatlar", "📋 Все заявки"]))
async def all_tickets(message: Message):
    if not is_admin(message): return

    async with async_session_maker() as session:
        # Oxirgi 20 ta murojaatni olish (xabar limiti buzilmasligi uchun)
        repo = TicketRepository(session)
        tickets = await repo.get_all()

    if not tickets:
        await message.answer("📭 Hozircha murojaatlar yo‘q")
        return

    status_map = {
        TicketStatus.NEW: "🟡",
        TicketStatus.IN_PROGRESS: "🔵",
        TicketStatus.SUCCESS: "🟢",
        TicketStatus.REJECTED: "🔴",
    }

    text = "📋 <b>Oxirgi 20 ta murojaat:</b>\n\n"
    for t in tickets:
        text += (
            f"{status_map.get(t.status, '⚪️')} 🆔 <code>{t.id}</code> | {t.name}\n"
            f"📞 {t.phone}\n"
            f"-------------------\n"
        )

    await message.answer(text, parse_mode="HTML")


# =====================================================
# 📊 UMUMIY STATISTIKA
# =====================================================
@router.message(F.text.in_(["📊 Statistika", "📊 Статистика"]))
async def total_stats(message: Message):
    if not is_admin(message): return

    async with async_session_maker() as session:
        repo = TicketRepository(session)
        stats = await repo.total_stats()

    text = (
        "📊 <b>UMUMIY STATISTIKA</b>\n\n"
        f"📥 Jami: <b>{stats.get('total', 0)}</b>\n"
        f"🟡 Yangi: <b>{stats.get('new', 0)}</b>\n"
        f"🔵 Jarayonda: <b>{stats.get('in_progress', 0)}</b>\n"
        f"🟢 Muvaffaqiyatli: <b>{stats.get('success', 0)}</b>\n"
        f"🔴 Rad etilgan: <b>{stats.get('rejected', 0)}</b>"
    )

    await message.answer(text, parse_mode="HTML")


# =====================================================
# 👨‍💻 OPERATORLAR STATISTIKASI (Eng aniq variant)
# =====================================================
@router.message(F.text.in_(["👨‍💻 Operatorlar statistikasi", "👨‍💻 Статистика операторов"]))
async def operator_stats(message: Message):
    if not is_admin(message): return

    async with async_session_maker() as session:
        # Repositoriyaga tayanmasdan, to'g'ridan-to'g'ri SQL so'rov yuboramiz
        # Bu xatolik ehtimolini nolga tushiradi
        query = (
            select(
                Ticket.operator_name,
                func.count(Ticket.id).label("total"),
                func.count(Ticket.id).filter(Ticket.status == TicketStatus.SUCCESS).label("success"),
                func.count(Ticket.id).filter(Ticket.status == TicketStatus.REJECTED).label("rejected")
            )
            .where(Ticket.operator_id.isnot(None))
            .group_by(Ticket.operator_name)
        )

        result = await session.execute(query)
        rows = result.all()

    if not rows:
        await message.answer("📭 Hozircha operatorlar tomonidan yopilgan murojaatlar yo‘q")
        return

    text = "👨‍💻 <b>Operatorlar faoliyati:</b>\n\n"
    for r in rows:
        text += (
            f"👤 <b>{r.operator_name}</b>\n"
            f"✅ Yopilgan: {r.success} ta\n"
            f"❌ Rad etilgan: {r.rejected} ta\n"
            f"📊 Jami: {r.total} ta\n"
            f"-------------------\n"
        )

    await message.answer(text, parse_mode="HTML")