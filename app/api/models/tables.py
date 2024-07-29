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
    fk_jinete = Column(Integer, ForeignKey("jinete.id"))
    jinete = relationship("Jinete", back_populates="aliados")


class Dragon(Base):
    __tablename__ = "dragon"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255))
    edad = Column(Integer)
    altura = Column(Float)
    numeroVictorias = Column(Integer)
    fk_jinete = Column(Integer, ForeignKey("jinete.id"))
    jinete = relationship("Jinete", back_populates="dragones")


class Jinete(Base):
    __tablename__ = "jinete"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255))
    edad = Column(Integer)
    fechaMontura = Column(Date)
    dragones = relationship("Dragon", back_populates="jinete")
    aliados = relationship("Aliado", back_populates="jinete")
