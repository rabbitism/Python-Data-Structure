def GetWeeklyPay(hourlyWage, regularHours, overTimeHours):
    return hourlyWage*regularHours+overTimeHours*1.5*hourlyWage


if __name__ =="__main__":
    print(GetWeeklyPay(12.5,80,40))