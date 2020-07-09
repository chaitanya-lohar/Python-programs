
# i=5
# # while i>=0:
# #     print("*"*i)
# #     i=i-1
# # print("done")

# guess game

# guess_number=5
# guess_count=0
# guess_limit=3
#
# while guess_count < guess_limit:
#     guess=int(input("enter guess number:"))
#     guess_count+=1
#     if guess==guess_number:
#         print("you won!")
#         break
#     #else:
#       #  print("try again!")
# #print("you have lost!")
# else:
   # print("oh you have failed!")

# car game logic
command=""
started=False
while True:
     choice=input("Enter choice:").lower()
     if choice=="start":
         if started:
             print("car already started")
         else:
             print("ready to start")

     elif choice=="stop":
         print("car has stopped")

     elif(choice=="quite"):
         print("program terminated")
         break
     else:
         print("sorry , i can't understand")




