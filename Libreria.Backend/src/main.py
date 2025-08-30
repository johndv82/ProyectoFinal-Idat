from fastapi import FastAPI
from src.core.database import engine
from src.models import Base
from src.api import clientes, libros, ventas, auth

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Librería API")

app.include_router(clientes.router)
app.include_router(libros.router)
app.include_router(ventas.router)
app.include_router(auth.router)