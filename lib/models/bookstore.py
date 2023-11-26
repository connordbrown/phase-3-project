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