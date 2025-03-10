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

init_mokykla_database()

prideti_mokykla("Vilniaus progimnazija", "Vilniaus g. 10", 500)
prideti_mokykla("Kauno gimnazija", "Kauno g. 5", 800)

def print_all_mokyklos():
    with sqlite3.connect('mokykla.db') as conn:
        c = conn.cursor()
        for row in c.execute("SELECT * FROM mokykla"):
            print(row)

print_all_mokyklos()
