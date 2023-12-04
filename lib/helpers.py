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

def create_bookstore():
    print("Create a bookstore")
    print("--------------------")
    name = input("Enter the bookstore's name: ")
    location = input("Enter the bookstore's location: ")
    try:
        bookstore = Bookstore.create(name, location)
        print()
        print(f'Success: {bookstore.name}, {bookstore.location} created')
    except Exception as exc:
        print()
        print("Error creating bookstore:", exc)

def update_bookstore():
    print("Update a bookstore")
    print("--------------------")
    bookstore_name = input("Enter the bookstore name: ")
    print()
    if bookstore := Bookstore.find_by_name(bookstore_name):
        try:
            name = input("Enter the bookstore's new name: ")
            bookstore.name = name
            location = input("Enter the bookstore's new location: ")
            bookstore.location = location

            bookstore.update()
            print()
            print(f'Success: {bookstore.name}, {bookstore.location} updated')
        except Exception as exc:
            print("Error updating bookstore:", exc)
    else:
        print(f"Bookstore '{bookstore_name}' not found")

def delete_bookstore():
    bookstore_name = input("Enter the bookstore name: ")

    if bookstore := Bookstore.find_by_name(bookstore_name):
        bookstore.delete()
        print()
        print(f"Bookstore '{bookstore_name}' deleted")
    else:
        print()
        print(f"Bookstore '{bookstore_name}' not found")

def list_bookstore_books():
    bookstore_name = input("Enter the bookstore name: ")
    print()
    if bookstore := Bookstore.find_by_name(bookstore_name):
        books = bookstore.books()
        print(f"{'id':<2}   {'title':<25}   {'author':<22}   {'customer_id':<2}")
        print(f"-----------------------------------------------------------------------")
        for book in books:
            print(f"{book.id:<2}   {book.title:<25}   {book.author:<22}   {book.customer_id:<2}")
    else:
        print(f"Bookstore '{bookstore_name}' not found") 

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

def create_customer():
    print(f"Create a customer")
    print("--------------------")
    first_name = input("Enter the customer's first name: ")
    last_name = input("Enter the customer's last name: ")
    try:
        customer = Customer.create(first_name, last_name)
        print()
        print(f"Success: customer '{customer.first_name} {customer.last_name}' created")
    except Exception as exc:
        print()
        print("Error creating customer:", exc)

def update_customer():
    print("Update a customer")
    print("-------------------")
    last_name = input("Enter the customer's last name: ")

    if customer := Customer.find_by_last_name(last_name):
        try:
            first_name = input("Enter the customer's new first name: ")
            customer.first_name = first_name
            last_name = input("Enter the customers's new last name: ")
            customer.last_name = last_name

            customer.update()
            print()
            print(f"Success: customer '{customer.first_name} {customer.last_name}' updated")
        except Exception as exc:
            print("Error updating customer:", exc)
    else:
        print(f"Customer '{last_name}' not found")

def delete_customer():
    last_name = input("Enter the customer's last name: ")
    if customer := Customer.find_by_last_name(last_name):
        customer.delete()
        print()
        print(f"Customer '{customer.first_name} {customer.last_name}' deleted")
    else:
        print()
        print(f"Customer '{last_name}' not found")

def list_customer_books():
    last_name = input("Enter the customer's last name: ")

    if customer := Customer.find_by_last_name(last_name):
        books = customer.books()
        print()
        print(f"{'id':<2}   {'title':<25}   {'author':<22}   {'bookstore_id':<12}")
        print(f"------------------------------------------------------------------------")
        for book in books:
            print(f"{book.id:<2}   {book.title:<25}   {book.author:<22}   {book.customer_id:<2}")
    else:
        print(f"Customer '{last_name}' not found") 

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

def create_book():
    print(f"Create a book")
    print("--------------------")
    title = input("Enter the book's title: ")
    author = input("Enter the book's author: ")
    try:
        bookstore_name = input("Enter the bookstore name: ")
        if bookstore := Bookstore.find_by_name(bookstore_name):
            bookstore_id = bookstore.id
        else: 
            raise Exception("Bookstore not found")

        last_name = input("Enter the customer's last_name: ")
        if customer := Customer.find_by_last_name(last_name):
            customer_id = customer.id
        else:
            raise Exception("Customer not found")

        book = Book.create(title, author, bookstore_id, customer_id)
        print()
        print(f'Success: {book.title} by {book.author} created')
    except Exception as exc:
        print()
        print("Error creating book:", exc)

def update_book():
    print("Update a book")
    print("---------------")
    title = input("Enter the book title: ")

    if book := Book.find_by_title(title):
        title = input("Enter the book's new title: ")
        book.title = title
        author = input("Enter the book's new author: ")
        book.author = author
        try:
            bookstore_name = input("Enter the book's new bookstore name: ")
            if bookstore := Bookstore.find_by_name(bookstore_name):
                book.bookstore_id = bookstore.id
            else: 
                raise Exception("Bookstore not found")

            last_name = input("Enter the book's new customer's last_name: ")
            if customer := Customer.find_by_last_name(last_name):
                book.customer_id = customer.id
            else:
                raise Exception("Customer not found")

            book.update()
            print()
            print(f'Success: {book.title}, by {book.author} updated')
            
        except Exception as exc:
            print()
            print("Error updating book:", exc)
    else:
        print(f"Book '{title}' not found")

def delete_book():
    title = input("Enter the book title: ")

    if book := Book.find_by_title(title):
        book.delete()
        print()
        print(f"Book '{book.title}' deleted")
    else:
        print()
        print(f"Book '{title}' not found")

def list_customers_bookstores():
    customers_bookstores = Book.customer_bookstores() 
    print(f"{'book_title':<25}   {'bookstore_name':<18}   {'customer_last_name':<12}")
    print(f"---------------------------------------------------------------------")
    for customer_bookstore in customers_bookstores:
        print(f"{customer_bookstore[0]:<25}   {customer_bookstore[1].name:<18}   {customer_bookstore[2].last_name:<12}")