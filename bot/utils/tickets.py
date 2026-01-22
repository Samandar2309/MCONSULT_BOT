from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, date
from enum import Enum
from typing import Dict, Optional, List
from threading import Lock


# =====================================================
# 🔹 TICKET STATUSLAR
# =====================================================
class TicketStatus(str, Enum):
    NEW = "new"
    IN_PROGRESS = "in_progress"
    SUCCESS = "success"
    REJECTED = "rejected"


# =====================================================
# 🔹 TICKET MODEL
# =====================================================
@dataclass
class Ticket:
    id: int

    # 👤 Mijoz
    name: str
    phone: str
    username: str

    # 📌 Xizmat
    category: str
    service: str

    # 📝 Xabar
    message: str

    # 🔄 Holat
    status: TicketStatus = TicketStatus.NEW

    # 👨‍💻 Operator
    operator_id: Optional[int] = None
    operator_name: Optional[str] = None

    # ⏱ Vaqt
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)


# =====================================================
# 🔹 TICKET STORAGE (hozir RAM, keyin DB)
# =====================================================
class TicketStore:
    def __init__(self) -> None:
        self._tickets: Dict[int, Ticket] = {}
        self._counter: int = 0
        self._lock = Lock()

    # -------------------------------------------------
    # ➕ CREATE TICKET
    # -------------------------------------------------
    def create(
        self,
        *,
        name: str,
        phone: str,
        message: str,
        username: Optional[str],
        category: Optional[str],
        service: Optional[str],
    ) -> Ticket:
        with self._lock:
            self._counter += 1
            now = datetime.utcnow()

            ticket = Ticket(
                id=self._counter,
                name=name,
                phone=phone,
                username=username or "yo‘q",
                category=category or "Aniqlanmagan",
                service=service or "Aniqlanmagan",
                message=message,
                created_at=now,
                updated_at=now,
            )

            self._tickets[ticket.id] = ticket
            return ticket

    # -------------------------------------------------
    # 🔒 TAKE TICKET (LOCK)
    # -------------------------------------------------
    def take(
        self,
        *,
        ticket_id: int,
        operator_id: int,
        operator_name: str,
    ) -> bool:
        with self._lock:
            ticket = self._tickets.get(ticket_id)
            if not ticket:
                return False

            if ticket.status != TicketStatus.NEW:
                return False

            ticket.status = TicketStatus.IN_PROGRESS
            ticket.operator_id = operator_id
            ticket.operator_name = operator_name
            ticket.updated_at = datetime.utcnow()
            return True

    # -------------------------------------------------
    # ✅❌ CLOSE TICKET
    # -------------------------------------------------
    def close(
        self,
        *,
        ticket_id: int,
        status: TicketStatus,
    ) -> bool:
        if status not in (TicketStatus.SUCCESS, TicketStatus.REJECTED):
            return False

        with self._lock:
            ticket = self._tickets.get(ticket_id)
            if not ticket:
                return False

            if ticket.status != TicketStatus.IN_PROGRESS:
                return False

            ticket.status = status
            ticket.updated_at = datetime.utcnow()
            return True

    # -------------------------------------------------
    # 🔎 GETTERS
    # -------------------------------------------------
    def get(self, ticket_id: int) -> Optional[Ticket]:
        return self._tickets.get(ticket_id)

    def all(self) -> List[Ticket]:
        return list(self._tickets.values())

    # -------------------------------------------------
    # 📊 ADMIN STATISTICS
    # -------------------------------------------------
    def total_stats(self) -> dict:
        return {
            "total": len(self._tickets),
            "new": sum(t.status == TicketStatus.NEW for t in self._tickets.values()),
            "in_progress": sum(t.status == TicketStatus.IN_PROGRESS for t in self._tickets.values()),
            "success": sum(t.status == TicketStatus.SUCCESS for t in self._tickets.values()),
            "rejected": sum(t.status == TicketStatus.REJECTED for t in self._tickets.values()),
        }

    def today_operator_stats(self) -> Dict[int, dict]:
        today = date.today()
        stats: Dict[int, dict] = {}

        for t in self._tickets.values():
            if t.created_at.date() != today:
                continue
            if not t.operator_id:
                continue

            if t.operator_id not in stats:
                stats[t.operator_id] = {
                    "operator_name": t.operator_name,
                    "total": 0,
                    "success": 0,
                    "rejected": 0,
                }

            stats[t.operator_id]["total"] += 1

            if t.status == TicketStatus.SUCCESS:
                stats[t.operator_id]["success"] += 1
            elif t.status == TicketStatus.REJECTED:
                stats[t.operator_id]["rejected"] += 1

        return stats


# =====================================================
# 🔹 SINGLETON (GLOBAL INSTANCE)
# =====================================================
ticket_store = TicketStore()
