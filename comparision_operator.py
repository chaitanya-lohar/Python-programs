#temp = int(input("Enter current temperature:"))

#if temp > 30:
  #  print("its a hot day")
#elif temp < 10:
 #   print("its a cold day")
#else:
  #  print("its moderate day!")

    # > this is greater than operator
    # < this is less than operator
    # >= greater then and equal
    # <= less then and equal
    # == equality operator ( = this is assignment operator)

name= input("enter your name please! ")
name_lenght =len(name)

if name_lenght < 3:
    print(" your name must be more than three character ")
elif name_lenght > 30:
    print("its more then 30 character so name must be maximum 30 character")
else:
    print("name looks good!")