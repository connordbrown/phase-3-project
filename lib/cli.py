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
    print("3: Create bookstore")
    print("4: Update bookstore")
    print("5: Delete bookstore")

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
