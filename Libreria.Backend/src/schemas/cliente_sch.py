from typing import Optional
from pydantic import BaseModel, EmailStr

class ClienteBase(BaseModel):
    nombres: str
    apellidos: str
    dni: str
    email: EmailStr

class ClienteCreate(ClienteBase):
    pass

class ClienteOut(ClienteBase):
    id: int

    class Config:
        from_attributes = True

class ClienteUpdate(BaseModel):
    nombres: Optional[str] = None
    apellidos: Optional[str] = None
    dni: Optional[str] = None
    email: Optional[EmailStr] = None