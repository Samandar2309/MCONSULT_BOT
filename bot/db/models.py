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



class TicketStatus(str, Enum):
    NEW = "new"
    IN_PROGRESS = "in_progress"
    SUCCESS = "success"
    REJECTED = "rejected"


class Ticket(Base):
    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        index=True,
    )

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

    message: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    status: Mapped[TicketStatus] = mapped_column(
        SAEnum(
            TicketStatus,
            name="ticketstatus",
            native_enum=True,
            create_type=False,
            validate_strings=True,
            # Важно: SQLAlchemy должен использовать .value вместо имён членов
            values_callable=lambda enums: [e.value for e in enums],
        ),
        nullable=False,
        index=True,
        default=TicketStatus.NEW,
        server_default=TicketStatus.NEW.value,
    )

    operator_id: Mapped[Optional[int]] = mapped_column(
        BigInteger,
        nullable=True,
    )

    operator_name: Mapped[Optional[str]] = mapped_column(
        String(100),
        nullable=True,
    )
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

    def __repr__(self) -> str:
        return (
            f"<Ticket id={self.id} "
            f"status={self.status} "
            f"name={self.name} "
            f"operator={self.operator_id}>"
        )