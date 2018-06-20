def indexOfMin(lyst):
    minIndex = 0
    currentIndex = 1
    while currentIndex<len(lyst):
        if lyst[currentIndex]<lyst[minIndex]:
            minIndex = currentIndex
        currentIndex+=1
    return minIndex

def sequentialSearch(target, lyst):
    position = 0
    while position < len(lyst):
        if target == lyst[position]:
            return position
        position +=1
    return -1

def binarySearch(target, sortedLyst):
    left = 0
    right = len(sortedLyst) -1
    while left<=right:
        mid = (left+right)//2 #This can be optimized to avoid int overflow
        if target == sortedLyst[mid]:
            return mid
        elif target < sortedLyst[mid]:
            right=mid-1
        else: 
            left = mid+1
    return -1



if __name__ == "__main__":
    lyst = [2,3,4,1,5,6,7,8]
    print(indexOfMin(lyst))
    print(sequentialSearch(6, lyst))
    lyst2 = range(1,100)
    print(binarySearch(25, lyst2))