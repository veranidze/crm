from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, Text

Base = declarative_base()

class Lead(Base):
    __tablename__ = "leads"
    id = Column(String, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    source = Column(String)
    client_comment = Column(Text)
    status = Column(String)
    stage = Column(String)
    created_at = Column(DateTime)
