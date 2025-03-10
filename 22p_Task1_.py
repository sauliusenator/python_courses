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

existing_student = session.query(Mokinys).filter_by(vardas="Jonas", pavarde="Jonaitis").first()
if existing_student is None:
    new_student = Mokinys(vardas="Jonas", pavarde="Jonaitis", klase=10)
    session.add(new_student)
    session.commit()
    print("Mokinys Jonas Jonaitis pridėtas.")

existing_student = session.query(Mokinys).filter_by(vardas="Petras", pavarde="Petraitis").first()
if existing_student is None:
    new_student = Mokinys(vardas="Petras", pavarde="Petraitis", klase=12)
    session.add(new_student)
    session.commit()
    print("Mokinys Petras Petraitis pridėtas.")

existing_student = session.query(Mokinys).filter_by(vardas="Ona", pavarde="Onaitytė").first()
if existing_student is None:
    new_student = Mokinys(vardas="Ona", pavarde="Onaitytė", klase=11)
    session.add(new_student)
    session.commit()
    print("Mokinys Ona Onaitytė pridėta.")

new_teacher = Mokytojas(vardas="Mantas", pavarde="Mantaitis")
session.add(new_teacher)
session.commit()
print("Mokytojas Mantas Mantaitis pridėtas.")

new_teacher = Mokytojas(vardas="Laura", pavarde="Lauraitė")
session.add(new_teacher)
session.commit()
print("Mokytojas Laura Lauraitė pridėta.")

students = session.query(Mokinys).all()
print("Visi mokiniai:")
for student in students:
    print(f"Mokinys: {student.vardas} {student.pavarde}, Klasė: {student.klase}")

teachers = session.query(Mokytojas).all()
print("Visi mokytojai:")
for teacher in teachers:
    print(f"Mokytojas: {teacher.vardas} {teacher.pavarde}")

student_id_to_delete = 1
student = session.query(Mokinys).filter_by(id=student_id_to_delete).first()
if student:
    session.delete(student)
    session.commit()
    print(f"Mokinys su ID {student_id_to_delete} buvo pašalintas.")
else:
    print(f"Mokinys su ID {student_id_to_delete} nerastas.")

teacher_id_to_delete = 1
teacher = session.query(Mokytojas).filter_by(id=teacher_id_to_delete).first()
if teacher:
    session.delete(teacher)
    session.commit()
    print(f"Mokytojas su ID {teacher_id_to_delete} buvo pašalintas.")
else:
    print(f"Mokytojas su ID {teacher_id_to_delete} nerastas.")

graduated_students = session.query(Mokinys).filter_by(klase=12).all()
for student in graduated_students:
    session.delete(student)
session.commit()
print("Ištrinti visi mokiniai, kurie baigė mokyklą (12 klasė).")

students = session.query(Mokinys).all()
print("Visi mokiniai po trynimo:")
for student in students:
    print(f"Mokinys: {student.vardas} {student.pavarde}, Klasė: {student.klase}")