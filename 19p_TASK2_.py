import sqlite3

def init_databse():
conn = sqlite3.connect('mokykla.db')
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXIST mokykla (
PAVADINIMAS TEXT,
ADRESAS TEXT,
MOJINIU_SKAICIUS INTEGER)
''')

conn.commit()
conn.close()

def append_to_studentai():
    with (sqlite3.connect('mokykla.db')  as conn):
        c = conn.cursor(
        c.execute("INSERT INTO studentai (vardas, pavarde, klase) VALUES (?, ?, ?)""")

def print_all_studentai_rows():
    with (sqlite3.connect('mokykla.db') as conn):
        c = conn.cursor()
        for row in conn.execute("SELECT * From"):
            print(row)


append_to_studentai('Tomas', 'Tomaitis' 10)
append_to_studentai('Jonas', 'Jonaitis', 10)
append_to_studentai('Tomas', 'Tomaitis' 10)
print_all_rows()