from mylib import projektai, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()


pavadinimas = input("Įveskite projekto pavadinimą: ")
kaina = float(input('Įveskite kainą: '))

row_object = projektai(pavadinimas=pavadinimas, kaina=kaina)
session.add(row_object)
session.commit()

all_row = session.query(projektai).all()

for row in all_rows:
    print(row)
