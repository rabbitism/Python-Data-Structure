lyst = [20,44,48,55,62,66,74,88,93,99]
def binarySearch(target, lyst):
    left = 0
    right = len(lyst)-1
    while left<= right:
        mid = left+(right-left)//2
        print("%10s%10d%10d%10d%10d"%("Target:",target, lyst[left], lyst[mid], lyst[right]))
        if target == lyst[mid]:
            return lyst[mid]
        elif target> lyst[mid]:
            left = mid+1
        else: 
            right = mid-1
    return -1

if __name__ == "__main__":
    print(binarySearch(100, lyst))
    print(binarySearch(44, lyst))