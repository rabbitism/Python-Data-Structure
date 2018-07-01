from counter import Counter

def fib(n):
    if n<3:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def fib2(n, counter):
    """Count the number of iterations in the Fibnacci functions"""
    sum = 1
    first = 1
    second = 1
    count = 3
    while count<=n:
        counter.increment()
        sum = first+second
        first = second
        second = sum
        count +=1
    return sum


if __name__ == "__main__":
    problemSize = 2
    counter = Counter()
    print("%12s%15s" % ("ProblemSize","Iterations"))
    for count in range(20):
        fib2(problemSize, counter)
        
        print("%12d%15d" % (problemSize, counter.getValue()))
        counter.reset()
        problemSize*=2
