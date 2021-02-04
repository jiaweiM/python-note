class Set:
    # these are the member functions
    # every one takes a first parameter "self" (another convention)
    # that refers to the particular Set object being used
    def __init__(self, values=None):
        """
        This is the constructor.
        It gets called when you create a new set.
        You would use it like
        s1 = Set() # empty set
        s2 = Set([1,2,2,3]) # initialize with values
        """
        self.dict = {}  # each instance of Set has its own dict property
        # which is what we'll use to track memberships
        if values is not None:
            for value in values:
                self.add(value)

    def __repr__(self):
        """this is the string representation of a Set object
        if you type it at the Python prompt or pass it to str()"""
        return "Set: " + str(self.dict.keys())

    def add(self, value):
        """we'll represent membership by being a key in self.dict with value True"""
        self.dict[value] = True

    def contains(self, value):
        """
        value is in the Set if it's a key in the dictionary
        """
        return value in self.dict

    def remove(self, value):
        del self.dict[value]


def test_my_set():
    s = Set([1, 2, 3])
    s.add(4)
    assert s.contains(4)
    s.remove(3)
    assert not s.contains(3)
