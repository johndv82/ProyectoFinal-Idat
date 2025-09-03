from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import StaticPool
from src.config import DATABASE_URL

from src.models import Base
# IMPORTAR  modelos
from src.models.cliente import Cliente
from src.models.libro import Libro
from src.models.venta import Venta
from src.models.libroventa import LibroVenta
from src.models.usuario import Usuario

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Crear tablas
Base.metadata.create_all(bind=engine)

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
