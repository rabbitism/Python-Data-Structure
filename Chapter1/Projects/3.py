def totalTravel(initialHeight, timeOfBounce):
    sum = 0
    height = initialHeight
    for number in range(timeOfBounce):
        sum+=1.6*height
        height=0.6*height

    return sum

if __name__=="__main__":
    print(totalTravel(10,2))