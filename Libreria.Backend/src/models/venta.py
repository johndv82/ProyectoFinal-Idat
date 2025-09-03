from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from src.models import Base

class Venta(Base):
    __tablename__ = "tbl_ventas"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    cliente_id = Column(Integer, ForeignKey("tbl_clientes.id"), nullable=False)
    fecha = Column(DateTime, default=datetime.now)

    cliente = relationship("Cliente", back_populates="ventas")
    libros = relationship("LibroVenta", back_populates="venta")