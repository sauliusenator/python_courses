# 4. ############################################
class Book:
    publisher = "Penguin"
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def __str__(self):
        return f"Book(title='{self.title}', author='{self.author}', year={self.year})"
book1 = Book('Knyga 1', 'Autorius 1', 2000)
print(book1)
# 5. ############################################
import datetime

class Book:
    publisher = "Penguin"

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def get_book_age(self):
        return datetime.datetime.today().year - self.year
    def __str__(self):
        return f"Book(title='{self.title}', author='{self.author}', year={self.year})"
books = [
    Book('Knyga 1', 'Autorius 1', 2000),
    Book('Knyga 2', 'Autorius 2', 2010),
    Book('Knyga 3', 'Autorius 3', 2015)
]
for book in books:
    print(f"{book}: Knygos amžius: {book.get_book_age()} metai")
# 6. ############################################

class Book:
    publisher = "Penguin"

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_book_age(self):
        return datetime.datetime.today().year - self.year
    def __str__(self):
        return f"Book(title='{self.title}', author='{self.author}', year={self.year})"

book = Book('Knyga 1', 'Autorius 1', 2000)
age = book.get_book_age()
print(f"Knyga '{book.title}' yra {age} metų senumo.")