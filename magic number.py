
# strong number

num=input("Enter any value:")
save=int(num)
# print(num)
n=sum(map(int,str(num)))
n1=str(n)
n2=int(n1[::-1])
# print(n2)
cal=n * n2
print(cal)
if(cal==save):
    print("STRONG NUMBER")
else:
    print("NOT STRONG NUMBER")

#---------------------------------------------------------------------------------------------------------------------
#