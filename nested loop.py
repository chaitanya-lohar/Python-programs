# 1 print 1 to 1001 prime number
# for j in range(1,101):
#     num=j
#     cout=0
#     for i in range(1,num+1):
#         if(num%i==0):
#             cout+=1
#     if(cout==2):
#         print(num,end=":")
#------------------------------------------------------------------------------------------------------------------------
# 2 print 1 to 1001 perfect number
# for j in range(1,1001):
#     num=j
#     sum=0
#     for i in range(1,num):
#         if(num%i==0):
#             sum=sum+i
#     if(sum==j):
#         print(j)

#-----------------------------------------------------------------------------------------------------------------------
# 3 print 1 to 1001 armstrong number

# for j in range(1,1001):
#     num = j
#     s=0
#     while(num>0):
#         r=num%10
#         s=s+r**3
#         num=num//10
#     if (j == s):
#         print(j, end=":")

#----------------------------------------------------------------------------------------------------------------------
 # 4 print 1 to 1001 palindrome number
# for j in range(1,1001):
#     num=j
#     s=0
#     while(num>0):
#         r=num%10
#         s=s*10+r
#         num=num//10
#     if(j==s):
#         print(j,end=":")

#-----------------------------------------------------------------------------------------------------------------------

# 5. print 1 to 1001 strong number

# for j in range(1,1001):
#     num=j
#     sum=0
#     while(num>0):
#         fact=1
#         r=num%10
#
#         for i in range(1,r+1):
#             fact=fact*i
#
#         sum=sum+fact
#         num = num // 10
#     if(sum==j):
#         print(j,end=":")

#-----------------------------------------------------------------------------------------------------------------------
#6. print 1 to 1001 magical number
# for i in range(1,1730):
#     num=str(i)
#     total=sum(map(int,str(num)))
#     n1=str(total)
#     n2=int(n1[::-1])
#     cal=total*n2
#     if(cal==i):
#         print(i,end=":")
