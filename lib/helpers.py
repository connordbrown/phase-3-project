# lib/helpers.py
from models.book import Book
from models.bookstore import Bookstore
from models.customer import Customer

def exit_program():
    print("Goodbye!")
    exit()

### book functions ###

def list_books():
    books = Book.get_all()
    for book in books:
        print(book)

### bookstore functions ###
### customer functions ###
