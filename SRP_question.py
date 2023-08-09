""""""
class Book:
    def __init__(self, title, author, isbn, genre, availability = True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.availability = availability

    def __str__(self):
        return f"Book Details\nTitle: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nGenre: {self.genre}\nAvailability: {self.availability}"


class LibraryCatalog:
    def __init__(self):
        self.books = []

    def add_books(self, book):
        self.books.append(book)

    def get_books_details(self, title):
        for book in self.books:
            if book.title == title:
                return book

    def get_all_books(self):
        return self.books

book1 = Book("One Piece","Eiichiro ODA", 123, "Manga")

library = LibraryCatalog()
library.add_books(book1)

all_books = library.get_all_books()
for books in all_books:
    print(books)

book_info = library.get_books_details("One Piece")
print(book_info)