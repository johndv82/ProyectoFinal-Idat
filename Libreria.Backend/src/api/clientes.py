from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from src.schemas.cliente_sch import ClienteCreate, ClienteOut, ClienteUpdate
from src.core.database import get_db
from src.services import cliente_service

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.post("/", response_model=ClienteOut, status_code=201)
def crear_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    nuevo = cliente_service.crear_cliente(db, cliente)
    if not nuevo:
        raise HTTPException(status_code=400, detail="Email ya registrado.")
    return nuevo

@router.get("/{cliente_id}", response_model=ClienteOut)
def obtener_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente = cliente_service.obtener_cliente(db, cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado.")
    return cliente

@router.delete("/{cliente_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_cliente(cliente_id:int, db:Session = Depends(get_db)):
    eliminado = cliente_service.eliminar_cliente(db, cliente_id)
    if not eliminado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cliente con id {cliente_id} no encontrado"
        )
    return

@router.put("/{cliente_id}", response_model=ClienteOut)
def actualizar_cliente(cliente_id: int, datos: ClienteUpdate, db: Session = Depends(get_db)):
    cliente = cliente_service.actualizar_cliente(db, cliente_id, datos)
    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cliente con id {cliente_id} no encontrado"
        )
    return cliente

@router.patch("/{cliente_id}", response_model=ClienteOut)
def actualizar_cliente_parcial(cliente_id: int, cambios: ClienteUpdate, db: Session = Depends(get_db)):
    cliente = cliente_service.actualizar_cliente_parcial(db, cliente_id, cambios)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente