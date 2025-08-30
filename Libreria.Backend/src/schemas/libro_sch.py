from pydantic import BaseModel
from datetime import datetime

class LibroBase(BaseModel):
    titulo: str
    isbn: str
    autor: str
    precio: float

class LibroCreate(LibroBase):
    pass

class LibroOut(LibroBase):
    id: int
    fecha_ingreso: datetime
    activo: bool

    class Config:
        from_attributes = True