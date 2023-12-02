# lib/cli.py
from helpers import (
    exit_program,
    list_bookstores,
    find_bookstore_by_name,
    create_bookstore,
    update_bookstore,
    delete_bookstore,
    list_bookstore_books,
    list_customers,
    find_customer_by_last_name,
    create_customer,
    update_customer,
    delete_customer,
    list_books,
    find_book_by_title,
    create_book,
    update_book,
    delete_book,
    list_customers_bookstores
)

def menu():
    print("Welcome to the Big Book Business store management system!\n")
    print("Please select an option:\n")
    print("0. Exit the program")
    print("1. Manage bookstores")
    print("2. Manage customers")
    print("3. Manage books")

def bookstore_menu():
    print("Bookstore Manager - please select an option:\n")
    print("0. Return to main menu")
    print("1. List all bookstores")
    print("2. Find bookstore by name")
    print("3: Create a bookstore")
    print("4: Update a bookstore")
    print("5: Delete a bookstore")
    print("6: List all books for a given bookst0ore")

def customer_menu():
    print("Customer Manager - please select an option:\n")
    print("0. Return to main menu")
    print("1. List all customers")
    print("2. Find customer by last name")
    print("3: Create a customer")
    print("4: Update a customer")
    print("5: Delete a customer")
    print("6: List all books for a given customer")   

def book_menu():
    print("Book Manageer - please select an option:\n")
    print("0. Return to main menu")
    print("1. List all books")
    print("2. Find book by title")
    print("3: Create a book")
    print("4: Update a book")
    print("5: Delete a book")
    print("6: List all customers and bookstores associated with each book")   

def bookstore_main():
    while True:
        bookstore_menu()
        print()
        choice = input("> ")
        print()
        if choice == "0":
            break
        elif choice == "1":
            list_bookstores()
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            pass
        else:
            print("Invalid choice")
        print()

def customer_main():
    while True:
        customer_menu()
        print()
        choice = input("> ")
        print()
        if choice == "0":
            break
        elif choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            pass
        else:
            print("Invalid choice")

def book_main():
    while True:
        book_menu()
        print()
        choice = input("> ")
        print()
        if choice == "0":
            break
        elif choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            pass
        else:
            print("Invalid choice")

def main():
    print()
    while True:
        menu()
        print()
        choice = input("> ")
        print()
        if choice == "0":
            exit_program()
        elif choice == "1":
            bookstore_main()
        elif choice == "2":
            customer_main()
        elif choice == "3":
            book_main()
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()