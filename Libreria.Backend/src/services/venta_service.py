from sqlalchemy.orm import Session
from src.models.venta import Venta
from src.models.cliente import Cliente
from src.models.libro import Libro
from src.models.libroventa import LibroVenta
from src.models.usuario import Usuario
from src.schemas.venta_sch import VentaCreate, LibroVentaOut, VentaOut
from typing import List, Optional

def registrar_venta(db: Session, venta_data: VentaCreate):
    cliente = db.query(Cliente).filter(Cliente.id == venta_data.cliente_id).first()
    if not cliente:
        usuario = db.query(Usuario).filter(Usuario.id == venta_data.cliente_id).first()
        if not usuario:
            return None

    nueva_venta = Venta(cliente_id=venta_data.cliente_id)
    db.add(nueva_venta)
    db.flush()  # obtener el id antes del commit

    resumen = []

    for item in venta_data.libros:
        libro = db.query(Libro).filter(Libro.id == item.libro_id).first()
        if not libro:
            db.rollback()
            return None

        detalle = LibroVenta(
            venta_id=nueva_venta.id,
            libro_id=libro.id,
            cantidad=item.cantidad
        )
        db.add(detalle)

        resumen.append(LibroVentaOut(
            libro_id=libro.id,
            titulo=libro.titulo,
            cantidad=item.cantidad,
            precio_unitario=libro.precio
        ))

    db.commit()

    return VentaOut(
        id=nueva_venta.id,
        cliente_id=nueva_venta.cliente_id,
        fecha=nueva_venta.fecha,
        libros=resumen
    )

def obtener_ventas_cliente(db: Session, cliente_id: int) -> List[VentaOut]:
    ventas = db.query(Venta).filter(Venta.cliente_id == cliente_id).all()
    if not ventas:
        return []

    resultado = []

    for venta in ventas:
        resumen = []
        for lv in venta.libros:
            resumen.append(LibroVentaOut(
                libro_id=lv.libro.id,
                titulo=lv.libro.titulo,
                cantidad=lv.cantidad,
                precio_unitario=lv.libro.precio
            ))

        resultado.append(VentaOut(
            id=venta.id,
            cliente_id=venta.cliente_id,
            fecha=venta.fecha,
            libros=resumen
        ))

    return resultado