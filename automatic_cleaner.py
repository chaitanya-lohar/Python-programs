import os
files=os.listdir()
print(files)
# os.makedirs("Images")
# os.makedirs("Doc")
# os.makedirs("Others")
# os.makedirs("Media")
def create(*folder):
    for data in folder:
        if not os.path.exists(data):
            os.makedirs(data)
            print(data,"folder created")    # joined photography
        else:
            print(data,"Folder Already exits")

create("Image","Medias","Others","Doc")

imagelist1=[".png",".jpg",".jpeg"]
images=[file for file in files if os.path.splitext(file)[1].lower() in imagelist1]
print("images moved ")
doclist1=[".doc",".docs",".xlsx",".txt"]
docs=[file for file in files if os.path.splitext(file)[1].lower() in doclist1]
print("document moved ")
songlist1=['.mp3']
songs=[file for file in files if os.path.splitext(file)[1].lower() in songlist1]
print("song moved")

def move(foldername,files):
    for file in files:
        os.replace(file,f"{foldername}/{file}")

move("Medias",songs)
move("Image",images)
move("Doc",docs)