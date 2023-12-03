# lib/helpers.py
from models.book import Book
from models.bookstore import Bookstore
from models.customer import Customer

def exit_program():
    print("Goodbye!")
    exit() 

### bookstore functions ###

def list_bookstores():
    bookstores = Bookstore.get_all()
    print(f"{'id':<2}   {'bookstore_name':<16}   {'location':<12}")
    print(f"----------------------------------")
    for bookstore in bookstores:
        print(f"{bookstore.id:<2}   {bookstore.name:<16}   {bookstore.location:<12}")

def find_bookstore_by_name():
    name = input("Enter the bookstore's name: ")
    print()
    bookstore = Bookstore.find_by_name(name)
    if bookstore:
        print(f"{'id':<2}   {'bookstore_name':<16}   {'location':<12}")
        print(f"----------------------------------")
        print(f"{bookstore.id:<2}   {bookstore.name:<16}   {bookstore.location:<12}")
    else:
        print(f"Bookstore '{name}' not found")

# def find_bookstore_by_id():
#     try:
#         bookstore_id = int(input("Enter the bookstore's database id: "))
#     except Exception as exc:
#         print("Error:", exc)
#     bookstore = Bookstore.find_by_id(bookstore_id)
#     print(bookstore) if bookstore else print(f"Bookstore #{bookstore_id} not found")

def create_bookstore():
    print(f"Create a bookstore")
    print("--------------------")
    name = input("Enter the bookstore's name: ")
    location = input("Enter the bookstore's location: ")
    try:
        bookstore = Bookstore.create(name, location)
        print()
        print(f'Success: {bookstore}')
    except Exception as exc:
        print("Error creating bookstore: ", exc)

def update_bookstore():
    try:
        bookstore_id = int(input("Enter the bookstore id: "))
    except Exception as exc:
        print("Error:", exc)

    if bookstore := Bookstore.find_by_id(bookstore_id):
        try:
            name = input("Enter the bookstore's new name: ")
            bookstore.name = name
            location = input("Enter the bookstore's new location: ")
            bookstore.location = location

            bookstore.update()
            print(f'Success: {bookstore}')
        except Exception as exc:
            print("Error updating bookstore:", exc)
    else:
        print(f"Bookstore #{bookstore_id} not found")

def delete_bookstore():
    try:
        bookstore_id = int(input("Enter the bookstore id: "))
    except Exception as exc:
        print(f"Error:", exc)

    if bookstore := Bookstore.find_by_id(bookstore_id):
        bookstore.delete()
        print(f"Bookstore #{bookstore_id} deleted")
    else:
        print(f"Bookstore #{bookstore_id} not found")

def list_bookstore_books():
    try:
        bookstore_id = int(input("Enter the bookstore id: "))
    except Exception as exc:
        print(f"Error:", exc)

    if bookstore := Bookstore.find_by_id(bookstore_id):
        books = bookstore.books()
        for book in books:
            print(book)
    else:
        print(f"Bookstore {bookstore_id} not found") 

### customer functions ###

def list_customers():
    customers = Customer.get_all()
    print(f"{'id':<2}   {'last_name':<10}   {'first_name':<12}")
    print(f"-----------------------------")
    for customer in customers:
        print(f"{customer.id:<2}   {customer.last_name:<10}   {customer.first_name:<12}")

def find_customer_by_last_name():
    last_name = input("Enter the customer's last name: ")
    print()
    customer = Customer.find_by_last_name(last_name)
    if customer:
        print(f"{'id':<2}   {'last_name':<10}   {'first_name':<12}")
        print(f"-----------------------------")
        print(f"{customer.id:<2}   {customer.last_name:<10}   {customer.first_name:<12}")
    else:
        print(f"Customer '{last_name}' not found")

# def find_customer_by_id():
#     try:
#         customer_id = int(input("Enter the customers's database id: "))
#     except Exception as exc:
#         print("Error:", exc)
#     customer = Customer.find_by_id(customer_id)
#     print(customer) if customer else print(f"Customer {customer_id} not found")

def create_customer():
    first_name = input("Enter the customer's first name: ")
    last_name = input("Enter the customer's last name: ")
    try:
        customer = Customer.create(first_name, last_name)
        print(f'Success: {customer}')
    except Exception as exc:
        print("Error creating customer: ", exc)

def update_customer():
    try:
        customer_id = int(input("Enter the customer id: "))
    except Exception as exc:
        print("Error:", exc)

    if customer := Customer.find_by_id(customer_id):
        try:
            first_name = input("Enter the customer's new first name: ")
            customer.first_name = first_name
            last_name = input("Enter the customes's new last name: ")
            customer.last_name = last_name

            customer.update()
            print(f'Success: {customer}')
        except Exception as exc:
            print("Error updating customer:", exc)
    else:
        print(f"Customer #{customer_id} not found")

def delete_customer():
    customer_id = input("Enter the customer's id: ")
    if customer := Customer.find_by_id(customer_id):
        customer.delete()
        print(f'Customer #{customer_id} deleted')
    else:
        print(f'Customer #{customer_id} not found')

def list_customer_books():
    try:
        customer_id = int(input("Enter the customer id: "))
    except Exception as exc:
        print(f"Error:", exc)

    if customer := Bookstore.find_by_id(customer_id):
        books = customer.books()
        for book in books:
            print(book)
    else:
        print(f"Customer #{customer_id} not found") 

### book functions ###

def list_books():
    books = Book.get_all()
    print(f"{'id':<2}   {'title':<25}   {'author':<22}   {'bookstore_id':<12}   {'customer_id':<2}")
    print(f"--------------------------------------------------------------------------------------")
    for book in books:
        print(f"{book.id:<2}   {book.title:<25}   {book.author:<22}   {book.bookstore_id:<12}   {book.customer_id:<2}")
        

def find_book_by_title():
    title = input("Enter the book's title: ")
    print()
    book = Book.find_by_title(title)
    if book:
        print(f"{'id':<2}   {'title':<25}   {'author':<22}   {'bookstore_id':<12}   {'customer_id':<2}")
        print(f"--------------------------------------------------------------------------------------")
        print(f"{book.id:<2}   {book.title:<25}   {book.author:<22}   {book.bookstore_id:<12}   {book.customer_id:<2}")
    else:
        print(f"Book '{title}' not found")

# def find_book_by_id():
#     try:
#         book_id = int(input("Enter the book's database id: "))
#     except Exception as exc:
#         print("Error:", exc)
#     book = Book.find_by_id(book_id)
#     print(book) if book else print(f"Book #{book_id} not found")

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
        print(f"Book #{book_id} deleted")
    else:
        print(f"Book #{book_id} not found")

def list_customers_bookstores():
    customers_bookstores = Book.customer_bookstores() 
    for customer_bookstore in customers_bookstores:
        print(customer_bookstore)  