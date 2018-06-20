from counter import Counter

def fib(n, counter):
    counter.increment()
    if(n<3): 
        return 1
    else:
        return fib(n-1, counter)+fib(n-2, counter)

problemSize = 2
print("%12s%15s" % ("Problem Size", "Calls"))
for count in range(6):
    counter = Counter()
    fib(problemSize, counter)

    print("%12d%15s" % (problemSize, counter))
    problemSize*=2
