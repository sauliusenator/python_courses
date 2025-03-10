import sqlite3

# 1. Sukurti duomenų bazę su dviem lentelėmis
class DatabaseManager:
    def __init__(self, db_name='mokykla.db'):
        self.db_name = db_name
        self.create_tables()

    def create_tables(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.executescript('''
                CREATE TABLE IF NOT EXISTS mokiniai (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    vardas TEXT NOT NULL,
                    pavarde TEXT NOT NULL,
                    klase TEXT NOT NULL,
                    vidurkis REAL CHECK (vidurkis BETWEEN 1 AND 10)
                );

                CREATE TABLE IF NOT EXISTS mokytojai (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    vardas TEXT NOT NULL,
                    pavarde TEXT NOT NULL,
                    dalykas TEXT NOT NULL
                );
            ''')
            conn.commit()

    def execute_query(self, query, params=(), fetchone=False, fetchall=False):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            if fetchone:
                return cursor.fetchone()
            if fetchall:
                return cursor.fetchall()
            conn.commit()

db = DatabaseManager()

# 2. Sukurti OOP klases
class Asmuo:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde

class Mokinys(Asmuo):
    def __init__(self, vardas, pavarde, klase, vidurkis):
        super().__init__(vardas, pavarde)
        self.klase = klase
        self.vidurkis = vidurkis

    def __str__(self):
        return f"{self.vardas} {self.pavarde}, Klasė: {self.klase}, Vidurkis: {self.vidurkis:.2f}"

class Mokytojas(Asmuo):
    def __init__(self, vardas, pavarde, dalykas):
        super().__init__(vardas, pavarde)
        self.dalykas = dalykas

    def __str__(self):
        return f"{self.vardas} {self.pavarde}, Dėsto: {self.dalykas}"

# 3. Dekoratorius funkcijų registracijai
def log_dekoratorius(func):
    def wrapper(*args, **kwargs):
        print(f'Vykdoma operacija: {func.__name__} su parametrais {args}')
        try:
            return func(*args, **kwargs)
        except sqlite3.Error as e:
            print(f'Klaida vykdant {func.__name__}: {e}')
    return wrapper

# 4. Funkcijos duomenų valdymui
@log_dekoratorius
def prideti_mokini(mokinys):
    db.execute_query(
        'INSERT INTO mokiniai (vardas, pavarde, klase, vidurkis) VALUES (?, ?, ?, ?)',
        (mokinys.vardas, mokinys.pavarde, mokinys.klase, mokinys.vidurkis)
    )

@log_dekoratorius
def prideti_mokytoja(mokytojas):
    db.execute_query(
        'INSERT INTO mokytojai (vardas, pavarde, dalykas) VALUES (?, ?, ?)',
        (mokytojas.vardas, mokytojas.pavarde, mokytojas.dalykas)
    )

@log_dekoratorius
def perziureti_visus_mokinius():
    mokiniai = db.execute_query(
        'SELECT vardas, pavarde, klase, vidurkis FROM mokiniai', fetchall=True
    )
    if not mokiniai:
        print('Mokinių sąrašas tuščias.')
        return
    for mokinys in mokiniai:
        print(f'Vardas: {mokinys[0]}, Pavardė: {mokinys[1]}, Klasė: {mokinys[2]}, Vidurkis: {mokinys[3]:.2f}')

@log_dekoratorius
def ieskoti_mokinio(vardas, pavarde):
    mokiniai = db.execute_query(
        'SELECT vardas, pavarde, klase, vidurkis FROM mokiniai WHERE vardas = ? AND pavarde = ?',
        (vardas, pavarde), fetchall=True
    )
    if not mokiniai:
        print('Mokinys nerastas.')
        return
    for mokinys in mokiniai:
        print(f'Vardas: {mokinys[0]}, Pavardė: {mokinys[1]}, Klasė: {mokinys[2]}, Vidurkis: {mokinys[3]:.2f}')

@log_dekoratorius
def atnaujinti_mokinio_klase(mokinys_id, nauja_klase):
    db.execute_query(
        'UPDATE mokiniai SET klase = ? WHERE id = ?',
        (nauja_klase, mokinys_id)
    )

@log_dekoratorius
def istrinti_mokini(mokinys_id):
    db.execute_query(
        'DELETE FROM mokiniai WHERE id = ?',
        (mokinys_id,)
    )

# 5. Iteratorius mokinių sąrašui
class MokiniuIteratorius:
    def __init__(self):
        self.mokiniai = db.execute_query(
            'SELECT vardas, pavarde, klase, vidurkis FROM mokiniai', fetchall=True
        )
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.mokiniai):
            duomenys = self.mokiniai[self.index]
            self.index += 1
            return Mokinys(*duomenys)
        raise StopIteration

# 6. Vartotojo sąsaja
def pasirinkti_veiksma():
    veiksmai = {
        '1': lambda: prideti_mokini(
            Mokinys(
                vardas=input('Mokinio vardas: '),
                pavarde=input('Mokinio pavardė: '),
                klase=input('Mokinio klasė: '),
                vidurkis=float(input('Mokinio vidurkis: '))
            )
        ),
        '2': lambda: prideti_mokytoja(
            Mokytojas(
                vardas=input('Mokytojo vardas: '),
                pavarde=input('Mokytojo pavardė: '),
                dalykas=input('Mokytojo dėstomas dalykas: ')
            )
        ),
        '3': perziureti_visus_mokinius,
        '4': lambda: ieskoti_mokinio(
            vardas=input('Mokinio vardas: '),
            pavarde=input('Mokinio pavardė: ')
        ),
        '5': lambda: atnaujinti_mokinio_klase(
            int(input('Mokinio ID: ')),
            input('Nauja klasė: ')
        ),
        '6': lambda: istrinti_mokini(int(input('Mokinio ID: '))),
        '7': exit
    }

    while True:
        print('\nMokyklos duomenų valdymo sistema')
        print('1. Pridėti mokinį')
        print('2. Pridėti mokytoją')
        print('3. Peržiūrėti visus mokinius')
        print('4. Ieškoti mokinio pagal vardą')
        print('5. Atnaujinti mokinio klasę')
        print('6. Ištrinti mokinį')
        print('7. Išeiti')

        pasirinkimas = input('Pasirinkite veiksmą: ')
        veiksmai.get(pasirinkimas, lambda: print('Neteisingas pasirinkimas!'))()

# 7. Vykdymas
pasirinkti_veiksma()
