# Example of type conversion:
birth_year=input('enter your birth year: ') #  whenever we use input function than we will get only string value and if we want to perform any numeric calculation than we have to convert
                                           # this into int or float according to our requirement
print(type(birth_year))                     # type function is used to determine type of given variable
age=2021-int(birth_year)
print(type(age))
print('your age is: '+str(age)) # we can't concatenate two different types that's why here we convertated age into string .
