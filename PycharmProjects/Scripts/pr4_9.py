N = int(input())
l = x = 1
c = 3
sum = 2
while c <= N:
    l, x = x, l + x
    sum += x
    c += 1
print(sum)

