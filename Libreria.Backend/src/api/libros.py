from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from src.schemas.libro_sch import LibroCreate, LibroOut, LibroUpdate
from src.core.database import get_db
from src.services import libro_service 

router = APIRouter(prefix="/libros", tags=["Libros"])

@router.post("/", response_model=LibroOut, status_code=201)
def crear_libro(libro: LibroCreate, db: Session = Depends(get_db)):
    return libro_service.create_libro(db, libro)

@router.get("/", response_model=List[LibroOut])
def buscar_libros(q: str = Query(default="", description="Buscar por título o autor"), db: Session = Depends(get_db)):
    if not q:
        return libro_service.get_all_libros(db)
    return libro_service.find_libros(db, q)

@router.get("/", response_model=List[LibroOut])
def listar_libros(db: Session = Depends(get_db)):
    return libro_service.get_all_libros(db)

@router.get("/{libro_id}", response_model=LibroOut)
def obtener_libro(libro_id: int, db: Session = Depends(get_db)):
    libro = libro_service.get_libro(db, libro_id)
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return libro

@router.put("/{libro_id}", response_model=LibroOut)
def actualizar_libro(libro_id: int, libro_in: LibroUpdate, db: Session = Depends(get_db)):
    libro = libro_service.update_libro(db, libro_id, libro_in.dict())
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return libro

@router.delete("/{libro_id}", response_model=LibroOut)
def eliminar_libro(libro_id: int, db: Session = Depends(get_db)):
    libro = libro_service.delete_libro(db, libro_id)
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return libro