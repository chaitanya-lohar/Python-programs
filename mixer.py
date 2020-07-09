from pygame import mixer
mixer.init()
list1=["16. Atif Aslam - Kabhi-To-Pas-Mere-aao (DJ Mix).mp3","song1.mp3","song2.mp3","song3.mp3"]
x=len(list1)
print(f"choose from between 1 to {x}")
song=int(input("enter your choice of music in numbers:"))

mixer.music.load(list1[song-1])
vol=int(input("set your volume:"))
mixer.music.set_volume(vol)
mixer.music.play()

while(1):
    print("press'p' to pause, press 'u' to resume, press 'e' for exit ,'r' for rewind" )
    choice1=input("enter your choice ")
    if choice1=='p':
        mixer.music.pause()

    elif choice1=='u':
        mixer.music.unpause()

    elif choice1=='r':
        mixer.music.rewind()

    elif choice1 == 'e':
        mixer.music.stop()
        break




