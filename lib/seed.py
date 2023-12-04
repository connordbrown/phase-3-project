# lib/seed.py

from models.__init__ import CONN, CURSOR
from models.bookstore import Bookstore
from models.customer import Customer
from models.book import Book

def seed_database():
    Bookstore.drop_table()
    Customer.drop_table()
    Book.drop_table()
    Bookstore.create_table()
    Customer.create_table()
    Book.create_table()

    Bookstore.create("Barnes and Noble", "Boulder") 
    Bookstore.create("Borders", "Superior")         
    Bookstore.create("Read Queen", "Lafayette")     

    Customer.create("James", "Jameson")  
    Customer.create("Dick", "Dickens")   
    Customer.create("John", "Johnson")   
    Customer.create("Wendy", "Williams") 
    Customer.create("Sarah", "Summers")  
    Customer.create("Emma", "Emsworth")  

    Book.create("Moby Dick", "Herman Melville", 1, 1)
    Book.create("Moby Dick", "Herman Melville", 1, 2)
    Book.create("Don Quixote", "Miguel de Cervantes", 1, 1)
    Book.create("Alice in Wonderland", "Lewis Carroll", 1, 1)
    Book.create("Treasure Island", "Robert Louis Stevenson", 1, 2)
    Book.create("Pride and Prejudice", "Jane Austen", 1, 2)
    Book.create("Gulliver's Travels", "Jonathan Swift", 1, 2)
    Book.create("A Christmas Carol", "Charles Dickens", 2, 3)
    Book.create("Little Women", "Louisa May Alcott", 2, 3)
    Book.create("The Hobbit", "J.R.R. Tolkien", 2, 3)
    Book.create("Dracula", "Bram Stoker", 2, 4)
    Book.create("The Great Gatsby", "F. Scott Fitzgerald", 2, 4)
    Book.create("The Call of the Wild", "Jack London", 2, 4)
    Book.create("The Wind in the Willows", "Kenneth Grahame", 3, 5)
    Book.create("The Grapes of Wrath", "John Steinbeck", 3, 5)
    Book.create("Fahrenheit 451", "Ray Bradbury", 3, 5)
    Book.create("Candide", "Voltaire", 3, 6)
    Book.create("The Swiss Family Robinson", "Johann David Wyss", 3, 6)
    Book.create("A Wrinkle in Time", "Madeleine L'Engle", 3, 6)


if __name__ == '__main__':
    seed_database()
    print("Seeded database")
