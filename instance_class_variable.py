# class Demo:
#     no_of_leaves=9  # class variable creates only a single copy
#
# obj1=Demo()
# obj2=Demo()
# obj1.name="chetan"
# obj1.deparment="computer science"
# # obj1.no_of_leaves=12
# obj2.name="rajesh"
# obj2.department="HR"
# # obj2.no_of_leaves=13
# Demo.no_of_leaves=10
# print(obj1.no_of_leaves)
# print(obj2.no_of_leaves)
# print(obj1.__dict__)
# print(obj2.__dict__)


#------------------------------------------------------------
# class car:
#     wheels=4
#     def __init__(self):
#         self.mil=5
#         self.comp="BMW"
#
# obj1=car()
# obj2=car()
# print(obj1.mil)
# print(obj1.comp)
# obj1.mil=24
# print(obj1.mil)
# print(obj2.mil)
# car.comp="hyudai"
# print(obj1.comp)
# print(obj2.comp)
#
# car.wheels=10
# print(car.wheels)
# print(obj1.wheels)
# print(obj2.wheels)
# print(car.wheels)