from array import *
# arr=array('i',[1,2,3,4,4,5,6,7])

# print(arr.buffer_info())  # base address and cout of element
# for i in arr:
#     print(i)

# for i in range(0,len(arr)):
#     print(i,':',arr[i])
#-------------------------------------------------------------------------------------------------------------------------

# arr=[]
# n=int(input("size of array:"))
#
# for i in range(0,n):
#     arr.append(int(input("enter values:")))
# print(arr)
#
# data=int(input("enter searching data:"))
# if data in arr:
#     print("data found")
# else:
#     print("data not found")
#---------------------------------------------------------------------------
# for i in range(0,len(arr)):
#     if data == i:
#         print("data found at index number:",arr.index(i))
#     else:
#         print("not found")
#----------------------------------------------------------------------------
# arr=[]
# n=int(input("enter number of element:"))
#
# for i in range(0,n):
#     arr.append(int(input("enter values:")))
# print(arr)
# deleted=int(input("enter deleted element:"))
# if deleted in arr:
#     # if i==deleted:
#     print("yes found:",arr.index(deleted))
#     arr.remove(deleted)
#     print(arr)
#
# else:
#     print("not found")
#--------------------------------------------------------------------------------------------------------------------
# list1=[1,2,3,4,5,6,7,4,3,3,2,1,5,6]
# list2=[11,22,33,44,55,66,77]
# list3=list1+list2
# print(list3)
# for data in list1:
#     print(data,":",list1.count(data))
# list2=[]
# for data in list1:
#     if data not in list2:  # this is to remove duplicate value
#         list2.append(data)
# print(list2)
#----------------------------------------------------------------------------------------------------------------------
list1=[1,2,3,4,5]
list2=[]

# for data in list1:
#     list2.append(data**2)
# print(list2)

# list2=list(map(lambda a:a**2,list1))
# print(list2)

from functools import reduce
list2=reduce(lambda a,b:b+a,list1)
print(list2)

list2=list(filter(lambda a:a%2==0,list1))
print(list2)

# min from array
list2=min(list1)
print(list2)
# max from array
list2=max(list1)
print(list2)