import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date, ForeignKey, exc
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from datetime import datetime, timedelta

DATABASE_URL = "sqlite:///library.db"
engine = create_engine(DATABASE_URL, echo=False)

Base = declarative_base()

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True, nullable=False)
    author_first_name = Column(String, nullable=False)
    author_last_name = Column(String, nullable=False)
    year_published = Column(Integer)
    available = Column(Boolean, default=True)

    borrowed_books = relationship("BorrowedBook", back_populates="book")

    def __repr__(self):
        return f"<Book(title='{self.title}', author='{self.author_first_name} {self.author_last_name}', available={self.available})>"

class Reader(Base):
    __tablename__ = "readers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)

    borrowed_books = relationship("BorrowedBook", back_populates="reader")

    def __repr__(self):
        return f"<Reader(name='{self.name}', email='{self.email}')>"

class BorrowedBook(Base):
    __tablename__ = "borrowed_books"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    reader_id = Column(Integer, ForeignKey("readers.id"), nullable=False)
    borrowed_at = Column(Date, default=datetime.utcnow)
    return_due_date = Column(Date, default=datetime.utcnow() + timedelta(days=14))

    book = relationship("Book", back_populates="borrowed_books")
    reader = relationship("Reader", back_populates="borrowed_books")

    def __repr__(self):
        return f"<BorrowedBook(book_id={self.book_id}, reader_id={self.reader_id}, borrowed_at='{self.borrowed_at}')>"

Base.metadata.create_all(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def add_new_book(db, title, author_first_name, author_last_name, year_published):
    try:
        new_book = Book(title=title, author_first_name=author_first_name, author_last_name=author_last_name, year_published=year_published)
        db.add(new_book)
        db.commit()
        print(f"Knyga '{title}' pridėta.")
    except exc.IntegrityError:
        db.rollback()
        print(f"Klaida: Knyga '{title}' jau yra.")
    except Exception as e:
        db.rollback()
        print(f"Klaida pridedant knygą: {e}")

def add_new_reader(db, name, email):
    try:
        new_reader = Reader(name=name, email=email)
        db.add(new_reader)
        db.commit()
        print(f"Skaitytojas '{name}' pridėta pridėtas.")
    except exc.IntegrityError:
        db.rollback()
        print(f"Klaida: Skaitytojas su el. paštu '{email}' jau yra.")
    except Exception as e:
        db.rollback()
        print(f"Klaida pridedant skaitytoją: {e}")

def borrow_a_book(db, reader_id, book_id):
    reader = db.query(Reader).filter(Reader.id == reader_id).first()
    book = db.query(Book).filter(Book.id == book_id).first()

    if not reader:
        print("Klaida: Skaitytojas nerastas.")
        return
    if not book:
        print("Klaida: Knyga nėra.")
        return
    if not book.available:
        print("Klaida: Knyga jau paskolinta.")
        return

    try:
        borrowed_book = BorrowedBook(reader_id=reader_id, book_id=book_id)
        db.add(borrowed_book)
        book.available = False
        db.commit()
        print(f"Knyga '{book.title}' sėkmingai paskolinta '{reader.name}'.")
    except Exception as e:
        db.rollback()
        print(f"Klaida skolinant knygą: {e}")

def update_book_info(db, book_id, title=None, author_first_name=None, author_last_name=None, year_published=None):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        print("Klaida: Knygos nerasta.")
        return

    if title:
        book.title = title
    if author_first_name:
        book.author_first_name = author_first_name
    if author_last_name:
        book.author_last_name = author_last_name
    if year_published:
        book.year_published = year_published

    try:
        db.commit()
        print(f"Knyga '{book.title}' sėkmingai atnaujinta.")
    except Exception as e:
        db.rollback()
        print(f"Klaida atnaujinant knygą: {e}")

def delete_reader_or_book(db, id_to_delete, is_book=False):
    if is_book:
        item = db.query(Book).filter(Book.id == id_to_delete).first()
        item_type = "Knyga"
    else:
        item = db.query(Reader).filter(Reader.id == id_to_delete).first()
        item_type = "Skaitytojas"

    if not item:
        print(f"Klaida: {item_type} nerastas.")
        return

    try:
        db.delete(item)
        db.commit()
        print(f"{item_type} sėkmingai pašalintas.")
    except Exception as e:
        db.rollback()
        print(f"Klaida šalinant {item_type}: {e}")

def list_all_books(db):
    books = db.query(Book).all()
    if not books:
        print("Knygų sąrašas tuščias.")
        return

    print("Knygų sąrašas:")
    for book in books:
        print(f"ID: {book.id}, Pavadinimas: {book.title}, Autorius: {book.author_first_name} {book.author_last_name}, Metai: {book.year_published}, Prieinama: {book.available}")

def list_all_borrowed_books(db):
    borrowed_books = db.query(BorrowedBook).all()
    if not borrowed_books:
        print("Paskolintų knygų sąrašas tuščias.")
        return

    print("Paskolintų knygų sąrašas:")
    for borrowed in borrowed_books:
        book = db.query(Book).filter(Book.id == borrowed.book_id).first()
        reader = db.query(Reader).filter(Reader.id == borrowed.reader_id).first()
        print(f"Knyga: {book.title}, Skaitytojas: {reader.name}, Paimta: {borrowed.borrowed_at}, Grąžinti iki: {borrowed.return_due_date}")