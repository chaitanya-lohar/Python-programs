# class Demo:
#     pass
#
#
# obj1=Demo()
# obj2=Demo()
# obj1.name="chetan"
# obj1.std="1st year"
# obj1.place="udaipur"
# print(obj1.__dict__)
# obj2.name="rajesh"
# obj2.std="2nd year"
# obj2.place="ajmer"
# print(obj2.__dict__)
#------------------------------------------------------------------------
# calling of function in class
# class demo:
#     def demo1(self):
#         print("Hi ! i am in class demo")
#
# obj1=demo()
# obj1.demo1() # first method of calling
# demo.demo1(obj1)  # second method of calling
#-------------------------------------------------------------------------
# class Demo:
#     def funtion1(self,name,age,college):   #name ,age, college are instant variable or instant method(function)
#         self.name=name
#         self.age=age
#         self.college=college
#         print(self.name,self.age,self.college)
#
# obj1=Demo()
# obj1.funtion1("chetan",23,"Aishwariya")
#-----------------------------------------------------------------------------
# class demo:
#     def getdata(self):
#         self.a,self.b=int(input("enter first values:")),int(input("enter second value:"))  # dynamic assignment
#     def putdata(self):
#         print("addition of two values:",self.a+self.b)
#
# obj1=demo()
# obj1.getdata()
# obj1.putdata()
#-----------------------------------------------------------------------------
#  factorial of given value:

# class demo:
#     def getdata(self):
#         self.n=int(input("enter any value:"))
#
#     def putdata(self):
#         print("entered value is:",self.n)
#     def calculation(self):
#         fact=1
#         for i in range(1,self.n+1):
#
#             fact=fact*(i)
#
#         print(f"factorial of given number:{self.n} is {fact}")
#
# obj1=demo()
# obj1.getdata()
# obj1.putdata()
# obj1.calculation()
#----------------------------------------------------------------------
