from sqlalchemy import Boolean, Column, DateTime, Integer, String, Float
from sqlalchemy.orm import relationship
from src.models import Base
from datetime import datetime

class Libro(Base):
    __tablename__ = "tbl_libros"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(200), nullable=False)
    isbn = Column(String(20), nullable=False, unique=True)
    autor = Column(String(200), nullable=False)
    precio = Column(Float, nullable=False)
    activo = Column(Boolean, default=True)
    fecha_ingreso = Column(DateTime, default=datetime.now)

    ventas = relationship("LibroVenta", back_populates="libro")