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