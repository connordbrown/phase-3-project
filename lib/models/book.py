from __init__ import CURSOR, CONN
from bookstore import Bookstore
from customer import Customer

class Book:

    # dictionary of objects saved to the database
    all = {}

    def __init__(self, title, author, bookstore_id, customer_id, id=None):
        self.title = title
        self.author = author
        self.bookstore_id = bookstore_id
        self.customer_id = customer_id
        self.id = id 
    
    def __repr__(self):
        return (
            f"<Book #{self.id}: {self.title}, by {self.author}, " +
            f"Bookstore ID: {self.bookstore_id}, Customer ID: {self.customer_id}>" 
        )
    
    @property
    def title(self):
        return self._name
    
    @title.setter
    def title(self, title):
        if not isinstance(title, str):
            raise Exception
        if not len(title):
            raise Exception
        self._title = title
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if not isinstance(author, str):
            raise Exception
        if not len(author):
            raise Exception
        self._author = author
    
    @property
    def bookstore_id(self):
        return self._bookstore_id
    
    @bookstore_id.setter
    def bookstore_id(self, bookstore_id):
        if not isinstance(bookstore_id, int):
            raise Exception
        if not Bookstore.find_by_id(bookstore_id):
            raise Exception
        self._bookstore_id = bookstore_id
    
    @property
    def customer_id(self):
        return self._customer_id
    
    @customer_id.setter
    def customer_id(self, customer_id):
        if not isinstance(customer_id, int):
            raise Exception
        if not Customer.find_by_id(customer_id):
            raise Exception
        self._customer_id = customer_id
    
