number1=0
number2=1
print(number1)
print(number2)
for data in range(1,20):
    # print(number1)
    # print(number2)
    number1,number2=number2,number1+number2
    print(number2)


