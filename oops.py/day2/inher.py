# class Parent:
#     def __init__(self, name):
#         self.name = name

#     def house(self):
#         print("my house in kulathur")


# class Child(Parent):
#     def display(self):
#         print(self.name)

#     def house(self):
#         print("my housr in mamboyil")

#     def set_details(self, age, adress="none"):
#         self.age = age
#         self.adress = adress

#     def child(s):
#         print("name:" + s.name)
#         print("age:", s.age)
#         print("adress:" + s.adress)


# name = "yaser arafath"
# x1 = Parent(name)
# x1.house()
# x2 = Child(name)
# x2.house()
# x2.set_details(age=30)
# x2.child()

"""method or constructor override: child classil parent classile same name ulla method or constructor use cheythaal childile method or constrocter mathrame child object vach call aakkumbol work cheyyyullu  """
"ini base class ulla function koode venamenkil super().m or c vach call aakiya mathi"

# # multiple inheritance


# class Father:
#     def __init__(self):
#         super().__init__()
#         print("iam father")


# class Mother:
#     def __init__(self):
#         print("iam mother")


# class Child(Father, Mother):
#     def __init__(self):
#         super().__init__()
#         print("iam child")


# x1 = Child()

# multilevel
# operator overloading


# class Name:
#     def __init__(self, name):
#         self.name = name

#     def __add__(first, second):  # add operator overloading
#         name = first.name + " " + second.name
#         return name


# first_name = Name("yaser")
# second_name = Name("arafath")
# name = first_name.name + " " + second_name.name
# full_name = first_name + second_name
# print(name)
# print(full_name)

# print(f"my name is {name} ")


# class A:
#     def func(self):
#         print("class a")


# class B(A):
#     def func(self):
#         print("class b")

#     def superfunc(self):
#         super().func()


# obj = B()


# def new():
#     obj.superfunc()


# new()
