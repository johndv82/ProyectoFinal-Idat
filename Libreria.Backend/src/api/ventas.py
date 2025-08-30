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

@router.get("/{venta_id}", response_model=VentaOut)
def obtener_venta(venta_id: int, db: Session = Depends(get_db)):
    venta = venta_service.obtener_venta(db, venta_id)
    if not venta:
        raise HTTPException(status_code=404, detail="Venta no encontrada")
    return venta