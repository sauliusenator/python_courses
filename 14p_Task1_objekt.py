from symtable import Class
# 1. ############################################

class Manufacturer:
    car = 'C5'
Manufacturer1_bike = 'Yamaha'

# print(Manufacturer)
print(Manufacturer.car,  Manufacturer1_bike)

# 2. ############################################

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

book = Book('Book', 'Mark', 2025)
print(book.title, book.author, book.year)
# 3. ############################################
class Book:
    publisher = "Penguin"  # Statinis laukas

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

book1 = Book('Book 1', 'Author 1', 2000)
book2 = Book('Book 2', 'Author 2', 2005)


for book in [book1, book2]:
    print(f"Title: {book.title}, Author: {book.author}, Publisher: {Book.publisher}")