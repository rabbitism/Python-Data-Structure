# BASIC PYTHON PROGRAMMING
## BASIC PROGRAM ELEMENTS
### Programs and Modules
A Python program consists of one or more modules. A module is just a file of Python code, which can include statements, function definitions, and class definitions. 

### An Example Python Program: Guessing a Number
See Sample Code [here](Chapter1/GuessNumber.py).

### Programming Comments
Single line comments start with #
Multiline commoents is enclosed in triple single quotes or triple double quotes. Such comments are also called docstrings, to indicate that they can document major constructs within a program. 
```python
# This is an end-of-line comment
'''This is a multiline comment
with many lines'''
"""This is another multiline comment 
with many lines"""
```

### Naming Convention
|Type of Names|Example|
|:---|:---|
|Variable|`salary`, `hoursWorked`, `isAbsent`|
|Constant|`ABSOLUTE_ZERO`, `INTEREST_RATE`|
|Function or method|`printResults`, `cubeRoot`, `isEmpty`|
|Class|`BankAccount`, `SortedSet`|

### Syntactic Elements
Python uses white space (spaces, tabs, or line breaks) to mark the syntax of many types of sentences. This means that indentation and line breaks are significant in Python code. 

### Literals
Numbers(integers and floating-point numbers) are written as they are in other programming languages. The Boolean values `True` and `False` are keywords.

### String Literals
See sample of string print [here](Chapter1/StringLiterals.py).

### Operators and Expressions
|Type|Example|Comments|
|:---|:---|:---|
|Arithmic standard operators|+, -, *, /|+ means concatenation when used with collections|
|Comparison operators|<, <=, >=, ==, !=|works with numbers and strings|
|Logical Operators|`and`, `or`, `not`|`0`, `None`, empty string, list are `false`|
|Subscript operator|[]||
|Selector operator|.|used to refer to a named item in a module, class, or object|

The operators have a standard precedence (selector, function call, subscript, arithmetic, comparison, logical, assignment.)

The `**` and `=` operators are right associative, whereas the others are left associative

### Function Calls
Functions are called in the usal manner
```Python
min(5,2) #Returns 2
```

### The print Function
The standard output function `print` displays its arguments on the console. By default, `print` terminates its output with a newline.

### The input Function
The standard input function `input` waits for the user to enter text at the keyboard. When the user presses the Enter key, the function returns a string containg the characters entered. 

### Type COnversion Functions and Mixed-Mode Operations
See sample code [here](Chapter1/TypeConversion.py).

### Optional and Keyword Function Argument
Functions may allow optional arguments. Required arguments have no default values, Optional arguments have default values and can appear in any order when their keywords are used, as long as they come after the required arguments.

### Variables and Assignment Statements
```python
<identifier>=<expression>
PI = 3.1416
```
Several variables can be introduced in the same assignment statement:
```python
minVaue, maxValue = 1, 100
```

### Python Data Typing
In Python, any variable can name a value of any type. Variables are not declared to have a type. 

### Import Statements
Several ways of using import statement
```python
import math
from math import sqrt
from math import pi, sqrt
```

## CONTROL STATEMENTS
### Conditional Statements
keyword: `if`, `elif`, `else`
Syntax: 
```python
if<Boolean expression>:
    <sequence of statements>
elif<Boolean expression>:
    <sequence of statements>
else:
    <sequence of statements> ## There is a indentation typo in the book. 
```

### Loop Statements
keyword: `while`, `for <~> in <~>`
Syntax:
```python
while <Boolean expression>:
    <sequence of statements>

for <variable> in <iterable object>:
    <sequence of statements>
```

## STRINGS AND THEIR OPERATIONS
### Operators
When comparing strings, the pairs of characters at each position are compared using ASCII ordering. 

The subscript operator can be used to return the character at that position
```python
"greater"[0] #returns "g"
```
slice
the slice returns a substring starting with the character at the lower index and ending with the character at the upper index minus 1.
```python
"greater"[:] #returns "greater"
"greater"[2:] #returns "eater"
"greater"[:2] #returns "gr"
"greater"[2:5] #returns "eat"
```

### Formatting Strings for Output
See sample code [here](Chapter1/StringFormatting.py)

##  BUILT-IN PYTHON COLLECTIONS AND THEIR OPERATIONS
### Lists
A list is a sequence of zero or more Python objects, commonly called items. Use square brackets to enclose, separated by commas.
```python
[]                          # An empty list
["greater"]                 # A list of one string
["greater", "less"]         # A list of two strings
["greater", "less", 10]     # A list of two strings and an int
["greater", ["less", 10]]   # A list with a nested list
```
Most commonly used list methods: `append`, `insert`, `pop`, `remove`, `sort`
For String: `split`, `join`

### Tuples
A tuple is an **immutable** sequence of items. Enclosed in parentheses, must include at lest two items. 

### Loops Over Sequences
```python
testList = [67, 100, 22]
for item in testList:
    print(item)

for index in range(len(testList)):
    print(testList[index])
```

### Dictionaries
A dictionary contains zero or more entries. Each entry associates a unique key with a value. Keys are typically strings or intergers, whiereas values are any Python objects.

A dictionary literal encloses the key-value entries in a set of braces.
```python
{}
{"name":"Ken"}
{"name":"Ken", "age":61}
{"hobbies":["reading", "running"]}
```

### Searching for a Value
use `in` operator with the value and the collection. The target value for a dictionary should be a potential key.
When it is known that a given value is in a sequence, the index method returns the position of the **first** such value.
For dictionaries, the methods `get` and `pop` can take two arguements: A key and a default value. 

### Pattern Matching with Collections
Omitted.

## CREATING NEW FUNCTIONS
### Function Definitions
Syntax:
```python
def <function name>(<list of parameters):
    <sequence of statements>
```
See naming convention [here](#Naming Convention).
