list = [1, 2, 3, 4]
new_list = (
    list  # this is same list so if operqation on one list changee value to other list
)
new_list.append(5)
new_list2 = list.copy()
new_list2.append(6)
new_list3 = list[:]  # slicing method
new_list4 = [i for i in list]  # list comprehension method
list.append(7)


print(
    list,
    new_list,
    new_list2,
    new_list3,
    new_list4,
)
