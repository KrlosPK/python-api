from pydantic import BaseModel, Field
from datetime import date


class AliadoDTORequest(BaseModel):
    nombre: str
    ubicacion: str
    aporteMonetario: float
    fk_jinete: int

    class Config:
        orm_mode = True


class AliadoDTOResponse(BaseModel):
    id: int
    nombre: str
    ubicacion: str
    aporteMonetario: float
    fk_jinete: int

    class Config:
        orm_mode = True


class DragonDTORequest(BaseModel):
    nombre: str
    edad: int
    altura: float
    numeroVictorias: int
    fk_jinete: int

    class Config:
        orm_mode = True


class DragonDTOResponse(BaseModel):
    id: int
    nombre: str
    edad: int
    altura: float
    numeroVictorias: int
    fk_jinete: int

    class Config:
        orm_mode = True


class JineteDTORequest(BaseModel):
    nombre: str
    edad: int
    fechaMontura: date

    class Config:
        orm_mode = True


class JineteDTOResponse(BaseModel):
    id: int
    nombre: str
    edad: int
    fechaMontura: date

    class Config:
        orm_mode = True
