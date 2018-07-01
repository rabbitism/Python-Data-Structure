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


# Quick Sort Sample Code
def quicksort(lyst):
    quicksortHelper(lyst, 0, len(lyst)-1)

def quicksortHelper(lyst, left, right):
    if left<right:
        pivotLocation = partition(lyst, left, right)
        quicksortHelper(lyst, left, pivotLocation-1)
        quicksortHelper(lyst, pivotLocation+1, right)

def partition(lyst, left, right):
    # Find the pivot and exchange it with the last item
    middle = (left + right)//2
    pivot = lyst[middle]
    lyst[middle] = lyst[right]
    lyst[right] = pivot
    # Set boundary point to first position
    boundary = left
    # Move items less than pivot to the left
    for index in range(left, right):
        if lyst[index] < pivot:
            swap(lyst, index, boundary)
            boundary+=1
    #Exchange the pivot item and the boundary item
    swap(lyst, right, boundary)
    return boundary



#Merge Sort


#from arrays import Array
def mergeSort(lyst):
    #lyst           list being sorted
    #copyBuffer     temporary space needed during merge
    copyBuffer = Array(len(lyst))
    mergeSortHelper(lyst, copyBuffer, 0, len(lyst)-1)

def mergeSortHelper(lyst, copyBuffer, low, high):
    #lyst           list being sorted
    #copyBuffer     temp space needed during merge
    #low, high      bounds of sublist
    #middle         midpoint of sublist
    if low<high:
        middle=(low+high)//2
        mergeSortHelper(lyst, copyBuffer, low, middle)
        mergeSortHelper(lyst, copyBuffer, middle+1,high)
        merge(lyst, copyBuffer, low, middle, high)

def merge(lyst, copyBuffer, low, middle, high):
    #lyst           list that is being sorted
    #copyBuffer     temp space needed during the merge process
    #low            beginning of first sorted sublist
    #middle         end of first sorted sublist
    #middle+1       beginning of second sorted sublist
    #high           end of second sorted sublist

    #initialize i1 and i2 to the first items in each sublsit
    i1=low
    i2=middle+1

    #interleave items from the sublists into the copyBuffer in such away that order is maintained.
    for i  in range(low, high+1):
        if i1>middle:
            copyBuffer[i]=lyst[i2]#first sublist exhausted
            i2+=1
        elif i2>high:
            copyBuffer[i]=lyst[i1] # second sublist exhausted 
            i1+=1
        elif lyst[i1]<lyst[i2]:
            copyBuffer[i]=lyst[i1] # item in first sublist is smaller
            i1+=1
        else:
            copyBuffer[i]=lyst[i2] # item in second subllst is smaller
            i2+=1
    
    for i in range(low, high+1):
        lyst[i]=copyBuffer[i]