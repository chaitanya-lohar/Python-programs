from numpy import *
# arr1=array([11,2,3,4,5,6])
# print(arr1)
# print(type(arr1))
# print(arr1.dtype)
#--------------------------------------------------
#1. linspace
#2. array
#3. logspace
#4.Arange
#5. zeros
#6.ones

#--------------------------------------------------------
#2. linspace divide default(50)

# arr2=linspace(0,10,5) # 0,10 range , 4 equal parts
# print(arr2)
#-------------------------------------------------------
#3. logspace
# arr3=logspace(0,50,5)
# print(arr3)
#---------------------------------------------------------
#4. Arange
# arr4=arange(1,15,2)
# print(arr4)

#------------------------------------------------------

#5 zeros and ones
# arr5=ones(5,float)
# print(arr5)
#------------------------------------------------------

# arr1=array([1,2,3,4,5])
# arr2=array([6,7,8,9,10])
# arr3=arr1+arr2  # vectorized operation
# print(arr3)
# print(concatenate([arr1,arr2]))
# arr4=[1,2,3,4,5]
# arr5=[6,7,8,9,10]
# arr6=arr4+arr5  # vectorized operation only work on array not on list
# print(arr6)

#-----------------------------------------------------------------------
# angle=array([0,30,45,60,90])
# angle=angle*3.14/180
# print(sin(angle))
# print(cos(angle))
# print(tan(angle))

#----------------------------------------------------------------------
# arr1=array([1,2,3,4,5,6,7,8,9])
# print(arr1**2)
# print(sqrt(arr1))
# print(min(arr1))
# print(max(arr1))
# print(sum(arr1))
# print(len(arr1))
# print(arr1[::-1]) # reverse of array
# print(sort(arr1))

#---------------------------------------------------------------------
# arr1=array([1,2,3,4,5,6])
# arr=arr1   # shallow copy allias of arr1
# print(id(arr))   # base address
# print(id(arr1))  # base address  same in both id
#
# arr1[3]=100
# print(arr1)
# print(arr)
#--------------------------------------------------------------------
# arr1=array([1,2,3,4,5,6])
# arr2=arr1.copy() # deep copy
# print(id(arr1))  # both id are different means 2 memory block
# print(id(arr2))                                                      # id and type is called self intro inspection
# arr1[0]=100
# print(arr1)
# print(arr2)
#--------------------------------------------------------------------
#types of copy

#1 Shallow copy (change in one list affects other list, same id of both list)

# arr2 = arr1
# #or
# arr2 = arr1.view()

#2 Deep copy (change in one does not reflect on other list, diff id)

# arr2 = arr1.copy()
#--------------------------------------------------------------------
# arr=array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr)
# for i in range(3):
#     for j in range(3):
#         print(arr[i][j],end="")
#     print()
#------------------------------------------------------------
# arr1 = array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
# print(type(arr1))
# print(arr1.dtype)
# print(arr1.ndim)
# print(arr1.reshape(2,6))
# print(arr1.reshape(6,2))
# print(arr1.size)
# arr2=arr1.flatten() # to convert 2D array to 1D array
# print(arr2)
# arr5 = array([[1,2,3],[4,5,6],[7,8,9]])
m=matrix('1 2 3;4 5 6 ;7 8 9')
print(m)
print(m.diagonal())
print(m.min())
print(m.max())
print(m.sum())
print(m.dot(2))
m1=matrix('1 2 3;4 5 6 ;7 8 9')
m2=m1+m  # vectorized operation
print(m2)
