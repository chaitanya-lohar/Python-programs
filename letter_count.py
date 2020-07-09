string ="hello this is my first project and you are my first student"
dic1={}
string1=list(string)
# print(string1)

for data in string1:
    if(data in dic1):
        dic1[data]+=1
        # print(dic1)
    else:
        dic1[data]=1
for letter,count in dic1.items():
    print(letter,":",count)

