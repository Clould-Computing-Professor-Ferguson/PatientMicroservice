# models.py
from __future__ import annotations
from sqlalchemy import String, Date, Text, TIMESTAMP, func, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from db import Base
import uuid
import json
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

def uuid_str() -> str:
    return str(uuid.uuid4())

"""class PatientORM(Base):
    __tablename__ = "patients"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=uuid_str)
    first_name: Mapped[str] = mapped_column(String(100))
    last_name:  Mapped[str] = mapped_column(String(100))
    date_of_birth: Mapped[Date | None] = mapped_column(Date, nullable=True)
    gender: Mapped[str | None] = mapped_column(String(32), nullable=True)
    phone_number: Mapped[str | None] = mapped_column(String(32), nullable=True)
    email: Mapped[str | None] = mapped_column(String(255), nullable=True)
    address: Mapped[str | None] = mapped_column(Text, nullable=True)
    emergency_contact: Mapped[str | None] = mapped_column(Text, nullable=True)
    condition: Mapped[str | None] = mapped_column(String(255), nullable=True)
    created_at: Mapped[str] = mapped_column(TIMESTAMP, server_default=func.current_timestamp())
    updated_at: Mapped[str | None] = mapped_column(TIMESTAMP, nullable=True, onupdate=func.current_timestamp())
"""

class PatientORM(Base):
    __tablename__ = "patients"

    id: Mapped[str] = mapped_column(String(16), primary_key=True,index=True)
    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    date_of_birth: Mapped[Date | None] = mapped_column(Date, nullable=True)
    gender: Mapped[str | None] = mapped_column(String(32), nullable=True)
    phone_number: Mapped[str | None] = mapped_column(String(32), nullable=True)
    email: Mapped[str | None] = mapped_column(String(255), nullable=True)
    address: Mapped[str | None] = mapped_column(Text, nullable=True)
    emergency_contact: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    condition: Mapped[str | None] = mapped_column(String(255), nullable=True)

    def to_json(self):
        return json.dumps({
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_of_birth": str(self.date_of_birth) if self.date_of_birth else None,
            "gender": self.gender,
            "phone_number": self.phone_number,
            "email": self.email,
            "address": self.address,
            "emergency_contact": self.emergency_contact,
            "condition": self.condition,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        })
