#number=(1,2,3)   in this we use [] this brackets and in tupes we use () this brackets
#
number=(1,2,3,4,2)
#count=number.count(2)
#print(count)
#->  number[0]=20 this will show that tuples doesn't support value assignment
#print(number)

#----------------------------------------------------------------------------------------------------------------------

#                               topic
# unpacking
#number=(1,2,3)
# assume that 1,2,3 are coordinates like a,b,c
# and you want to multiply it then what you will do ->
# a=number[0]
# b=number[1]
# c=number[2]
# print(a*b*c)
# but this is very  long method so we have another feature called unpacking
# number=(1,2,3)
# a,b,c=number   # this is short method called unpacking
# print(a*b*c)
#----------------------------------------------------------------------------------------------------------------------

#                           dictonaries

customer={
     'name':"john smith ",
     "age":40,
     "birthdate": "jan 1 1998",
     "department":"customer care"
 }
print(customer["name"])
customer["name"]="chetan"
print(customer.get("name"))

# print(customer.get("name"))
# print(customer["birthdate"])
# customer['name']='chetan'
# print(customer.get("name"))
# print(customer["date"])     # it will show key error


 #
 #practice question

phone=input("numbers:")

dictionary={

    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine",
    "0":"zero"
}
outstring=""
for ch in phone:
    outstring+=(dictionary.get(ch))+" "
print(outstring)

# dict={1:"shyam",2:"roha",3:"prashant"}