k = int(input())
for i in range(1, k + 1):
    s = sum([int(j) ** len(str(i)) for j in str(i)])
    if s == i:
        print(i)


def f(x1, x2, y1, y2, z1, z2):
    tan1 = abs(x2 / x1)
    tan2 = abs(y2 / y1)
    tan3 = abs(z2 / z1)
    if min(tan1, tan2, tan3) == tan1:
        print(f'X: {x1, x2}')
    elif min(tan1, tan2, tan3) == tan2:
        print(f'Y: {y1, y2}')
    else:
        print(f'Z: {z1, z2}')


print(f(5, 4,2,7,1,1))