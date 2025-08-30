from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.models import Base

class Cliente(Base):
    __tablename__ = "tbl_clientes"

    id = Column(Integer, primary_key=True, index=True)
    nombres = Column(String(150), nullable=False)
    apellidos = Column(String(150), nullable=False)
    dni = Column(String(8), nullable=False, unique=True)
    email = Column(String(150), unique=True, index=True, nullable=False)

    ventas = relationship("Venta", back_populates="cliente")