# src/api/v1/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session
from src.core.database import get_db
from src.core.security import hash_password, verify_password
from src.models.usuario import Usuario
from src.schemas.usuario_sch import UsuarioCreate, UsuarioResponse

router = APIRouter(prefix="/auth", tags=["Auth"])
security = HTTPBasic()

@router.post("/register", response_model=UsuarioResponse)
def register(user_in: UsuarioCreate, db: Session = Depends(get_db)):
    user_exist = db.query(Usuario).filter(
        (Usuario.username == user_in.username) | (Usuario.email == user_in.email)
    ).first()
    if user_exist:
        raise HTTPException(status_code=400, detail="Usuario o email ya registrado")

    hashed_pw = hash_password(user_in.password)
    new_user = Usuario(
        username=user_in.username,
        email=user_in.email,
        hashed_password=hashed_pw
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/login")
def login(
    credentials: HTTPBasicCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    user = db.query(Usuario).filter(Usuario.username == credentials.username).first()
    if not user or not verify_password(credentials.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas",
            headers={"WWW-Authenticate": "Basic"},
        )

    return {"message": f"Bienvenido {user.username}", "user_id": user.id}
