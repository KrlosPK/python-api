from pydantic import BaseModel, Field
from datetime import date


class AliadoDTORequest(BaseModel):
    nombre: str
    ubicacion: str
    aporteMonetario: float

    class Config:
        orm_mode = True


class AliadoDTOResponse(BaseModel):
    id: int
    nombre: str
    ubicacion: str
    aporteMonetario: float

    class Config:
        orm_mode = True


class DragonDTORequest(BaseModel):
    nombre: str
    edad: int
    altura: float
    numeroVictorias: int

    class Config:
        orm_mode = True


class DragonDTOResponse(BaseModel):
    id: int
    nombre: str
    edad: int
    altura: float
    numeroVictorias: int

    class Config:
        orm_mode = True


class JineteDTORequest(BaseModel):
    nombre: str
    edad: str
    fechaMontura: date

    class Config:
        orm_mode = True


class JineteDTOResponse(BaseModel):
    id: int
    nombre: str
    edad: str
    fechaMontura: date

    class Config:
        orm_mode = True
