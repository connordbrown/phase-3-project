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

def find_book_by_title():
    title = input("Enter the book's title: ")
    book = Book.find_by_title(title)
    print(book) if book else print(f"Book {title} not found")

def find_book_by_id():
    book_id = input("Enter the book's database id: ")
    book = Book.find_by_id(book_id)
    print(book) if book else print(f"Book {book_id} not found")

### bookstore functions ###
### customer functions ###
