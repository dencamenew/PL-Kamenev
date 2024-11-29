a = [[1, 2, 3, 4],
     [3, 4, 5, 6],
     [9, 12]]
for i in range(0, len(a)):
    if i % 2 == 0:
        print(min(a[i]))




arr = [[1, 2, 3, 4, 5, 6, 7],
     [8, 10, 11, 12, 13, 14, 15],
     [16, 17, 18, 19, 20, 21, 22]
     ]
max_value_index = min_value_index = [0, 0]
max_value, min_value = -100, 100
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

print(arr)
