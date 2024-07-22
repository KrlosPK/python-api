from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Aliado(Base):
    __tablename__ = "aliado"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    ubicacion = Column(String)
    aporteMonetario = Column(Float)


class Dragon(Base):
    __tablename__ = "dragon"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    edad = Column(Integer)
    altura = Column(Float)
    numeroVictorias = Column(Integer)


class Jinete(Base):
    __tablename__ = "jinete"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    edad = Column(String)
    fechaMontura = Column(Date)
