from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.schemas.venta_sch import VentaCreate, VentaOut
from src.core.database import get_db
from src.services import venta_service

router = APIRouter(prefix="/ventas", tags=["Ventas"])

@router.post("/", response_model=VentaOut, status_code=201)
def registrar_venta(venta: VentaCreate, db: Session = Depends(get_db)):
    resultado = venta_service.registrar_venta(db, venta)
    if resultado is None:
        raise HTTPException(status_code=400, detail="Stock insuficiente o libro no encontrado")
    return resultado

@router.get("/{cliente_id}", response_model=List[VentaOut])
def obtener_ventas_cliente(cliente_id: int, db: Session = Depends(get_db)):
    venta = venta_service.obtener_ventas_cliente(db, cliente_id)
    if not venta:
        raise HTTPException(status_code=404, detail="Venta no encontrada")
    return venta