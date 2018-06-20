for exponent in range(7,11):
    print(exponent, 10**exponent)

print("%6s"%"four")
print("%-6s"%"four")

for exponent in range(7,11):
    print("%-3d%12d" % (exponent, 10**exponent))