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
    
    @classmethod
    def create_table(cls):
        """ Create a new table to presist the attributes of Book instances """
        
        sql = """
            CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            bookstore_id INTEGER,
            FOREIGN KEY (bookstore_id) REFERENCES bookstores(id),
            customer_id INTEGER,
            FOREIGN KEY (customer_id) REFERENCES customers(id))
        """

        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Book instances """

        sql = """
            DROP TABLE IF EXISTS books;
        """

        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        """ Insert new row with title, author, bookstore_id and customer_id values of current 
        Customer instance. Update current object id attribute using primary key value of new row. Save object in class
        dictionary 'all' using table row's primary key as dictionary key """

        sql = """
            INSERT INTO books (title, author, bookstore_id, customer_id)
            VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.title, self.author, self.bookstore_id, self.customer_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """ Update the table row corresponding to the current Book instance """

        sql = """
            UPDATE books
            SET title = ?, author = ?, bookstore_id = ?, customer_id = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.title, self.author, self.bookstore_id, self.customer_id, self.id))
        CONN.commit()
    
    def delete(self):
        """ Delete the table row corresponding to the current Book instance,
        delete the dictionary key, and reassign id attribute """

        sql = """
            DELETE FROM books
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # delete dictionary entry using id as key
        del type(self).all[self.id]

        # set the id to None
        self.id = None
    
    @classmethod
    def create(cls, title, author, bookstore_id, customer_id):
        """ Initialize a new Book instance and save the object to the database """

        employee = cls(title, author, bookstore_id, customer_id)
        employee.save()
        return employee

    @classmethod
    def instance_from_db(cls, row):
        """ Return a Book object having the attribute values from its table row """

        # check dictionary for existing instance using row's primary key
        book = cls.all.get(row[0])
        if book:
            # ensure attributes match row values in case local instance was modified
            book.title = row[1]
            book.author = row[2]
            book.bookstore_id = row[3]
            book.customer_id = row[4]
        else:
            # not in dictionary, create new instance and add to dictionary
            book = cls(row[1], row[2], row[3], row[4])
            book.id = row[0]
            cls.all[book.id] = book

        return book

    @classmethod
    def get_all(cls):
        """ Return a list of Book objects for each row in table """
        
        sql = """
            SELECT *
            FROM books
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """ Return Book object corresponding to first table row matching
        the specified primary key """

        sql = """
            SELECT *
            FROM books
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()

        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_title(cls, title):
        """Return Book object corresponding to the first table row matching
        the specified title """

        sql = """
            SELECT *
            FROM books
            WHERE title = ?
        """

        row = CURSOR.execute(sql, (title,)).fetchone()

        return cls.instance_from_db(row) if row else None

    