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

engine = create_engine('sqlite:///mokykla.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

session.add(Mokinys(vardas="Jonas", pavarde="Jonaitis", klase=10))
session.add(Mokinys(vardas="Petras", pavarde="Petraitis", klase=12))
session.add(Mokinys(vardas="Ona", pavarde="Onaitytė", klase=11))
session.add(Mokinys(vardas="Paulina", pavarde="Pavardenė", klase=9))
session.add(Mokinys(vardas="Tomas", pavarde="Tomaitis", klase=10))
session.add(Mokinys(vardas="Eglė", pavarde="Eglaitė", klase=12))
session.commit()

def print_students_sorted_by_class():
    students = session.query(Mokinys).order_by(Mokinys.klase).all()
    print("Mokiniai pagal klasę (didėjančia tvarka):")
    for student in students:
        print(f"{student.vardas} {student.pavarde}, Klasė: {student.klase}")

def count_students_in_each_class():
    class_counts = {}
    students = session.query(Mokinys).all()
    for student in students:
        if student.klase in class_counts:
            class_counts[student.klase] += 1
        else:
            class_counts[student.klase] = 1
    print("Mokinių skaičius kiekvienoje klasėje:")
    for klasė, count in class_counts.items():
        print(f"Klasė {klasė}: {count} mokinių")

def calculate_average_students_per_class():
    class_counts = {}
    students = session.query(Mokinys).all()
    for student in students:
        if student.klase in class_counts:
            class_counts[student.klase] += 1
        else:
            class_counts[student.klase] = 1
    total_students = sum(class_counts.values())
    total_classes = len(class_counts)
    average = total_students / total_classes if total_classes > 0 else 0
    print(f"Vidutinis mokinių skaičius klasėje: {average:.2f}")

print_students_sorted_by_class()
count_students_in_each_class()
calculate_average_students_per_class()