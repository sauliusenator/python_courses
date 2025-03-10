from sqlalchemy import Column, create_engine, Integer, String, Float
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///mokykla.db')
Base = declarative_base()

class Mokykla(Base):
    __tablename__ = 'Mokykla'

    id = Column(Integer, primary_key=True)
    vardas = Column(String)
    pavarde = Column(String)
    klase = Column(Integer)



class Mokytojas(Base):
    __tablename__ = 'mokytojas'

    id = Column(Integer, primary_key=True)

    vardas = Column(String)
    pavarde = Column(String)
    dalykas = Column(String)

Base.metadata.create_all(engine)
