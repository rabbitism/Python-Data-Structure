import sort
import random

lyst = [1,3,2,4,7,6,5]
print(lyst)
sort.selectionSort(lyst)
print(lyst)
lyst = [1,3,2,4,7,6,5]
print(lyst)
sort.bubbleSort(lyst)
print(lyst)
lyst = [1,3,2,4,7,6,5]
print(lyst)
sort.insertionSort(lyst)
print(lyst)

lyst = []
for count in range(1000):
    lyst.append(random.randint(1, 20))
print(lyst)
sort.quicksort(lyst)
print(lyst)
