from __future__ import annotations

from typing import Optional
from uuid import UUID, uuid4
from datetime import date, datetime
from pydantic import BaseModel, Field, EmailStr


class PatientBase(BaseModel):
    """
    Base patient schema shared across creation, reading, and updating.
    """

    id: str = Field(
        description="Unique patient ID.",
        json_schema_extra={"Columbia UNI (email prefix)"},
    )

    first_name: str = Field(
        ...,
        description="Patient’s given name.",
        json_schema_extra={"example": "John"},
    )
    last_name: str = Field(
        ...,
        description="Patient’s family name.",
        json_schema_extra={"example": "Doe"},
    )
    date_of_birth: Optional[date] = Field(
        None,
        description="Patient’s date of birth (YYYY-MM-DD).",
        json_schema_extra={"example": "1985-04-12"},
    )
    gender: Optional[str] = Field(
        None,
        description="Patient’s gender (e.g., male, female, non-binary, other).",
        json_schema_extra={"example": "male"},
    )
    phone_number: Optional[str] = Field(
        None,
        description="Primary contact number for the patient.",
        json_schema_extra={"example": "+1-555-123-4567"},
    )
    email: Optional[EmailStr] = Field(
        None,
        description="Patient’s email address for contact and notifications.",
        json_schema_extra={"example": "john.doe@example.com"},
    )
    address: Optional[str] = Field(
        None,
        description="Full mailing address or residence of the patient.",
        json_schema_extra={"example": "123 Main St, New York, NY 10001"},
    )
    emergency_contact: Optional[str] = Field(
        None,
        description="Emergency contact (name and relationship).",
        json_schema_extra={"example": "Jane Doe (Spouse)"},
    )

    # 🆕 Add condition
    condition: Optional[str] = Field(
        None,
        description="Current condition, symptoms, or medical notes.",
        json_schema_extra={"example": "High fever and persistent cough"},
    )

    model_config = {
        "title": "PatientBase",
        "description": "Base schema for patient information used throughout the PatientMicroservice.",
        "json_schema_extra": {
            "examples": [
                {
                    "first_name": "John",
                    "last_name": "Doe",
                    "date_of_birth": "1985-04-12",
                    "gender": "male",
                    "phone_number": "+1-555-123-4567",
                    "email": "john.doe@example.com",
                    "address": "123 Main St, New York, NY 10001",
                    "emergency_contact": "Jane Doe (Spouse)",
                    "condition": "High fever and cough",
                },
                {
                    "first_name": "Alice",
                    "last_name": "Nguyen",
                    "gender": "female",
                    "email": "alice.nguyen@healthcare.org",
                    "condition": "Chest pain",
                },
            ]
        },
    }


class PatientCreate(PatientBase):
    """Fields required when creating a new patient."""

    model_config = {
        "title": "PatientCreate",
        "description": "Schema for creating a new patient record via POST /patients.",
        "json_schema_extra": {
            "example": {
                "first_name": "John",
                "last_name": "Doe",
                "gender": "male",
                "email": "john.doe@example.com",
                "phone_number": "+1-555-123-4567",
                "address": "123 Main St, New York, NY 10001",
                "emergency_contact": "Jane Doe (Spouse)",
                "condition": "High fever for 2 days",
            }
        },
    }


class PatientUpdate(BaseModel):
    """All fields optional to allow partial updates."""
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    date_of_birth: Optional[date] = None
    gender: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[EmailStr] = None
    address: Optional[str] = None
    emergency_contact: Optional[str] = None
    condition: Optional[str] = None  

    model_config = {
        "title": "PatientUpdate",
        "description": "Schema for updating an existing patient record via PUT or PATCH.",
        "json_schema_extra": {
            "example": {
                "email": "john.new@example.com",
                "phone_number": "+1-555-987-6543",
                "address": "456 Park Ave, Brooklyn, NY 11201",
                "condition": "Symptoms improving after medication",
            }
        },
    }


class PatientRead(PatientBase):
    """Returned when reading patient data."""

    id: UUID = Field(default_factory=str)
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Record creation timestamp (UTC).")
    updated_at: Optional[datetime] = Field(None, description="Last update timestamp (UTC).")

    model_config = {
        "from_attributes": True,
        "title": "PatientRead",
        "description": "Schema for patient data returned from the API (GET endpoints).",
        "json_schema_extra": {
            "example": {
                "id": "550e8400-e29b-41d4-a716-446655440000",
                "first_name": "John",
                "last_name": "Doe",
                "gender": "male",
                "email": "john.doe@example.com",
                "phone_number": "+1-555-123-4567",
                "address": "123 Main St, New York, NY 10001",
                "emergency_contact": "Jane Doe (Spouse)",
                "condition": "High fever and cough",
                "created_at": "2025-10-17T14:32:00Z",
                "updated_at": "2025-10-18T09:15:00Z",
            }
        },
    }
