import time
import random
class remote_controller:

    channel_list=[]
    def __init__(self, tv_status="off", tv_volume=0,channel_name="BBCI",watching_channel=None,no_channels=0):
        time.sleep(1)
        print("creating remote controller.....")
        self.tv_status=tv_status
        self.tv_volume=tv_volume
        self.channel_name=channel_name
        self.watching_channel=watching_channel
        self.no_channels=no_channels

    def Tv_On(self):
        if(self.tv_status=="ON"):
            print("tv is alread ON....")
        else:
            print("TV is turnning ON......")
            self.tv_status="ON"
    def Tv_Off(self):
        if(self.tv_status=="off"):
            print("tv is already off......")

        else:
            print("tv is turnning off......")
            self.tv_status="off"

    def volume_adjustment(self):

        while(True):
            ans=input("Volume down:'-'\n Volume Up :'+'\n Exit:'exit'")
            if(ans=='-'):
                if(self.tv_volume!=0):
                    self.tv_volume-=1
                    print(f"TV Volume is:{self.tv_volume}")

            elif(ans=='+'):
                if(self.tv_volume!=50):
                    self.tv_volume+=1
                    print(f"TV Volume is:{self.tv_volume}")
            else:
                print("TV volume is updated....")
                break

    def Add_channel(self,channels_name):

        time.sleep(2)
        self.channel_list.append(channels_name)

    def random_channel(self):
        rand=random.randint(0,len(self.channel_list)-1)
        self.watching_channel=self.channel_list[rand]
        print(f"You are watching  {self.watching_channel} channel ")

    def lenths(self):
        print(type(self.channel_list))
        self.no_channels=len(self.channel_list)
        print(self.no_channels)
        return self.no_channels
    def __str__(self):
        return(f"TV Status:{self.tv_status}\n TV Volume:{self.tv_volume}\n Channel List:{self.channel_list}\n Watching Channel:{self.watching_channel}")

remote_controller1=remote_controller()

print('''

1.Turn On TV
2. Turn Off TV
3.Volume Adjustment
4.Add Channel
5.Number of Channels
6. Open Random Channel
7. Tv Info
''')


while(True):
    operation=int(input("choose the operation you want to perform:"))
    if(operation==1):
        remote_controller1.Tv_On()

    elif(operation==2):
        remote_controller1.Tv_Off()
    elif(operation==3):
        remote_controller1.volume_adjustment()
    elif(operation==4):
        channel_name=input("Enter channel name with using comas......")
        channel1_name=channel_name.split(",")
        for data in channel1_name:
            remote_controller1.Add_channel(data)
        print("Adding new channel.......")
        print("Channel added........")
    elif(operation==5):
        print("Number of Channels:",remote_controller1.lenths())
    elif(operation==6):
        remote_controller1.random_channel()
    elif(operation==7):
        print(remote_controller1)
    else:
        print("Select appropriate operation!")
        time.sleep(1)


