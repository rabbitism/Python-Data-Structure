problemSize = 10000
counter = 0
while problemSize>0:
    problemSize = problemSize//2
    counter+=1
    print("%12d%15d" % (problemSize, counter))