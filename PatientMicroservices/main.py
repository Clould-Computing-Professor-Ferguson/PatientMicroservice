from fastapi import FastAPI, Depends, HTTPException, status, Request, Response
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from db import get_db, Base, engine
from models.models import PatientORM
from models.patient import PatientCreate, PatientUpdate, PatientRead
from fastapi import Request, Response, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import Query
from typing import Optional

app = FastAPI(title="PatientMicroservice API", version="1.0.0")

@app.on_event("startup")
def create_tables():
    Base.metadata.create_all(bind=engine)


@app.post("/patients", response_model=PatientRead, status_code=status.HTTP_201_CREATED)
def create_patient(payload: PatientCreate, db: Session = Depends(get_db)):
    row = PatientORM(**payload.model_dump())
    db.add(row)
    db.commit()
    db.refresh(row)
    return row

@app.get("/patients", response_model=list[PatientRead])
def list_patients(
    first_name: Optional[str] = Query(None, description="Filter by patient name"),
    last_name: Optional[str] = Query(None, description="Filter by patient name"),
    gender: Optional[str] = Query(None, description="Filter by patient name"),
    limit: int = 10,
    offset: int = 0,
    db: Session = Depends(get_db)
):
    return (
        db.query(PatientORM)
        .order_by(PatientORM.created_at)  # optional, but best practice
        .limit(limit)
        .offset(offset)
        .all()
    )

@app.get("/patients/{patient_id}", response_model=None)
def get_patient(
    patient_id: str,
    request: Request,
    db: Session = Depends(get_db)
):
    row = db.query(PatientORM).get(patient_id)
    if not row:
        raise HTTPException(status_code=404, detail="Patient not found")

    timestamp = (
        row.updated_at.timestamp()
        if row.updated_at
        else row.created_at.timestamp()
    )
    etag_value = f'W/"{timestamp}"'

    client_etag = request.headers.get("if-none-match")

    if client_etag == etag_value:
        return Response(status_code=304)

    response = JSONResponse(
        content=jsonable_encoder(PatientRead.model_validate(row))
    )
    response.headers["ETag"] = etag_value
    return response


@app.put("/patients/{patient_id}", response_model=PatientRead)
def update_patient(patient_id: str, payload: PatientUpdate, db: Session = Depends(get_db)):
    row = db.query(PatientORM).get(patient_id)
    if not row:
        raise HTTPException(404, "Patient not found")
    for k, v in payload.model_dump(exclude_unset=True).items():
        setattr(row, k, v)
    db.commit()
    db.refresh(row)
    return row

@app.delete("/patients/{patient_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_patient(patient_id: str, db: Session = Depends(get_db)):
    row = db.query(PatientORM).get(patient_id)
    if not row:
        raise HTTPException(404, "Patient not found")
    db.delete(row)
    db.commit()
    return None