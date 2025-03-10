import sqlite3


def init_mokykla_database():
    conn = sqlite3.connect('mokykla.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS mokykla (
        pavadinimas TEXT,
        adresas TEXT,
        mokiniu_skaicius INTEGER
    )
    ''')
    conn.commit()
    conn.close()


def prideti_mokykla(pavadinimas, adresas, mokiniu_skaicius):
    with sqlite3.connect('mokykla.db') as conn:
        c = conn.cursor()
        c.execute("INSERT INTO mokykla (pavadinimas, adresas, mokiniu_skaicius) VALUES (?, ?, ?)",
                  (pavadinimas, adresas, mokiniu_skaicius))
        conn.commit()

def print_mokyklos_duomenys(min_mokiniu_skaicius=0):
    with sqlite3.connect('mokykla.db') as conn:
        c = conn.cursor()
        query = "SELECT * FROM mokykla WHERE mokiniu_skaicius >= ?"
        c.execute(query, (min_mokiniu_skaicius,))

        rows = c.fetchall()
        for row in rows:
            pavadinimas, adresas, mokiniu_skaicius = row
            print(f"Mokykla: {pavadinimas}, Adresas: {adresas}, Mokinių skaičius: {mokiniu_skaicius}")


init_mokykla_database()

print("Visos mokyklos:")
print_mokyklos_duomenys()

print("\nMokyklos su daugiau nei 600 mokinių:")
print_mokyklos_duomenys(600)
