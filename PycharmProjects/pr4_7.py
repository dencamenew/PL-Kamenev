n = int(input())
sfac = 1
k = 1
for i in range(2, n + 1):
    k *= i
    sfac += k
print(sfac)