N = int(input())
l = x = 1
c = 3
s = 2
while c <= N:
    l, x = x, l + x
    s += x
    c += 1
print(s)