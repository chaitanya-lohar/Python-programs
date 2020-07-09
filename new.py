# a,b=eval(input("enter two values:"))
# if(a>b):
#     print(f" greatest number is:{a}")
# else:
#     print(f" b greatest:{b}")

# national=input("Enter your nationality:")
# age=int(input("enter your age:"))
# national=national.lower()
# if(national=="indian" and age>18):
#     print("you are eligible for pancard")
# else:
#     print("you are not eligible for pancard")


#1. calculate da, ta, hra, lic, pf and greater and lesser salary

# basic=int(input("enter your basic salary:"))
#
# if(basic<1000):
#     da=float(basic*10.5/100)
#     ta=float(basic*10.5/100)
#     hra=float(basic*11.5/100)
#     pf=float(basic*13.5/100)
#     lic=float(basic*10.5/100)
#
#     net=(da+ta+hra)-(pf+lic)
#     print(f"Net salary of employee under 10000$ is:{net}$")
# elif(basic>1000):
#     da = float(basic * 15.5 / 100)
#     ta = float(basic * 14.5 / 100)
#     hra = float(basic * 17.5 / 100)
#     pf = float(basic * 19.5 / 100)
#     lic = float(basic * 13.5 / 100)
#
#     net = (da + ta + hra) - (pf + lic)
#     print(f"Net salary of employee above 10000$ is:{net}$")
#

#2.enter three number and find greatest among three

# first,second,third=eval(input("Enter three number:"))
#
# if( first > second):
#     if(first>third):
#         print("first is greatest")
#     else:
#         print("third is greatest")
# else:
#
#     if(second>third):
#         print("second is greatest")
#     else:
#         print("third is greatest")


#3,. pan card question

# nationality=input("enter your nationality :")
# age=int(input("Enter your age:"))
# nationality=nationality.lower()
# if(nationality=="indian"):
#     if(age>18):
#         print("YOU ARE ELIGIBLE FOR PAN CARD")
#     else:
#         print("YOU ARE UNDER AGE")
# else:
#     print("YOU ARE NOT INDIAN ")
#
#4 marksheet
# m1,m2,m3,m4,m5=eval(input("Enter your five subject marks:"))
# total=(m1)+(m2)+(m3)+(m4)+(m5)
# per=total/5
# print("total marks out of 500 is:",total)
# print("total percentage is:",per,"%")
#
# if(per<36):
#     print("you are failed")
# elif(per>90):
#     print("A Grade")
# elif(per>70 and per<90):
#     print("B Grade")
# elif(per>55 and per<70):
#     print("C Grade")
# elif(per>36 and per<55):
#     print("D Grade")


#5: find enter number is positive or negative or zero
# number=int(input("Enter any number:"))
# if(number>0):
#     print("number is positive")
# elif(number<0):
#     print("number is negative")
# else:
#     print("NUMBER IS ZERO")
#

# 6. Enter char is vovel or not ?
# char=input("Enter any Character:")
# char=char.lower()
# if(char=="a"):
#     print(f"VOWEL:{char}")
# elif(char=="e"):
#     print(f"VOWEL{char}")
# elif(char=="i"):
#     print(f"VOWEL:{char}")
# elif(char=="o"):
#     print(f"VOWEL:{char}")
# elif(char=="u"):
#     print(f"VOWEL:{char}")
# elif(char != int):
#     print("Please enter character not NUMBER")
# else:
#     print(f"Entered character is consonant:{char}")