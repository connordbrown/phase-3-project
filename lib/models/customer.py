from __init__ import CURSOR, CONN

class Customer:

    # dictionary of objects saved to database
    all = {}

    def __init__(self, first_name, last_name, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
    
    def __repr__(self):
        return f"<Customer #{self.id}: {self.last_name}, {self.first_name}>"
    
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, first_name):
        if not isinstance(first_name, str):
            raise Exception
        if not len(first_name):
            raise Exception
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name):
        if not isinstance(last_name, str):
            raise Exception
        if not len(last_name):
            raise Exception
        self._last_name = last_name
    
    @classmethod
    def create_table(cls):
        """ Create a new table to persist attributes of Customer instances """

        sql = """
            CREATE TABLE IF NOT EXISTS customers
            id INTEGER PRIMARY KEY
            first_name TEXT,
            last_name TEXT
        """

        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Customer instances """

        sql = """
            DROP TABLE IF EXISTS customers;
        """

        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert new row with first_name and last_name values of current Customer instance.
        Update current object id attribute using primary key value of new row. Save object in class
        dictionary 'all' using table row's primary key as dictionary key """

        sql = """
            INSERT INTO customers (first_name, last_name)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.first_name, self.last_name))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, first_name, last_name):
        """ Initialize a new Customer instance and save the object to the datebase
            return: customer (Customer object) """

        customer = cls(first_name, last_name)
        customer.save()
        return customer

    def update(self):
        """ Update table row corresponding to current Customer instance """

        sql = """
            UPDATE customers
            SET first_name = ?, last_name = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.first_name, self.last_name, self.id))
        CONN.commit()
    
    def delete(self):
        """ Delete table row and dictionary entry corresponding to 
        current Customer instance and reassign id attribute """

        sql = """
            DELETE FROM customers
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # delete dictionary entry using id as key
        del type(self).all[self.id]

        # set id to None
        self.id = None
    
    @classmethod
    def instance_from_db(cls, row):
        """ Return a Customer object having attribute values from its table row """

        # check dictionary for existing instance using row's primary key
        customer = cls.all.get(row[0])
        if customer:
            # ensure attributes match row values in case local instance modified
            customer.first_name = row[1]
            customer.last_name = row[2]
        else:
            # not in dictionary, create new instance and add to dictionary
            customer = cls(row[1], row[2])
            customer.id = row[0]
            cls.all[customer.id] = customer
        return customer

    @classmethod
    def get_all(cls):
        """ Return a list of Customer objects for each row in table """
        
        sql = """
            SELECT *
            FROM customers
        """

        rows = CURSOR.execute(sql).fetchall()
        
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        """ Return a Customer object corresponding to the first table row matching
        the specified primary key """

        sql = """
            SELECT *
            FROM customer
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_last_name(cls, last_name):
        """ Return a Customer object corresponding to the first table row matching
        specified last name """
                
        sql = """
            SELECT *
            FROM customers
            WHERE last_name = ?
        """

        row = CURSOR.execute(sql, (last_name,)).fetchone()

        return cls.instance_from_db(row) if row else None
    
    #def books(self):
        #""" Return list of books associated with current customer """
        #from book import Book
        #sql = """
        #    SELECT *
        #    FROM books
        #    WHERE customer_id = ?
        #"""

        #rows = CURSOR.execute(sql, (self.id,)).fetchall()
        #return [Customer.instance_from_db(row) for row in rows]
        
