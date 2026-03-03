# print("hello")
# print("hi")
# a = 10
# b = 20

# a = int(input("enter a number"))
# print(a + b)
# if a % 2 == 0:
#     print(str(a) + " is even")
# else:
#     print("odd")

# for i in range(0, 5, 2):
#     print(i)
# s = "hi iam"
# print(len(s))
# list = [1, "2", 3]
# print(list[0:-4])
# list.append(input("enter a list"))
# print(list)


# a = "Hello world"
# a[2] = "l"
# print(a[2])
# print(a.replace("H", "j"))

# num_rows = 5
# for i in range(1, num_rows + 1):
#     for j in range(num_rows - i):
#         print(" ", end="")
#     for k in range(i):
#         print("* ", end="")
#     print("")


def add1():
    a = 10
    b = 12
    sum = a + b
    print(sum)


# def add2(a=10, b=0):
#     a = 12
#     sum = a + b
#     print("sum", sum, "aan")


# def add3():
#     a = 10
#     b = 12
#     sum = a + b
#     return sum


# def add4(a, b):
#     sum = a + b
#     return sum


# add1()
# add2(b=20)

# sum = add3()
# print("sum:", sum)
# sum = add4(12, 32)
# print("sum:", sum)
# import exception

# print("...")

# print(__name__)

# print(exception.__name__)


# import math as m
# print(m.sqrt(2))
b = 10
try:
    a = 10/b
    print(a)

except ZeroDivisionError:
    print("not devided by zero")

