list = [1, 2, 10, 3, 0]
n = len(list)
print(n)
for i in range(0, n-1 ):
    for j in range(0, n -i-1 ):
        if list[j + 1] < list[j]:
            temp = list[j]
            list[j] = list[j + 1]
            list[j + 1] = temp

print(list)
