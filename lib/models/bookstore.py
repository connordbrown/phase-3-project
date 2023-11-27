from __init__ import CURSOR, CONN

class Bookstore:

    # dictionary of objects saved to the database
    all = {}

    def __init__(self, name, location, id=None):
        self.name = name
        self.location = location
        self.id = id
    
    def __repr__(self):
        return f"<Bookstore #{self.id}: {self.name}, {self.location}>"

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
            DROP TABLE IF EXISTS bookstores;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name and location values of current Bookstore instance.
            Update object id attribute using primary key value of new row. Save object in class
            dictionary 'all' using table row's primary key as dictionary key """

        sql = """
            INSERT INTO bookstores (name, location)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.location))
        CONN.commit()

        # update id attribute, save instance to class dictionary
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    @classmethod
    def create(cls, name, location):
        """ Initialize a new Bookstore instance and save object to database.
        return: bookstore (Bookstore object) """

        bookstore = cls(name, location)
        bookstore.save()
        return bookstore
    
    def update(self):
        """ Update the table row corresponding to the current Bookstore instance """

        sql = """
            UPDATE bookstores
            SET name = ?, location = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.name, self.location, self.id))
        CONN.commit()

    def delete(self):
        """ Delete the table row and dictionary entry corresponding to the
        current bookstore instance and reassign id attribute """

        sql = """
            DELETE FROM bookstores
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # delete dictionary entry using id as key
        del type(self).all[self.id]
         
        # set the id to None
        self.id = None
    
    @classmethod
    def instance_from_db(cls, row):
        """ Return a Bookstore object having attribute values from its table row """

        # check dictionary for existing instance using row's primary key
        bookstore = cls.all.get(row[0])
        if bookstore:
            # ensure attributes match row values in case local instance modified
            bookstore.name = row[1]
            bookstore.location = row[2]
        else:
            # not in dictionary, create new instance and add to dictionary
            bookstore = cls(row[1], row[2])
            bookstore.id = row[0]
            cls.all[bookstore.id] = bookstore
        return bookstore
    
    @classmethod
    def get_all(cls):
        """ Return a list of Bookstore objects for each row in table """

        sql = """
            SELECT *
            FROM bookstores
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows] 

    @classmethod
    def find_by_id(cls, id):
        """ Return a Bookstore object corresponding to the first table row matching
        the specified primary key """

        sql = """
            SELECT *
            FROM bookstores
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        """ Return a Bookstore object corresponding to the first table row matching
        the specified name """

        sql = """
            SELECT *
            FROM bookstores
            WHERE name = ?
        """

        row = CURSOR.execute(sql, (name,))
        return cls.instance_from_db(row) if row else None

    #def books(self):
        #""" Return list of books associated to current bookstore """
        #from book import Book
        #sql = """
        #    SELECT *
        #    FROM books
        #    WHERE bookstore_id = ?
        #"""

        #rows = CURSOR.execute(sql, (self.id,)).fetchall()
        #return [Book.instance_from_db(row) for row in rows]