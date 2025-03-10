from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, year, available=True):
        self.title = title
        self.author = author
        self.year = year
        self.available = available
        self.borrowed_date = None
    def __str__(self):
        return f"Pavadinimas: {self.title}, Autorius: {self.author}, Metai: {self.year}, Prieinama: {self.available}"
    def is_classic(self):
        return datetime.now().year - self.year > 50
    def borrow(self):
        self.available = False
        self.borrowed_date = datetime.now()
    def return_book(self):
        self.available = True
        self.borrowed_date = None
    def due_date(self):
        if self.borrowed_date:
            return self.borrowed_date + timedelta(days=14)

class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        if isinstance(book, Book): self.books.append(book)
        else: print("Tik knygos")
    def display_books(self):
        if not self.books: print("Nėra knygų")
        for book in self.books: print(book)
    def borrow_book(self, title):
        try:
            book = next(b for b in self.books if b.title == title)
            if book.available:
                book.borrow()
                print(f"'{title}' pasiskolinta")
            else: print(f"'{title}' nepasiekiama")
        except StopIteration: print(f"'{title}' nerasta")
    def return_book(self, title):
        try:
            book = next(b for b in self.books if b.title == title)
            if not book.available:
                book.return_book()
                print(f"'{title}' grąžinta")
            else: print(f"'{title}' nebuvo pasiskolinta")
        except StopIteration: print(f"'{title}' nerasta")
    def filter_books(self, *args, **kwargs):
        filtered_books = self.books
        if args: filtered_books = [book for book in filtered_books if book.title in args]
        for key, value in kwargs.items():
            if key == "author": filtered_books = [book for book in filtered_books if book.author == value]
            elif key == "year": filtered_books = [book for book in filtered_books if book.year == value]
            elif key == "is_classic": filtered_books = [book for book in filtered_books if book.is_classic() == value]
        return filtered_books

def library_system():
    library = Library()
    while True:
        print("\nBibliotekos sistema")
        print("1. Pridėti knygą")
        print("2. Peržiūrėti knygas")
        print("3. Pasiskolinti knygą")
        print("4. Grąžinti knygą")
        print("5. Filtruoti knygas")
        print("6. Išeiti")
        choice = input("Pasirinkite parinktį: ")
        if choice == '1':
            title = input("Pavadinimas: ")
            author = input("Autorius: ")
            year = input("Metai: ")
            book = Book(title, author, int(year))
            library.add_book(book)
            print(f"Knyga '{title}' pridėta.")
        elif choice == '2':
            library.display_books()
        elif choice == '3':
            title = input("Pasiskolinti knygą: ")
            library.borrow_book(title)
        elif choice == '4':
            title = input("Grąžinti knygą: ")
            library.return_book(title)
        elif choice == '5':
            filter_choice = input("Filtruoti pagal: (title/author/year): ")
            if filter_choice == 'title': title = input("Pavadinimas: "); library.filter_books(title)
            elif filter_choice == 'author': author = input("Autorius: "); library.filter_books(author=author)
            elif filter_choice == 'year': year = input("Metai: "); library.filter_books(year=int(year))
        elif choice == '6':
            print("Išeinama...")
            break
        else:
            print("Netinkamas pasirinkimas.")

if __name__ == "__main__":
    library_system()


