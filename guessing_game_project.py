import random
import time

print('''

this is guesing game.......
you will get 5 attemp...
let's start....

'''
)
time.sleep(2)
attemp=5
counter=0
random_number=random.randint(1,11)

time.sleep(1)
while(True):
    guess_number = int(input("enter any guessing number:"))
    if(guess_number>random_number):
        print("you guessing number is higher than our number, please select lower number.................")
        time.sleep(2)
        attemp-=1
        counter+=1

    elif(guess_number<random_number):
        print("you guessing number is lower than our number, pelase select higher number............")
        time.sleep(2)
        attemp-=1
        counter+=1
    else:
        print("hurry! you won the game, your guessing number is right....")
        print(f"random number was:{random_number}")
        print("you guessed in",counter,"attemp(s)")
        time.sleep(1)
        break


