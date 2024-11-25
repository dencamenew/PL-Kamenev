def get_i(arr, el):
    return el , [i for i in range(len(arr)) if arr[i] == el]


a = [1, 2, 3, 4]
d = dict()
if len(a) == len(set(a)):
    print('Повторяющийся элементов нет')
else:
    b = set(a)
    for j in b:
        if a.count(j) > 1:
            print(get_i(a, j))


m = [1, 2 ,3 ,4 ,5 ,6, 7, 8]
for i in range(0, len(m)):
    if m[i] <= 15:
        m[i] = m[i] ** 2
print(m)
