class SavingsAccount(object):
    """This class represents a savings account with the owner's name, PIN, and balance."""
    def __init__(self, name, pin, balance = 0.0):
        self._name = name
        self._pin = pin
        self._balance = balance
    
    def __lt__(self, other):
        return self._name < other._name
    def __gt__(self, other):
        return self._name > other._name
    def __eq__(self, other):
        return self._name == other._name


s1 = SavingsAccount("Ken", "1000", 0)
s2 = SavingsAccount("Bill", "1001", 30)
print(s1<s2)
print(s1==s2)
print(s1>s2)
s3 = SavingsAccount("Ken", "1000", 0)
print(s1==s3)
s4 = s1
print(s4==s1)