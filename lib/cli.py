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
            helper_1()
        else:
            print("Invalid choice")
        to_menu = input("Press enter to return to menu?")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")


if __name__ == "__main__":
    main()
