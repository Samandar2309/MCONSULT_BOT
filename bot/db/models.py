from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional

from sqlalchemy import (
    String,
    BigInteger,
    Text,
    DateTime,
    Enum as SAEnum,
    func,
    Integer,
)
from sqlalchemy.orm import Mapped, mapped_column

from bot.database.base import Base


# =====================================================
# 🔹 TICKET STATUS (ENUM)
# =====================================================
class TicketStatus(str, Enum):
    NEW = "new"
    IN_PROGRESS = "in_progress"
    SUCCESS = "success"
    REJECTED = "rejected"


# =====================================================
# 🎫 TICKET MODEL (POSTGRESQL)
# =====================================================
class Ticket(Base):
    __tablename__ = "tickets"

    # 🔹 PRIMARY KEY
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        index=True,
    )

    # 👤 MIJOZ MA'LUMOTLARI
    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    phone: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    username: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        default="yo‘q",
        server_default="yo‘q",
    )

    # 📝 MUROJAAT MATNI
    message: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    # 🔄 STATUS
    # 'native_enum=True' PostgreSQL uchun eng yaxshi amaliyotdir
    status: Mapped[TicketStatus] = mapped_column(
        SAEnum(
            TicketStatus,
            name="ticketstatus",
            native_enum=True,
            create_type=True,
        ),
        nullable=False,
        index=True,
        default=TicketStatus.NEW,
        server_default=TicketStatus.NEW.value,
    )

    # 👨‍💻 OPERATOR (BigInteger Telegram ID uchun shart)
    operator_id: Mapped[Optional[int]] = mapped_column(
        BigInteger,
        nullable=True,
    )

    operator_name: Mapped[Optional[str]] = mapped_column(
        String(100),
        nullable=True,
    )

    # ⏱ VAQT (Xatolikni oldini olish uchun ham SQL, ham Python darajasida default)
    # default=datetime.utcnow -> Python orqali yozish uchun
    # server_default=func.now() -> Agar SQL o'zi yozsa
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.utcnow,
        server_default=func.now(),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.utcnow,
        server_default=func.now(),
        onupdate=func.now(),
    )

    # -------------------------------------------------
    # 🧾 DEBUG / LOG
    # -------------------------------------------------
    def __repr__(self) -> str:
        return (
            f"<Ticket id={self.id} "
            f"status={self.status} "
            f"name={self.name} "
            f"operator={self.operator_id}>"
        )