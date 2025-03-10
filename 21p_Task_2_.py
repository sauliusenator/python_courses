from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Mokinys(Base):
    __tablename__ = 'mokiniai'

    id = Column(Integer, primary_key=True)
    vardas = Column(String)
    pavarde = Column(String)


class Mokytojas(Base):
    __tablename__ = 'mokytojai'

    id = Column(Integer, primary_key=True)
    vardas = Column(String)
    pavarde = Column(String)


# Sukurkite duomenų bazės variklį
engine = create_engine('sqlite:///mokykla.db')  # Pakeiskite su savo duomenų bazės URL
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def add_student(vardas, pavarde):
    # Patikrinkite, ar mokinys jau egzistuoja
    existing_student = session.query(Mokinys).filter_by(vardas=vardas, pavarde=pavarde).first()
    if existing_student is None:
        new_student = Mokinys(vardas=vardas, pavarde=pavarde)
        session.add(new_student)
        session.commit()
        print(f"Mokinys {vardas} {pavarde} pridėtas.")
    else:
        print(f"Mokinys {vardas} {pavarde} jau egzistuoja.")

def add_teacher(vardas, pavarde):
    new_teacher = Mokytojas(vardas=vardas, pavarde=pavarde)
    session.add(new_teacher)
    session.commit()
    print(f"Mokytojas {vardas} {pavarde} pridėtas.")

# Įterpkite mokinius
add_student("Jonas", "Jonaitis")
add_student("Petras", "Petraitis")
add_student("Ona", "Onaitytė")

# Įterpkite mokytojus
add_teacher("Mantas", "Mantaitis")
add_teacher("Laura", "Lauraitė")

def get_all_students():
    students = session.query(Mokinys).all()
    for student in students:
        print(f"Mokinys: {student.vardas} {student.pavarde}")

def get_all_teachers():
    teachers = session.query(Mokytojas).all()
    for teacher in teachers:
        print(f"Mokytojas: {teacher.vardas} {teacher.pavarde}")

# Išveskite visus mokinius ir mokytojus
get_all_students()
get_all_teachers()