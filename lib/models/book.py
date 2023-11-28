from __init__ import CURSOR, CONN

class Book:

    # dictionary of objects saved to the database
    all = {}

    def __init__(self, title, author, bookstore_id, customer_id, id=None):
        self.title = title
        self.author = author
        self.bookstore_id = bookstore_id
        self.customer_id = customer_id
        self.id = id 