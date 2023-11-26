from __init__ import CURSOR, CONN

class Bookstore:

    # dictionary of objects saved to the database
    all = {}

    def __init__(self, name, location, id=None):
        self.name = name
        self.location = location
        self.id = id
    
    def __repr__(self):
        return f"<Bookstore b{self.id}: {self.name}, {self.location}>"

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise Exception
        if not len(name):
            raise Exception
        self._name = name
    
    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, location):
        if not isinstance(location, str):
            raise Exception
        if not len(location):
            raise Exception
        self._location = location
    
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Bookstore instances """

        sql = """
            CREATE TABLE IF NOT EXISTS bookstores (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Bookstore instances """

        sql = """
            DROP TABLE IF EXISTS departments;
        """
        CURSOR.execute(sql)
        CONN.commit()