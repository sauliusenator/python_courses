import sqlite3

def create_database():
    conn = sqlite3.connect('mokykla.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS mokiniai (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vardas TEXT NOT NULL,
        pavarde TEXT NOT NULL,
        klase TEXT,
        vidurkis REAL
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS mokytojai (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vardas TEXT NOT NULL,
        pavarde TEXT NOT NULL,
        dalykas TEXT
    )
    ''')
    conn.commit()
    conn.close()

create_database()

class Asmuo:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde

class Mokinys(Asmuo):
    def __init__(self, vardas, pavarde, klase, vidurkis):
        super().__init__(vardas, pavarde)
        self.klase = klase
        self.vidurkis = vidurkis


class Mokytojas(Asmuo):
    def __init__(self, vardas, pavarde, dalykas):
        super().__init__(vardas, pavarde)
        self.dalykas = dalykas


def log_operation(func):
    def wrapper(*args, **kwargs):
        print("Vykdoma operacija...")
        return func(*args, **kwargs)

    return wrapper


class Mokykla:
    def __init__(self):
        self.conn = sqlite3.connect('mokykla.db')
        self.cursor = self.conn.cursor()

    @log_operation
    def add_student(self, mokinys):
        self.cursor.execute('''
        INSERT INTO mokiniai (vardas, pavarde, klase, vidurkis) VALUES (?, ?, ?, ?)
        ''', (mokinys.vardas, mokinys.pavarde, mokinys.klase, mokinys.vidurkis))
        self.conn.commit()

    @log_operation
    def update_student(self, student_id, klase=None, vidurkis=None):
        if klase:
            self.cursor.execute('''
            UPDATE mokiniai SET klase = ? WHERE id = ?
            ''', (klase, student_id))
        if vidurkis is not None:
            self.cursor.execute('''
            UPDATE mokiniai SET vidurkis = ? WHERE id = ?
            ''', (vidurkis, student_id))
        self.conn.commit()

    @log_operation
    def delete_student(self, student_id):
        self.cursor.execute('''
        DELETE FROM mokiniai WHERE id = ?
        ''', (student_id,))
        self.conn.commit()

    @log_operation
    def find_student(self, vardas, pavarde):
        self.cursor.execute('''
        SELECT * FROM mokiniai WHERE vardas = ? AND pavarde = ?
        ''', (vardas, pavarde))
        return self.cursor.fetchall()

    @log_operation
    def list_students(self):
        self.cursor.execute('SELECT * FROM mokiniai')
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()


class StudentIterator:
    def __init__(self, students):
        self._students = students
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._students):
            student = self._students[self._index]
            self._index += 1
            return student
        else:
            raise StopIteration


def test_system():
    mokykla = Mokykla()

    # Pridėti mokinius
    mokinys1 = Mokinys("Jonas", "Jonaitis", "10A", 8.5)
    mokinys2 = Mokinys("Petras", "Petraitis", "10B", 7.0)

    print("Pridedu mokinius į sistemą...")
    mokykla.add_student(mokinys1)
    mokykla.add_student(mokinys2)

    print("\nVisi mokiniai sistemoje:")
    mokiniai = mokykla.list_students()
    for mokinys in StudentIterator(mokiniai):
        print(
            f"ID: {mokinys[0]}, Vardas: {mokinys[1]}, Pavardė: {mokinys[2]}, Klasė: {mokinys[3]}, Vidurkis: {mokinys[4]}")

    mokykla.close()


if __name__ == "__main__":
    test_system()