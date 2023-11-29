#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.bookstore import Bookstore
from models.customer import Customer
from models.book import Book
import ipdb

def reset_database():
    Bookstore.drop_table()
    Customer.drop_table()
    Book.drop_table()
    Bookstore.create_table()
    Customer.create_table()
    Book.create_table()

    Bookstore.create("Barnes and Noble", "Boulder")
    Bookstore.create("Borders", "Superior")
    Bookstore.create("Read Queen", "Lafayette")



reset_database()
ipdb.set_trace()
