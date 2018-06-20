def swap(lyst, i, j):
    """Exchanges the items at position i and j."""
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp
    #or directly use lyst[i], lyst[j] = lyst[j], lyst[i]

def selectionSort(lyst):
    i = 0
    while i<len(lyst)-1:
        minIndex = i
        j=i+1
        while j<len(lyst):
            if lyst[j]<lyst[minIndex]:
                minIndex=j
            j+=1
        if minIndex !=i:
            swap(lyst, minIndex, i)
        i+=1

def bubbleSort(lyst):
    n = len(lyst)
    while n>1:
        i=1
        while i<n:
            if lyst[i]<lyst[i-1]:
                swap(lyst, i, i-1)
            i+=1
        n-=1

def insertionSort(lyst):
    i = 1
    while i<len(lyst):
        itemToInsert = lyst[i]
        j = i-1
        while j>=0:
            if itemToInsert<lyst[j]:
                lyst[j+1]=lyst[j]
                j-=1
            else:
                break
        lyst[j+1]=itemToInsert
        i+=1