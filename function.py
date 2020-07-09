# def greet_user(first_name,last_name):   # parameter
#     print(f"hi {first_name}{last_name}!")
#     print("are you coming from abroad")
#
#
# print("start")
# # greet_user("chetan"," Lohar") #  argument
# greet_user("Sara",last_name="Khan ")   # keyword argument and keyword argument always comes after position argument
# print("finish it!")

#------------------------------------------------------------------------------------------------------------------
# RETURN STATEMENT
# def square(number):
#      return number*number  # if we don't write any return function than it will show NONE error
#
# ans=square(4)
# print(ans)

#--------------------------------------------------------------------------------------------------------------------

# addition of two number
# def mysum(a, b):
#     return a+b
# a,b=eval(input("enter values"))
# print(mysum(a,b))
#---------------------------------------------------------------------------------------------------------------------
# compare first and last letter of string
# d1=input("enter any string:")
# def compare():
#     if(d1[0]==d1[-1]):
#         print("first and last are same")
#     else:
#         print("not matched ")
#
# compare()
#----------------------------------------------------------------------------------------------------------------------
#through other method
# d1=input("enter any string:")
# def first(d1):
#     return d1[0]
# def last(d1):
#     return d1[-1]
# if(first(d1)==last(d1)):
#     print("same")
# else:
#     print("not same")
#-----------------------------------------------------------------------------------------------------------------------

# swap two number
# def swap(a,b):
#     a,b=b,a
#     print(a,b)
#
# a,b=eval(input("enter two value:"))
# swap(a,b)
# print(a,b)
#-----------------------------------------------------------------------------------------------------------------------
# a,b=eval(input("enter two values:"))
#
# def swap():
#     global a,b
#     a,b=b,a
#     print('A:',a,'B:',b)
#
#
# swap()
# print('A:',a,'B:',b)
#-----------------------------------------------------------------------------------------------------------------------
# list is always global

# def update(list1):
#     for i in range(5):
#         list1[i]+=10
#     print(list1)
#
# list1=[1,2,3,4,5]
# update(list1)
# print(list1)

#-----------------------------------------------------------------------------------------------------------------------
# swaping with list

# def update(list1):
#     list1[0],list1[1]=list1[1],list1[0]
#     print(list1)
# list1=[100,200]
# update(list1)
# print(list1)
#-----------------------------------------------------------------------------------------------------------------------
# variable length
# def add (a,*b): # a=1  b=2-5(tuple)
#     c=a
#     for i in b:
#         c+=i
#     return c
#
# print(add(1,2,3,4,5))

# def add (*b):
#     c=0
#     for i in b:
#         c+=i
#     return c
# print(add(1,2,3,4,5))

#-----------------------------------------------------------------------------------------------------------------------
# def person(name,**data):     # name,*data{dictionary}
#     print(name)
#     print(data)
#
#     for i in data.keys():
#         print(i)
# person(name="chetan",age=32,department='lab',salary=23000)
#----------------------------------------------------------------------------------------------------------------------

# student=[]
# lenght=eval(input("enter no student:"))
#
# for i in range(0,lenght):
#
#     student.append(input("student name:"))
#
# print(student)
#
# student=[]
# lenght=eval(input("enter no student:"))
#
# for i in range(0,lenght):
#
#     student.append(input("student name:"))
#
# print(student)
#
# student.sort()
# print(student)
# issue


#----------------------------------------------------------------------------------------------------------------------
#example of module
# from maximum import maximums
#
# number=[12,34,56,1,4]
# print(maximums(number))

from numpy import *
