from sqlalchemy.orm import Session
from src.models.libro import Libro
from src.schemas.libro_sch import LibroCreate

def create_libro(db: Session, libro_data: LibroCreate):
    nuevo = Libro(**libro_data.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def find_libros(db: Session, consulta: str):
    return db.query(Libro).filter(
        (Libro.titulo.ilike(f"%{consulta}%")) | (Libro.autor.ilike(f"%{consulta}%"))
    ).all()

def get_libro(db: Session, libro_id: int):
    return db.query(Libro).filter(Libro.id == libro_id).first()

def update_libro(db: Session, libro_id: int, libro_data: dict):
    libro = db.query(Libro).filter(Libro.id == libro_id).first()
    if not libro:
        return None
    for key, value in libro_data.items():
        if value is not None:
            setattr(libro, key, value)
    db.commit()
    db.refresh(libro)
    return libro

def delete_libro(db: Session, libro_id: int):
    libro = db.query(Libro).filter(Libro.id == libro_id).first()
    if not libro:
        return None
    db.delete(libro)
    db.commit()
    return libro

def get_all_libros(db: Session):
    return db.query(Libro).all()