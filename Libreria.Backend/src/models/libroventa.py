from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.models import Base

class LibroVenta(Base):
    __tablename__ = "tbl_libro_ventas"

    id = Column(Integer, primary_key=True, index=True)
    venta_id = Column(Integer, ForeignKey("tbl_ventas.id"), nullable=False)
    libro_id = Column(Integer, ForeignKey("tbl_libros.id"), nullable=False)
    cantidad = Column(Integer, nullable=False)

    venta = relationship("Venta", back_populates="libros")
    libro = relationship("Libro", back_populates="ventas")