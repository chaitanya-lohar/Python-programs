string="this is my first page and may be second also is is is this this page first"
list1=string.split()
print(list1)

dic1={}

for data in list1:
    if data in dic1:
        dic1[data]+=1
    else:
        dic1[data]=1

for word,count in dic1.items():
    print(word,":",count)