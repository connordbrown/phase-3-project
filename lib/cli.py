# lib/cli.py
from helpers import (
    exit_program,
    list_books,
    find_book_by_title,
    create_book,
    update_book,
    delete_book,
    list_customers_bookstores,
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
    delete_customer
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_books()
        elif choice == "2":
            submain()
        else:
            print("Invalid choice")
        print()


def menu():
    print()
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")
    print()

def bookstore_menu():
    print("Please select an option:")
    print("0. Return to main menu")
    print("1. List all bookstores")
    print("2. Find bookstore by name")
    print("3: Create a bookstore")
    print("4: Update a bookstore")
    print("5: Delete a bookstore")
    print("6: List all books for a given bookstore")

def customer_menu():
    print("Please select an option:")
    print("0. Return to main menu")
    print("1. List all customers")
    print("2. Find customer by last name")
    print("3: Create a customer")
    print("4: Update a customer")
    print("5: Delete a customer")
    print("6: List all books for a given customer")   

def book_menu():
    print("Please select an option:")
    print("0. Return to main menu")
    print("1. List all books")
    print("2. Find book by title")
    print("3: Create a book")
    print("4: Update a book")
    print("5: Delete a book")
    print("6: List all customers and bookstores associated with each book")   


def submain():
    while True:
        submenu()
        choice = input("> ")
        if choice == '0':
            break
        else:
            print("Yay!")
        input("Press ENTER to return to menu")



if __name__ == "__main__":
    main()