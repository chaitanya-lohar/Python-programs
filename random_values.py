import random

# for i in range(0,3):
#     print(random.random())      # first random is module and second one is function and it will create random value 3 time


#------------------------------------------------------------------------------
# if we want to generate random value between particular range

# for i in range(3):
#     print(random.randint(10,20))
#-------------------------------------------------------------------------------
# we want to select any random member
member=["jorj","janiffer","smith","carol"]
print(member)
# leader=random.choice(member)                   # choice is randomly picking item from list
# print(leader)

#-------------------------------------------------------------------------------
# class Dice:
#     def roll(self):
#         num=random.randint(1,6)
#         num1=random.randint(1,6)
#         return num,num1
#
#         # print(f"({num},{num1})")

# obj1=Dice()
# print(obj1.roll())