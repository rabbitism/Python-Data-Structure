def square(n):
    """REturns the square of n."""
    result = n**2
    return result

print(square(10))

def DisplayRange(lower, upper):
    """Output the numbers from lower to upper."""
    while lower<= upper:
        print(lower)
        lower+=1

DisplayRange(1,10)

def RecursiveDisplayRange(lower, upper):
    """Output the numbers from lower to upper with recursive function"""
    if lower<=upper:
        print(lower)
        RecursiveDisplayRange(lower+1, upper)

RecursiveDisplayRange(15,16)

def ourSum(lower, upper):
    """Returns the sum of the numbers from lwoer thru upper."""
    if lower> upper:
        return 0
    else:
        return lower+ourSum(lower+1, upper)

print(ourSum(1,10))

#Nested Function
def factorial(n):
    """Returns the factorial of n."""
    def recurse(n, product):
        if n==1: return product
        else: return recurse(n-1, n*product)
    recurse (n,1)

def factorial(n, product=1):
    if n==1: return product
    else: return factorial(n-1, n*product)

print(factorial(10))
print(factorial(10, 1)) 