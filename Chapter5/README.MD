# INTERFACES, IMPLEMENTATIONS AND POLYMORPHISM
When programmers use a software resource, they need only be concerned with its interface - the set of methods, functions, and data type names available to them. Ideally, the details of how this resource is implemented - the underlying algorithmic code and data structures - lie hidden or encapsulated within an abstraction barrier. The barrier that separates an interface from an implementation
* Flatterns the learning curve for a resources's user
* Allows users to quickly gue resources together in a plug-and-play fashion
* May give users the opportunity to choose among alternative implementation without diturbing its users' code
* Allows implementers to make changes to a resource's implementation without disturbing its user's code

## DEVELOPING AN INTERFACE
### Designing the Bag Interface
The methods in a resource's interface express the behavior of that resource, the kinds of things it does, or the things that you can do to it. 

Draw up a list of function names, method names, and operator sym-bols that meet the descriptions of these operations. These anmes typically are whole words or abbreviations of the actions performed or the properties being examined. 

### Specifying arguments and regurn values
The next refinement is to add argument to the operations in the interface and to think about what values, if any, they return. Illustrate them as following:
```python
b.clear()
for item in range(10):
    b.add(item)
print(b)
print(4 in b)
c=b+b
print(len(c))
for item in c:
    print(item)
for item in range(10):
    c.remove(item)
print(c==b)
```

Arguments for Bag Operations and Their Methods

|User's Bag Operation|Method in a Bag Class|
|:--|:--|
|`b=<class name>(<optional collection>)`|`__init__(self, sourceCollection==None)`|
|`b.isEmpty()`|`isEmpty(self)`|
|`len(b)`|`__len__(self)`|
|`str(b)`|`__str__(self)`|
|`for item in b:`|`__iter__(self)`| 
|`item in b`|`__contains__(self, item)`**Not needed if `__iter__` is included**|
|`b1+b2`|`__add__(self, other)`|
|`b==anyObject`|`__eq__(self, other)`|
|`b.clear()`|`clear(self)`|
|`b.add(item)`|`add(self, item)`|
|`b.remove(item)`|`remove(self, item)`|

### Constructors and Implementing Classes
`b=<class name>(<optional collection>)`is the constructor for the particular type. the method is always `__init__`. This method takes an optional source collection as an argument, which defaults to None. This allows the user to create either an empty bag or a bag with the contents of another collection.

### Preconditions, Postconditions, Exceptions, and Documentation
The final step is to describe clearly and concisely what each mehtod does. This description incldues not only what you expect to occur under normal conditions, but also what will happen when something abnormal, such as error, occurs. Such description are brief and deal only with what a method does, not with how it does it. 

`docstring` is a string enclosed in triple quotes that will displayed when Python's help function is run on a resource.

A more detailed form of documentation can include preconditions and postconditions

A **precondition** is a statement of what must be true of a method to perform its actions correctly. 
A **postcondition**states what will be true after the method completes execution, assuming that its preconditions are also true.
Documentation in an interface should also include a statement of any exceptions that could be raised, usually as the result of the failure to adhere to the preconditions of a method.

Sample:
```python
def remove(self, item):
    """Precondition: item is in self.
    Raises: KeyError if item is not in self
    Postcondition: item is removed from self."""
```

See full sample code [here](/Chapter5/baginterface.py)

## DEVELOPING AN ARRAY-BASED IMPLEMENTATION
