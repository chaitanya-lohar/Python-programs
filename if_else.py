#contact=input("Please enter 10 digit number:")

#lenght=len(contact)
#lenght==10
#if lenght==10:
 #   print("You entered correct digits!")
#else:
  #  print("Please enter only 10 digit number :")

# has_high_income=True
# has_good_credit=False
# # so this is AND and OR operator example
# # NOT operator is also here (it change the condition )
#
# if has_high_income and not has_good_credit:
#     print("you are eligible for loan")
# else:
#     print("you are not eligible for loan")

from pygame import mixer

mixer.init()
mixer.music.load("16. Atif Aslam - Kabhi-To-Pas-Mere-aao (DJ Mix).mp3")
mixer.music.set_volume(15)
mixer.music.play()

while(1):
    print("Enter 'p' to pause , 'u' to resume, 'e' to end")
    choice = input("enter your choice:")
    if choice == 'p':
        mixer.music.pause()
    elif choice == 'u':
        mixer.music.unpause()

    elif choice == 'e':
        mixer.music.stop()

        break

