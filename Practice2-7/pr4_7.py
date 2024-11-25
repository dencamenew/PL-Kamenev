n = int(input())
sfac = 1
fac = 1
for i in range(2, n + 1):
    fac *= i
    sfac += fac
print(sfac)