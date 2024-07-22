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


@router.post("/dragon", response_model=DragonDTOResponse)
def addDragoin(dragon: DragonDTORequest, db: Session = Depends(getDB)):
    dragon = Dragon(**dragon.dict())
    db.add(dragon)
    db.commit()
    db.refresh(dragon)


@router.get("/dragon", response_model=List[DragonDTOResponse])
def getDragones(db: Session = Depends(getDB)):
    return db.query(Dragon).all()


@router.get("/dragon/{id}", response_model=DragonDTOResponse)
def getDragonById(id: int, db: Session = Depends(getDB)):
    return db.query(Dragon).filter(Dragon.id == id).first()


@router.put("/dragon/{id}")
def updateDragon(id: int, dragon: DragonDTORequest, db: Session = Depends(getDB)):
    dragonToUpdate = getDragonById(id, db)
    if dragonToUpdate is None:
        raise HTTPException(status_code=404, detail="Dragon not found")
    for key, value in dragon.dict().items():
        setattr(dragonToUpdate, key, value)
    db.commit()
    db.refresh(dragonToUpdate)


@router.delete("/dragon/{id}")
def deleteDragon(id: int, db: Session = Depends(getDB)):
    dragonToDelete = getDragonById(id, db)
    if dragonToDelete is None:
        raise HTTPException(status_code=404, detail="Dragon not found")
    db.delete(dragonToDelete)
    db.commit()
