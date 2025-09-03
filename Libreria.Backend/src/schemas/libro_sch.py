from pydantic import BaseModel
from datetime import datetime

class LibroBase(BaseModel):
    titulo: str
    isbn: str
    autor: str
    precio: float
    portada:str
    activo: bool = True

class LibroCreate(LibroBase):
    pass

class LibroUpdate(BaseModel):
    titulo: str | None = None
    isbn: str | None = None
    autor: str | None = None
    precio: float | None = None
    portada:str | None = None
    activo: bool | None = None

class LibroOut(LibroBase):
    id: int
    fecha_ingreso: datetime
    activo: bool

    class Config:
        from_attributes = True