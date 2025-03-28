from pydantic import BaseModel

class LeadIn(BaseModel):
    name: str
    email: str
    phone: str
    source: str
    client_comment: str
