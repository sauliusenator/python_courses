from datetime import datetime, timedelta


class Book:
    def __init__(self, title, author, year, available=True):
        self.title = title
        self.author = author
        self.year = year
        self.available = available
        self.borrowed_date = None

    def __str__(self):
        return f"'{self.title}' by {self.author}, Published in {self.year}"

    def is_classic(self):
        current_year = datetime.now().year
        return current_year - self.year > 50

    def due_date(self):
        if self.borrowed_date:
            return self.borrowed_date + timedelta(days=14)
        return None


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return
        for book in self.books:
            status = "Available" if book.available else "Borrowed"
            print(f"{book} - {status}")

    def borrow_book(self, title):
        try:
            for book in self.books:
                if book.title.lower() == title.lower():
                    if book.available:
                        book.available = False
                        book.borrowed_date = datetime.now()
                        print(f"Book '{title}' borrowed successfully.")
                        print(f"Due date: {book.due_date().strftime('%Y-%m-%d')}")
                        return
                    else:
                        print(f"Book '{title}' is not available.")
                        return
            raise ValueError(f"Book '{title}' not found in the library.")
        except ValueError as e:
            print(e)

    def return_book(self, title):
        try:
            for book in self.books:
                if book.title.lower() == title.lower():
                    if not book.available:
                        book.available = True
                        book.borrowed_date = None
                        print(f"Book '{title}' returned successfully.")
                        return
                    else:
                        print(f"Book '{title}' is already in the library.")
                        return
            raise ValueError(f"Book '{title}' not found in the library.")
        except ValueError as e:
            print(e)

    def filter_books(self, *args, **kwargs):
        filtered_books = self.books

        if 'author' in kwargs:
            filtered_books = [book for book in filtered_books if book.author.lower() == kwargs['author'].lower()]

        if 'year' in kwargs:
            filtered_books = [book for book in filtered_books if book.year == kwargs['year']]

        if 'title' in kwargs:
            filtered_books = [book for book in filtered_books if kwargs['title'].lower() in book.title.lower()]

        return filtered_books


def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add a new book")
        print("2. Display all books")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Filter books")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice (1-6): "))

            if choice == 1:
                title = input("Enter book title: ")
                author = input("Enter book author: ")

                try:
                    year = int(input("Enter publication year: "))
                    book = Book(title, author, year)
                    library.add_book(book)
                    print("Book added successfully!")
                except ValueError:
                    print("Invalid year. Please enter a valid number.")

            elif choice == 2:
                library.display_books()

            elif choice == 3:
                title = input("Enter book title to borrow: ")
                library.borrow_book(title)

            elif choice == 4:
                title = input("Enter book title to return: ")
                library.return_book(title)

            elif choice == 5:
                print("Filter Options:")
                print("1. Filter by Author")
                print("2. Filter by Year")
                print("3. Filter by Title")

                filter_choice = int(input("Enter filter choice (1-3): "))

                if filter_choice == 1:
                    author = input("Enter author name: ")
                    results = library.filter_books(author=author)
                elif filter_choice == 2:
                    year = int(input("Enter year: "))
                    results = library.filter_books(year=year)
                elif filter_choice == 3:
                    title = input("Enter title: ")
                    results = library.filter_books(title=title)
                else:
                    print("Invalid choice.")
                    continue

                print("\nFiltered Books:")
                for book in results:
                    print(book)

            elif choice == 6:
                print("Thank you for using the Library Management System!")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()