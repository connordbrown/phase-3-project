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
        Update object id attribute using primary key value of new row. Save object in class
        dictionary 'all' using table row's primary key as dictionary key """

        sql = """
            INSERT INTO customers (first_name, last_name)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.first_name, self.last_name))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

