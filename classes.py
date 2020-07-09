# class

# class Demo():
#     def move(self):
#         print("move")
#     def draw(self):
#         print("draw")
# demo1=Demo()    # demo() is a class , and demo1 is variable who is receiving object
# demo1.draw()
# demo1.move()
# demo1.x=100
# print(demo1.x)
# demo2=Demo()
# demo2.x=10
# demo2.y=20
# print(demo2.x)
# print(demo2.y)

#------------------------------------------------------------------------------------------------------------------------

# constructor
# constructor is a function that gets called at the time of creating an object

# class Demo():
#     def __init__(self,x,y):  # self is reference of object
#
#         self.x=x        # self.x is a method to initialize value to the object
#         self.y=y        #""""""""""""""""""""
#
# demo1=demo(10,20)
# print(demo1.x)
# print(demo1.y)


#----------------------------------------------------------------------------------------------------------------------
# exercise

# class Demo():
#     def __init__(self,name):  # => this is contructor
#         self.name=name
#     def talk(self):              # => this is method
#         print(f"Hi! i am {self.name}")
#
#
# person=Demo("chetan")
# print(person.name)
# person.talk()