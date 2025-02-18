from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Mokinys(Base):
    __tablename__ = 'mokiniai'
    id = Column(Integer, primary_key=True)
    vardas = Column(String)
    pavarde = Column(String)
    klase = Column(Integer)

class Mokytojas(Base):
    __tablename__ = 'mokytojai'
    id = Column(Integer, primary_key=True)
    vardas = Column(String)
    pavarde = Column(String)

engine = create_engine('sqlite:///mokykla.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

session.add(Mokinys(vardas="Jonas", pavarde="Jonaitis", klase=10))
session.add(Mokinys(vardas="Petras", pavarde="Petraitis", klase=12))
session.add(Mokinys(vardas="Ona", pavarde="Onaitytė", klase=11))
session.add(Mokinys(vardas="Paulina", pavarde="Pavardenė", klase=9))
session.commit()

session.add(Mokytojas(vardas="Mantas", pavarde="Mantaitis"))
session.add(Mokytojas(vardas="Laura", pavarde="Lauraitė"))
session.add(Mokytojas(vardas="Andrius", pavarde="Andrėjus"))
session.commit()

def find_student_by_name(vardas):
    student = session.query(Mokinys).filter_by(vardas=vardas).first()
    if student:
        print(f"Mokinys rastas: {student.vardas} {student.pavarde}, Klasė: {student.klase}")
    else:
        print(f"Mokinys su vardu {vardas} nerastas.")

def find_students_by_lastname_starting_with_p():
    students = session.query(Mokinys).filter(Mokinys.pavarde.like("P%")).all()
    if students:
        print("Mokiniai, kurių pavardė prasideda raide 'P':")
        for student in students:
            print(f"{student.vardas} {student.pavarde}, Klasė: {student.klase}")
    else:
        print("Nėra mokinių, kurių pavardė prasideda raide 'P'.")

def find_teachers_with_name_ending_with_s():
    teachers = session.query(Mokytojas).filter(Mokytojas.vardas.like("%s")).all()
    if teachers:
        print("Mokytojai, kurių vardas baigiasi raide 's':")
        for teacher in teachers:
            print(f"{teacher.vardas} {teacher.pavarde}")
    else:
        print("Nėra mokytojų, kurių vardas baigiasi raide 's'.")

find_student_by_name("Jonas")
find_students_by_lastname_starting_with_p()
find_teachers_with_name_ending_with_s()