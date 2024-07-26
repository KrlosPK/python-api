from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Aliado(Base):
    __tablename__ = "aliado"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255))
    ubicacion = Column(String(255))
    aporteMonetario = Column(Float)


class Dragon(Base):
    __tablename__ = "dragon"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255))
    edad = Column(Integer)
    altura = Column(Float)
    numeroVictorias = Column(Integer)


class Jinete(Base):
    __tablename__ = "jinete"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255))
    edad = Column(String(255))
    fechaMontura = Column(Date)
