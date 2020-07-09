# PRIME NUMBER
# num=int(input("enter any number:"))
# cout=0
# for i in range(1,num+1):
#     if(num%i==0):
#       cout+=1
# if(cout==2):
#     print("entered number is Prime number")
# else:
#     print("not Prime number")

#----------------------------------------------------------------------------------------------------------------------
# PERFECT NUMBER

# num=int(input("Enter any number:"))
# sum=0
# for i in range(1,num):
#     if(num%i==0):
#         sum=sum+i
# print(sum)
# if(sum==num):
#     print("PERFECT NUMBER")
# else:
#     print("NOT PERFECT NUMBER")

#----------------------------------------------------------------------------------------------------------------------

# PALINDROME NUMBER

# num=int(input("enter any number:"))
# s=0
# save=num
# while(num!=0):
#     r=num%10
#     s=s*10+r
#     num=num//10
# if(s==save):
#     print("PALINDROME NUMBER")
# else:
#     print("NOT PALINDORM NUMBER")

#----------------------------------------------------------------------------------------------------------------------

# FACTORIAL OF GIVEN NUMBER

# num=int(input("enter any number:"))
# i=1
# fact=1
# while(i<=num):
#     fact=fact*i
#     i+=1
# print(f"FACTORIAL OF GIVEN NUMBER {num} is :",fact)
#----------------------------------------------------------------------------------------------------------------------

#ARMSTRONG NUMBER:
# num=int(input("enter any number:"))
# s=0
# save=num
# while(num!=0):
#     r=num%10
#     s=s+(r*r*r)
#     num=num//10
# if(s==save):
#     print("Given number is armstrong number")
# else:
#     print("NOT armstrong number")