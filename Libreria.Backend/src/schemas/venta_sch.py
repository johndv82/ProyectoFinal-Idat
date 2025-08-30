from typing import List
from pydantic import BaseModel
from datetime import datetime

class LibroEnVenta(BaseModel):
    libro_id: int
    cantidad: int

class VentaCreate(BaseModel):
    cliente_id: int
    libros: List[LibroEnVenta]

class LibroVentaOut(BaseModel):
    libro_id: int
    titulo: str
    cantidad: int
    precio_unitario: float

class VentaOut(BaseModel):
    id: int
    cliente_id: int
    fecha: datetime
    libros: List[LibroVentaOut]

    class Config:
        from_attributes = True