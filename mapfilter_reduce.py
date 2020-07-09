
def demo(data):
    global list2
    # data1=str(data)
    i=1
    while(i):
        data=data+1

        data2=str(data)
        data3=data2[::-1]
        if int(data2)==int(data3):
            list2.append(int(data2))
        break

list2 = []
list1=[]

n=int(input("enter total count of element:"))
for i in range(n):
    list1.append(int(input("insert value:")))
print(f"entered list",list1)

for data in list1:

    if data<10:
        print("palindrome number")
    else:
        demo(data)
print("palindrome list", list2)