from pydantic import BaseModel, EmailStr

class UsuarioBase(BaseModel):
    username: str
    email: EmailStr

class UsuarioCreate(UsuarioBase):
    password: str

class UsuarioResponse(UsuarioBase):
    id: int
    activo: bool

    class Config:
        from_attributes = True
