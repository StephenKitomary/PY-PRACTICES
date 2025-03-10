class Int_set(object):
    """ An Int_set is a set of integers"""

    def __int__(self):
        """Create an empty set of integers"""
        self._vals = []
    def insert(self,e):
        """Assumes e is an integer and inserts e into self"""
        if e not in self._vals:
            self._vals.append(e)
    def member(self,e):
        """Assumes e is an integer Returns True is e is in self, False otherwise"""
        return e in self._vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self, Raises Value error if e is not in self"""
        try:
            self._vals.remove(e)
        except:
            raise ValueError(str(e)+ "not found")

    def get_members(self):
        """Returns a list containing the elements of self. Nothing can be assumend about the order of the elements"""
        return self._vals[:]

    def __str__(self):
        """Returns a string representation of sef"""
        if self._vals = []:
            return '{}'

    
