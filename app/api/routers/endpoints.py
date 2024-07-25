from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.params import Depends
from app.api.schemas.dtos import (
    AliadoDTORequest,
    AliadoDTOResponse,
    DragonDTORequest,
    DragonDTOResponse,
    JineteDTORequest,
    JineteDTOResponse,
)
from app.api.models.tables import Dragon, Jinete, Aliado
from app.database.config import SessionLocal, engine

router = APIRouter()


def getDB():
    db = SessionLocal()

    try:
        yield db

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        db.close()


@router.post(
    "/dragones", response_model=DragonDTOResponse, summary="Crea un Dragon en la BD"
)
def addDragon(dragon: DragonDTORequest, db: Session = Depends(getDB())):
    try:
        dragon = Dragon(
            nombres=dragon.nombre,
            edad=dragon.edad,
            altura=dragon.altura,
            numeroVictorias=dragon.numeroVictorias,
        )
        db.add(dragon)
        db.commit()
        db.refresh(dragon)
        return dragon
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=500, detail=error)


@router.get(
    "/dragones",
    response_model=List[DragonDTOResponse],
    summary="Servicio que lista todos los dragones de la BD",
)
def getDragones(db: Session = Depends(getDB)):
    try:
        return db.query(Dragon).all()
    except Exception as error:
        raise HTTPException(status_code=500, detail=error)


@router.get(
    "/dragones/{id}",
    response_model=DragonDTOResponse,
    summary="Obtiene un Dragon por su ID",
)
def getDragonById(id: int, db: Session = Depends(getDB)):
    try:
        return db.query(Dragon).filter(Dragon.id == id).first()
    except Exception as error:
        raise HTTPException(status_code=500, detail=error)


@router.put("/dragones/{id}")
def updateDragon(id: int, dragon: DragonDTORequest, db: Session = Depends(getDB)):
    dragonToUpdate = getDragonById(id, db)
    if dragonToUpdate is None:
        raise HTTPException(status_code=404, detail="Dragon not found")
    for key, value in dragon.dict().items():
        setattr(dragonToUpdate, key, value)
    db.commit()
    db.refresh(dragonToUpdate)


@router.delete("/dragones/{id}")
def deleteDragon(id: int, db: Session = Depends(getDB)):
    dragonToDelete = getDragonById(id, db)
    if dragonToDelete is None:
        raise HTTPException(status_code=404, detail="Dragon not found")
    db.delete(dragonToDelete)
    db.commit()


@router.post(
    "/jinetes", response_model=JineteDTOResponse, summary="Crea un Jinete en la BD"
)
def addJinete(jinete: JineteDTORequest, db: Session = Depends(getDB())):
    try:
        jinete = Jinete(
            nombres=jinete.nombre,
            edad=jinete.edad,
            altura=jinete.altura,
            numeroVictorias=jinete.numeroVictorias,
        )
        db.add(jinete)
        db.commit()
        db.refresh(jinete)
        return jinete
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=500, detail=error)


@router.get(
    "/jinetes",
    response_model=List[JineteDTOResponse],
    summary="Servicio que lista todos los jinetes de la BD",
)
def getJinetes(db: Session = Depends(getDB)):
    try:
        return db.query(Jinete).all()
    except Exception as error:
        raise HTTPException(status_code=500, detail=error)


@router.get(
    "/jinetes/{id}",
    response_model=JineteDTOResponse,
    summary="Obtiene un Jinete por su ID",
)
def getJineteById(id: int, db: Session = Depends(getDB)):
    try:
        return db.query(Jinete).filter(Jinete.id == id).first()
    except Exception as error:
        raise HTTPException(status_code=500, detail=error)


@router.put("/jinetes/{id}")
def updateJinete(id: int, jinete: JineteDTORequest, db: Session = Depends(getDB)):
    jineteToUpdate = getJineteById(id, db)
    if jineteToUpdate is None:
        raise HTTPException(status_code=404, detail="Jinete not found")
    for key, value in jinete.dict().items():
        setattr(jineteToUpdate, key, value)
    db.commit()
    db.refresh(jineteToUpdate)


@router.delete("/jinetes/{id}")
def deleteJinete(id: int, db: Session = Depends(getDB)):
    jineteToDelete = getJineteById(id, db)
    if jineteToDelete is None:
        raise HTTPException(status_code=404, detail="Jinete not found")
    db.delete(jineteToDelete)
    db.commit()


@router.post(
    "/aliados", response_model=AliadoDTOResponse, summary="Crea un Aliado en la BD"
)
def addAliado(aliado: AliadoDTORequest, db: Session = Depends(getDB())):
    try:
        aliado = Aliado(
            nombres=aliado.nombre,
            edad=aliado.edad,
            altura=aliado.altura,
            numeroVictorias=aliado.numeroVictorias,
        )
        db.add(aliado)
        db.commit()
        db.refresh(aliado)
        return aliado
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=500, detail=error)


@router.get(
    "/aliados",
    response_model=List[AliadoDTOResponse],
    summary="Servicio que lista todos los aliados de la BD",
)
def getAliados(db: Session = Depends(getDB)):
    try:
        return db.query(Aliado).all()
    except Exception as error:
        raise HTTPException(status_code=500, detail=error)


@router.get(
    "/aliados/{id}",
    response_model=AliadoDTOResponse,
    summary="Obtiene un Aliado por su ID",
)
def getAliadoById(id: int, db: Session = Depends(getDB)):
    try:
        return db.query(Aliado).filter(Aliado.id == id).first()
    except Exception as error:
        raise HTTPException(status_code=500, detail=error)


@router.put("/aliados/{id}")
def updateAliado(id: int, aliado: AliadoDTORequest, db: Session = Depends(getDB)):
    aliadoToUpdate = getAliadoById(id, db)
    if aliadoToUpdate is None:
        raise HTTPException(status_code=404, detail="Aliado not found")
    for key, value in aliado.dict().items():
        setattr(aliadoToUpdate, key, value)
    db.commit()
    db.refresh(aliadoToUpdate)


@router.delete("/aliados/{id}")
def deleteAliado(id: int, db: Session = Depends(getDB)):
    aliadoToDelete = getAliadoById(id, db)
    if aliadoToDelete is None:
        raise HTTPException(status_code=404, detail="Aliado not found")
    db.delete(aliadoToDelete)
    db.commit()
