from __future__ import annotations

from datetime import date
from typing import Optional, List, Dict

from sqlalchemy import select, update, func
from sqlalchemy.ext.asyncio import AsyncSession

from bot.db.models import Ticket, TicketStatus


class TicketRepository:
    """
    🎫 Ticket bilan bog‘liq BARCHA DB operatsiyalar
    (CREATE, TAKE, CLOSE, STATS)
    """

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    # =================================================
    # ➕ CREATE TICKET
    # =================================================
    async def create(
            self,
            *,
            name: str,
            phone: str,
            message: str,
            username: Optional[str],
    ) -> Ticket:
        ticket = Ticket(
            name=name.strip(),
            phone=phone.strip(),
            username=(username or "yo‘q").strip(),
            message=message.strip(),
            status=TicketStatus.NEW,
        )

        try:
            self.session.add(ticket)
            await self.session.commit()
            await self.session.refresh(ticket)
            return ticket
        except Exception:
            await self.session.rollback()
            raise

    # =================================================
    # 🔎 GET BY ID
    # =================================================
    async def get(self, ticket_id: int) -> Optional[Ticket]:
        result = await self.session.execute(
            select(Ticket).where(Ticket.id == ticket_id)
        )
        return result.scalar_one_or_none()

    # =================================================
    # 📋 GET ALL (LIMIT BILAN VA LIMITSIZ)
    # =================================================
    async def get_all(self, limit: Optional[int] = None) -> List[Ticket]:
        # So'rovni yaratamiz
        query = select(Ticket).order_by(Ticket.created_at.desc())

        # Agar limit berilgan bo'lsa, uni qo'shamiz
        if limit is not None:
            query = query.limit(limit)

        result = await self.session.execute(query)
        return list(result.scalars().all())

    # =================================================
    # 🔒 TAKE TICKET (ATOMIC)
    # =================================================
    async def take(
            self,
            *,
            ticket_id: int,
            operator_id: int,
            operator_name: str,
    ) -> bool:
        stmt = (
            update(Ticket)
            .where(
                Ticket.id == ticket_id,
                Ticket.status == TicketStatus.NEW,
            )
            .values(
                status=TicketStatus.IN_PROGRESS,
                operator_id=operator_id,
                operator_name=operator_name.strip(),
            )
        )

        try:
            result = await self.session.execute(stmt)
            await self.session.commit()
            return result.rowcount == 1
        except Exception:
            await self.session.rollback()
            raise

    # =================================================
    # ✅❌ CLOSE TICKET
    # =================================================
    async def close(
            self,
            *,
            ticket_id: int,
            status: TicketStatus,
    ) -> bool:
        if status not in (TicketStatus.SUCCESS, TicketStatus.REJECTED):
            return False

        stmt = (
            update(Ticket)
            .where(
                Ticket.id == ticket_id,
                Ticket.status == TicketStatus.IN_PROGRESS,
            )
            .values(status=status)
        )

        try:
            result = await self.session.execute(stmt)
            await self.session.commit()
            return result.rowcount == 1
        except Exception:
            await self.session.rollback()
            raise

    # =================================================
    # 📊 TOTAL STATS (ADMIN)
    # =================================================
    async def total_stats(self) -> Dict[str, int]:
        result = await self.session.execute(
            select(
                func.count().label("total"),
                func.count().filter(Ticket.status == TicketStatus.NEW).label("new"),
                func.count().filter(Ticket.status == TicketStatus.IN_PROGRESS).label("in_progress"),
                func.count().filter(Ticket.status == TicketStatus.SUCCESS).label("success"),
                func.count().filter(Ticket.status == TicketStatus.REJECTED).label("rejected"),
            )
        )

        row = result.one()
        return {
            "total": row.total or 0,
            "new": row.new or 0,
            "in_progress": row.in_progress or 0,
            "success": row.success or 0,
            "rejected": row.rejected or 0,
        }

    # =================================================
    # 👨‍💻 TODAY OPERATOR STATS
    # =================================================
    async def today_operator_stats(self) -> Dict[int, dict]:
        today = date.today()

        result = await self.session.execute(
            select(
                Ticket.operator_id,
                Ticket.operator_name,
                func.count().label("total"),
                func.count().filter(Ticket.status == TicketStatus.SUCCESS).label("success"),
                func.count().filter(Ticket.status == TicketStatus.REJECTED).label("rejected"),
            )
            .where(
                Ticket.operator_id.isnot(None),
                func.date(Ticket.created_at) == today,
            )
            .group_by(Ticket.operator_id, Ticket.operator_name)
        )

        stats: Dict[int, dict] = {}
        for row in result.all():
            stats[row.operator_id] = {
                "operator_name": row.operator_name or "Noma'lum",
                "total": row.total or 0,
                "success": row.success or 0,
                "rejected": row.rejected or 0,
            }

        return stats