problemSizes = [1000, 2000, 4000, 10000, 100000]

for problemSize in problemSizes:
    counter = 0
    size = problemSize
    while size>0:
        size = size//2
        counter+=1
    print("%12d%15d" % (problemSize, counter))