# class Dog:
#     def walk(self):
#         print("dog")    # if here there is numbers of line of code and we want to use it in another class then we can
#                         # inheritance method
#                         # ******* using same/ duplicate methods and code its not sign of good programmer
# class Cat:
#     def walk(self):
#         print("cat")


# --------------------------------------------------------------------------------------------------------------------
# using inhertinance property

# class Mammal:
#     def talk(self):
#         print("talk method")
#     def walk(self):
#         print("Mammals class and dog class")
#
#
# class Dog(Mammal):
#     pass                       # python doesn't like any empty class if we will set as a empty then it will red
#                                 #    on next class name , so pass is a method which define nothing but it satisfy python
#
#
# class Cat(Mammal):
#     def be_annoying(self):
#         print("annoying")
#
#
# dog1 = Dog()
# dog1.talk()
# dog1.walk()
# cat1 = Cat()
# cat1.be_annoying()


# ----------------------------------------------------------------------------------------------------------------------
# another example

# class Father:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#         print(f"addition of two number:{a+b}")


# class Child(Father):
#     def display(self):
#         # super().getdata()
#         print(f"addition of two values are:{a + b}")


# demo1 = Father(100,200)
# ----------------------------------------------------------------------------------------------------------------------
# example of single inheritance
# class Parent:
#     def getata(self):
#         a,b,c=eval(input("enter three subject marks"))
#         self.a=a
#         self.b=b
#         self.c=c
#
#     def sum(self):
#         self.total = self.a + self.b + self.c
#         return self.total
#
# class Student(Parent):
#
#     def sum(self):
#         self.total = self.a + self.b + self.c
#         return self.total
#
# demo1 = Student()
# demo1.getata()
# total=demo1.sum()
# print(total)

# -----------------------------------------------------------------------------------
# example of multilevel inheritance

# class grand_parent:
#     def __init__(self):
#         a,b,c=eval(input("enter three values:"))
#         self.a=a
#         self.b=b
#         self.c=c
# class parent(grand_parent):
#     def putdata(self):
#         print(f"value of first:{self.a},value of second:{self.b},value of third:{self.c}")
#
# class child(parent):
#     def avg(self):
#         self.avg1=self.a+self.b+self.c/3
#         return self.avg1
# obj1=child()
# obj1.putdata()
# # obj1.avg()
# print(obj1.avg())
# ---------------------------------------------------------------------------------------------
# example of multiple inheritance
class grand_parent:
    def __init__(self):
        print("show of grand parent")

class parent:
    def __init__(self):
        print("show of parent")
        super(parent, self).__init__()



class child(parent,grand_parent):
    def __init__(self):
        print("show of child")
        super().__init__()




obj1 = child()
#----------------------------------------------------------------------------------
# Hierarchial inheritance
# class grand_parent:
#     def __init__(self):
#         print("show of grand parent")
#
#
# class parent(grand_parent):
#     def __init__(self):
#         print("show of parent")
#         super().__init__()
#         # super(parent, self).__init__()
#
# class child(grand_parent):
#     def __init__(self):
#
#         print("show of child")
#         super().__init__()
#         # super(child, self).__init__()
#
# obj1=child()
# obj2=parent()