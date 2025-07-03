from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import date
from typing import Optional

class PetBase(BaseModel):
    nome: str
    especie: str
    raca: Optional[str] = "Desconhecido"
    nascimento: Optional[date] = None
    peso: Optional[float] = None
    imagem: Optional[str] = None
    tutor_email: EmailStr

class PetCreate(PetBase):
    pass

class PetUpdate(BaseModel):
    nome: Optional[str] = None
    especie: Optional[str] = None
    raca: Optional[str] = None
    nascimento: Optional[date] = None
    peso: Optional[float] = None
    imagem: Optional[str] = None

class PetResponse(PetBase):
    id: int
    
    model_config = ConfigDict(from_attributes=True)


# Tutores
class TutorBase(BaseModel):
    email: EmailStr
    nome: str
    senha: str
    telefone: str

class TutorCreate(TutorBase):
    pass

class TutorUpdate(BaseModel):
    email: Optional[EmailStr] = None
    nome: Optional[str] = None
    senha: Optional[str] = None
    telefone: Optional[str] = None

class TutorResponse(TutorBase):
    model_config = ConfigDict(from_attributes=True)

class TutorLogin(BaseModel):
    email: EmailStr
    senha: str