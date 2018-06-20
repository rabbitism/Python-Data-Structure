def GetPi(iteration):
    sign = 1
    sum = 0
    for number in range(iteration):
        sum+=1/(2*number+1)*sign
        sign*=-1
    return sum*4

if __name__ =="__main__":
    iteration = int(input("How many iterations?"))
    print(GetPi(iteration))
