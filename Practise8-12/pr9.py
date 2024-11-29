def rev(string):
    if string == '':
        return string
    else:
        return rev(string[1:]) + string[0]


print(rev('привет'))




def every_second():
    n = int(input())
    if n == 0:
        return
    m = int(input())
    if m == 0:
        return
    else:
        print(m)
    every_second()

every_second()

