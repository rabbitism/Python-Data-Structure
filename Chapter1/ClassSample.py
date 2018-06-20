class Counter(object):
    """Models a counter."""

    #Class variable
    instances = 0

    #Constructor
    def __init__(self):
        """Sets up the counter."""
        Counter.instances+=1
        self.reset()
    
    #Mutator methods
    def reset(self):
        """Sets the counter to 0."""
        self.__value = 0
    def increment(self, amount=1):
        """Adds amount to the ocunter."""
        self.__value += amount
    def decrement(slef, amount=1):
        """Substracts amount from the counter."""
        self.__value -= amount
    
    # Accessor methods
    def getValue(self):
        """Returns the counter's value."""
        return self.__value

    def __str__(self):
        """Return the string representation of the counter."""
        return str(self.__value)

    def __eq__(self, other):
        """Returns True if self equals other, or False otherwise."""
        if self is other: return True
        if type(self) != type(other): return False
        return self.__value==other.__value


c1 = Counter()
print(c1)
print(str(c1))
c1.increment()
print(c1)
c1.increment(5)
print(c1)
c1.reset()
print(c1)
print(Counter.instances)
c2 = Counter()
print(Counter.instances)