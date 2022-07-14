"""
########################################################
# --------------Advanced Python Arguments---------------
########################################################
# ------------  *args:Many Positional Arguments --------
########################################################
"""

#
# def my_func_1(a, b, c):
#     # do this with a
#     # Then do this with b
#     # finally do this with c
#     pass
#
#
# my_func_1(c=3, b=2, a=1)
#
#
# # Arguments with Default Values
#
# def my_func_2(a=1, b=2, c=3):
#     # do this with a
#     # Then do this with b
#     # finally do this with c
#     pass
#
#
# my_func_2()
# my_func_2(b=5)  # rest takes default values.
#
#
# # ---------------UNLIMITED Arguments:---------------
#
# def add_1(n1, n2):
#     return n1 + n2
#
#
# add_1(n1=5, n2=6)
#
#
# def add(*args):  # [*args] --> here * is important, and it stands to passing as many arguments as you like,
#     # most developer prefer "args" as "variable" with "*" that stand for arguments.
#     print(f"args[0]: {args[0]}")
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
#
# print(add(4, 8, 9, 5, 6, 8))  # 40
# print(add(2, 6, 7))  # 15
# print(add(9, 7, 6, 3, 4, 7, 10, 12, 85, 96, 45, 75, 89))  # 448


"""
########################################################
# --------------Advanced Python Arguments---------------
########################################################
# ------------  **kwargs:Many Keyword Arguments --------
########################################################
"""


def calculate(n, **kwargs):
    print(kwargs)
    # print(type(kwargs))
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(f"kwargs['add']: {kwargs['add']}")
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(9, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        # self.make = kw['make']
        self.make = kw.get("make")
        # self.model = kw["model"]
        self.model = kw.get("model")
        self.color = kw.get('color')
        self.seats = kw.get('seats')


# my_car = Car()
# my_car = Car(make="Nissan", model="GT-8")
# print(my_car.model)
# print(my_car.make)
my_car = Car(make="Nissan")  # It will give error.  --> [KeyError: 'model'] to avoid this :
# in code we use --> kw.get("variable_name") instead of kw["variable_name"]
print(my_car.make)
print(my_car.model)
our_car = Car(make="Mahindra", model="Thar", color="Red", seats=4)
print(our_car.model)
print(our_car.make)
print(our_car.color)
print(our_car.seats)

