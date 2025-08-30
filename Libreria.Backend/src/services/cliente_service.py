from sqlalchemy.orm import Session
from src.models.cliente import Cliente
from src.schemas.cliente_sch import ClienteCreate, ClienteUpdate

def crear_cliente(db: Session, cliente_data: ClienteCreate):
    existe = db.query(Cliente).filter(Cliente.email == cliente_data.email).first()
    if existe:
        return None
    nuevo = Cliente(**cliente_data.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def obtener_cliente(db: Session, cliente_id: int):
    return db.query(Cliente).filter(Cliente.id == cliente_id).first()

def eliminar_cliente(db: Session, cliente_id: int):
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    if not cliente:
        return False
    db.delete(cliente)
    db.commit()
    return True

def actualizar_cliente(db: Session, cliente_id: int, datos: ClienteUpdate):
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    if not cliente:
        return None

    cliente.nombres = datos.nombres
    cliente.apellidos = datos.apellidos
    cliente.dni = datos.dni
    cliente.email = datos.email

    db.commit()
    db.refresh(cliente)
    return cliente

def actualizar_cliente_parcial(db: Session, cliente_id: int, cambios: ClienteUpdate):
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    if not cliente:
        return None

    datos = cambios.model_dump(exclude_unset=True)
    for campo, valor in datos.items():
        setattr(cliente, campo, valor)

    db.commit()
    db.refresh(cliente)
    return cliente