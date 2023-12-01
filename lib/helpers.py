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
    try:
        book_id = int(input("Enter the book's database id: "))
    except Exception as exc:
        print("Error:", exc)
    book = Book.find_by_id(book_id)
    print(book) if book else print(f"Book #{book_id} not found")

def create_book():
    title = input("Enter the book's title: ")
    author = input("Enter the book's author: ")
    try:
        bookstore_id = int(input("Enter the bookstore id: "))
        customer_id = int(input("Enter the customer id: "))
        book = Book.create(title, author, bookstore_id, customer_id)
        print(f'Success: {book}')
    except Exception as exc:
        print("Error creating book:", exc)

def update_book():
    try:
        book_id = int(input("Enter the book's id: "))
    except Exception as exc:
        print("Error:", exc)

    if book := Book.find_by_id(book_id):
        try:
            title = input("Enter the book's new title: ")
            book.title = title
            author = input("Enter the book's new author: ")
            book.author = author
            bookstore_id = int(input("Enter the book's new bookstore id: "))
            book.bookstore_id = bookstore_id
            customer_id = int(input("Enter the book's new customer id: "))
            book.customer_id = customer_id

            book.update()
            print(f'Success: {book}')
        except Exception as exc:
            print("Error updating book:", exc)
    else:
        print(f"Book #{book_id} not found")

def delete_book():
    try:
        book_id = int(input("Enter the book's id: "))
    except Exception as exc:
        print(f"Error:", exc)

    if book := Book.find_by_id(book_id):
        book.delete()
        print(f"Book {book_id} deleted")
    else:
        print(f"Book #{book_id} not found")

def list_customers_bookstores():
    customers_bookstores = Book.customer_bookstores() 
    for customer_bookstore in customers_bookstores:
        print(customer_bookstore)   

### bookstore functions ###

def list_bookstores():
    bookstores = Bookstore.get_all()
    for bookstore in bookstores:
        print(bookstore)

def find_bookstore_by_name():
    name = input("Enter the bookstore's name: ")
    bookstore = Bookstore.find_by_name(name)
    print(bookstore) if bookstore else print(f"Bookstore {name} not found")

def find_bookstore_by_id():
    try:
        bookstore_id = int(input("Enter the bookstore's database id: "))
    except Exception as exc:
        print("Error:", exc)
    bookstore = Bookstore.find_by_id(bookstore_id)
    print(bookstore) if bookstore else print(f"Bookstore #{bookstore_id} not found")


### customer functions ###
