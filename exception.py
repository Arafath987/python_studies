# import hello
from enimy import Enimy, Zombie

# print(__name__)
# print(hello.__name__)
# hello.add1()
# print("helo")

name = "yaser"
# print(f"hello iam {name}")
set = {1, 2, 3, 4, 5}
# print(set)
j = -1
list = []
for i in set:
    j = j + 1
    list.append(i)

# print(list)

set.update([4, 5, 6, 9])
# print(set)


"list operations"

# zoo = ["lion", "ele", "tiger", "jaguar", "snake"]
# zoo.pop(3)
# print(zoo)
# zoo.append("jiraph")
# print(zoo)
# zoo.pop(0)
# print(zoo)
# print(zoo[0:3])

# "dictionsries"
# my_vehicle = {"model": "Ford", "make": "Explorer", "year": 2018, "mileage": 40000}

# for i, j in my_vehicle.items():
#     print(i, j)

# vehicle2 = my_vehicle.copy()
# vehicle2["number_of_tires"] = 4
# vehicle2.pop("mileage")
# print(vehicle2.keys())


# def color1():
#     color = "red"
#     return color


# color1()


# def details_fun(first_name="yaser", last_name="arafath", age=0):
#     dict = {"first name:": first_name, "last name:": last_name, "age:": age}
#     return dict


# details = details_fun("sreehari", "jayarj", 12)

# for i, j in details.items():
#     print(i, j)

# enimy = Enimy("yaser", 100, 10)
# print(f"health={enimy.health_points}\nhealth_of_enimy={100-enimy.attacking_damage}")
# print("after healing")
# enimy.health_points = 100
# print(f"health={enimy.health_points}\nhealth_of_enimy={100-enimy.attacking_damage}")
# enimy.type_of_enimy = "wukong"
# print(f"enimy_type:{enimy.type_of_enimy}")


"""abstraction"""

# enimy.attacking_damage = 100
# enimy.attack()
"""this abstraction has only function call,no body of the function"""

""" INHERITANCE """
# super
# INHERITANCE TYPE
zombie = Zombie(100, 10)
zombie.talk()
enimy = Enimy("yaser", 100, 10)
# enimy.talk()


def battle(e: Enimy):
    e.talk()
    e.attack()


battle(zombie)
battle(enimy)
