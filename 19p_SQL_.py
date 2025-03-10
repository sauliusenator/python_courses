import sqlite3

def init_database():
    conn = sqlite3.connect('pavyzdys.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS studentai (
        vardas TEXT,
        pavarde TEXT,
        klase INTEGER
    )
    ''')
    conn.commit()
    conn.close()

def append_to_studentai(vardas, pavarde, klase):
    with sqlite3.connect('pavyzdys.db') as conn:
        c = conn.cursor()
        c.execute("INSERT INTO studentai (vardas, pavarde, klase) VALUES (?, ?, ?)", (vardas, pavarde, klase))

def print_all_studentai_rows():
    with sqlite3.connect('pavyzdys.db') as conn:
        c = conn.cursor()
        for row in c.execute("SELECT * FROM studentai"):
            print(row)

def print_all_studentai_names():
    with sqlite3.connect('pavyzdys.db') as conn:
        c = conn.cursor()
        for row in c.execute("SELECT vardas FROM studentai"):
            print(row)

def print_all_studentai_by_klase(klase):
    with sqlite3.connect('pavyzdys.db') as conn:
        c = conn.cursor()
        for row in c.execute("SELECT * FROM studentai WHERE klase = ?", (klase,)):
            print(row)

# Pirmiausia inicializuojame duomenų bazę (sukuriama lentelė)
init_database()

# Įrašome kelis studentus
append_to_studentai('John', 'Johnaitis', 11)
append_to_studentai('Gitanas', 'Nauseda', 11)
append_to_studentai('Dalia', 'Grybauskaite', 12)

# Išvedame visus studentus
print("Visi studentai:")
print_all_studentai_rows()

# Išvedame tik studentus pagal klasę 11
print("\nStudentai, klasė 11:")
print_all_studentai_by_klase(11)

# Išvedame tik studentų vardus
print("\nStudentų vardai:")
print_all_studentai_names()

# Išvedame studentus pagal klasę 10 (nėra tokių, todėl nieko nerodys)
print("\nStudentai, klasė 10:")
print_all_studentai_by_klase(10)

#------------------------
def change_klase_by_name(klase, vardas):
    with sqlite3.connect('pavyzdys.db') as conn:
        c = conn.cursor()
        c.execute('UPDATE studentai SET klase = ? WHERE vardas = ?', (klase, vardas,))

def remove_row_by_name(vardas):
    with sqlite3.connect('pavyzdys.db') as conn:
        c = conn.cursor()
        c.execute('DELE FROM studentai')


def delete_all_rows():
    with sqlite3.connect('pavyzdys.db') as conn:
        c = conn.cursor()
        c.execute('DELETE FROM studentai')

delete_all_rows()
# change_klase_by_name(8, 'Jonas')
print_all_studentai_rows()