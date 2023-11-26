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

