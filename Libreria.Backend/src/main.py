from fastapi import FastAPI
from src.core.database_sqlite import engine
from src.models import Base
from src.api import clientes, libros, ventas, auth
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Librería API")


# habilitamos CORS
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://libreriaapp.netlify.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(clientes.router)
app.include_router(libros.router)
app.include_router(ventas.router)
app.include_router(auth.router)