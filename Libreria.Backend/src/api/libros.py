from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List
from src.schemas.libro_sch import LibroCreate, LibroOut
from src.core.database import get_db
from src.services import libro_service 

router = APIRouter(prefix="/libros", tags=["Libros"])

@router.post("/", response_model=LibroOut, status_code=201)
def crear_libro(libro: LibroCreate, db: Session = Depends(get_db)):
    return libro_service.crear_libro(db, libro)

@router.get("/", response_model=List[LibroOut])
def buscar_libros(q: str = Query(default="", description="Buscar por título o autor"), db: Session = Depends(get_db)):
    return libro_service.buscar_libros(db, q)