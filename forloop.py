#1 example:
# for item in 'python':
#     print(item)
#----------------------------------------------------------------------------------------------------------------------

#2 example:
# for item in [10,20,30,40,50,60]:
#     print(item)
#-----------------------------------------------------------------------------------------------------------------------
#3 example:
# for item in range(0,100,5):
#     print(item)

#----------------------------------------------------------------------------------------------------------------------
#4. shopping example

# prices=[100,200,300,400]
# total=0
# for item in prices:
#     total+=item
#
# print(f"total is:{total}")

#----------------------------------------------------------------------------------------------------------------------
# nested for loop

# for x in range(4):
#     for y in range(3):
#         print(f"({x}),({y})")


#----------------------------------------------------------------------------------------------------------------------

#question to make F like shape using nested for loop


# for item in number:
#     item=item*'x'
#     print(item)
number=[5,2,5,2,2]
for item in number:
    output=''
    for count in range(item):
        output=output+'x'

    print(output)