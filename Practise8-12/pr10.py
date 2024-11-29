f = open('Pr10_1.txt').readlines()
res = open('Result10_1.txt', 'w')
a = [[int(j) for j in i.split()] for i in f]
for i in range(0, len(a)):
    if i % 2 == 0:
        res.write(str(min(a[i])) + '\n')




arr = [[int(j) for j in i.split()] for i in open('Pr10_2.txt').readlines()]
max_value_index = [0, 0]
min_value_index = [0, 0]
max_value = -1000
min_value = 1000

for i in range(len(arr)):
    for j in range(i, len(arr[i])):
        n = arr[i][j]
        if n < min_value:
            mi = n
            min_value_index[0] = i
            min_value_index[1] = j
        elif n > max_value:
            max_value = n
            max_value_index[0] = i
            max_value_index[1] = j

arr[max_value_index[0]].insert(max_value_index[1], min_value)
arr[max_value_index[0]].pop(max_value_index[1] + 1)
arr[min_value_index[0]].insert(min_value_index[1], max_value)
arr[min_value_index[0]].pop(min_value_index[1] + 1)

res1 = open('Resulr10_2.txt', 'w')
for i in arr:
    res1.write(' '.join(map(str, i)) + '\n')