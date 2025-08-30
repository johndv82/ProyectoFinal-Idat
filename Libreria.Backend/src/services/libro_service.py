from sqlalchemy.orm import Session
from src.models.libro import Libro
from src.schemas.libro_sch import LibroCreate

def crear_libro(db: Session, libro_data: LibroCreate):
    nuevo = Libro(**libro_data.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def buscar_libros(db: Session, consulta: str):
    return db.query(Libro).filter(
        (Libro.titulo.ilike(f"%{consulta}%")) | (Libro.autor.ilike(f"%{consulta}%"))
    ).all()

def obtener_libro(db: Session, libro_id: int):
    return db.query(Libro).filter(Libro.id == libro_id).first()