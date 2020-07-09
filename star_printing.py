
#1. for i in range(1,6):
#     for j in range(1,6):
#         print("*",end="")
#     print("")

#2.for i in range(1,6):
#     j=5
#     while j>0:
#         print(j,end="")
#         j -= 1
#     print("")

#3.for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print("")

#4.for i in range(5,0,-1):
    # for j in range(1,i+1):
    #     print(j,end="")
    # print("")

#5. for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end="")
#     print("")

# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(i,end="")
#     print("")

for i in range(0,6):
    for j in range(0,7):
        if((i==0 and j%3!=0)or (i==1 and j%3==0) or (i-j==2) or (i+j==8)):
            print("*",end="")
        else:
            print(" ", end=" ")
    print("")