list1 = [4, 3, 5, 7, 2, 0, 15, 12]
n = len(list1)


def insertion(list1):
    for i in range(0, n - 1):
        key = list1[i + 1]
        j = i
        while j >= 0 and key < list1[j]:
            list1[j + 1] = list1[j]
            j = j - 1
        list1[j + 1] = key
    return list1


print(insertion(list1))
