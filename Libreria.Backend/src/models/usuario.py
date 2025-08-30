from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from src.models import Base

class Usuario(Base):
    __tablename__ = "tbl_usuarios"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(150), unique=True, index=True, nullable=False)
    hashed_password = Column(String(200), nullable=False)
    activo = Column(Boolean, default=True)
    fecha_registro = Column(DateTime, default=datetime.now)
