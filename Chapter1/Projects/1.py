import math

radius = float(input("Please enter sphere radius:"))
diameter = radius*2
circumference = 2*math.pi*radius
area = 4*math.pi*radius**2
volume = 4/3*math.pi*radius**3

print("Diameter:", diameter)
print("Circumference:", circumference)
print("Area:", area)
print("Volume:",volume)