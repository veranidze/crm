from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Base, Lead
from db import engine, SessionLocal
from schemas import LeadIn
from fastapi import Depends
from sqlalchemy.orm import Session
import uuid, datetime

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api/leads")
def create_lead(lead: LeadIn, db: Session = Depends(get_db)):
    new_lead = Lead(
        id=str(uuid.uuid4()),
        name=lead.name,
        email=lead.email,
        phone=lead.phone,
        source=lead.source,
        client_comment=lead.client_comment,
        stage="Новый",
        status="не обработан",
        created_at=datetime.datetime.utcnow(),
    )
    db.add(new_lead)
    db.commit()
    return {"ok": True}
