# File Handling
# is use to save the text on hard disk parmanent.
# Modes
# 'r' = read
# 'w' = write
# 'a' = append
# 'x' = create file if not exists
# 't' = text mode
# 'b' = binary
# 'r+' = read + write
# -------------------------------------------------------------
# Read:
# f=open('demo.txt','r')
# print(f.read())
# f.close()
# f=open('demo.txt','w')
# f.write("this is my second page")
# -------------------------------------------------------------
# f=open("demo.txt",'r')
# print(f.read()) # read whole lines
# print(f.readline(10)) # read upto 10 char
# print(f.readlines())  # it create list of presented lines in file
# print(f.readline())  # read only one line
#----------------------------------------------------------------
# f=open('demo.txt','w')
# f.write("this is python project")
# f.close()
# f=open('demo.txt','r')
# print(f.read())
#-----------------------------------------------------------------
# display only small letter character
# f=open('demo.txt','w')
# f.write("THIS IS PYHON project , do you want to SAVE IT!")
# f.close()
# f=open('demo.txt','r')
# x=f.read()
# for i in range(len(x)):
#     if x[i]>'A' and x[i]<'Z':
#         print(x[i])

#------------------------------------------------------------------
# f=open('demo.txt','r+')
# print(f.read())
# f.write("that is amazing no to need to explain")
# print(f.read())
# print(f.tell()) # cout no of char
# print(f.seek(12)) # cursor move to 12th location
# print(f.readline())
#=--------------------------------------------------------------------------
# copy content from one file to another

# f1=open('demo.txt','r')
# data=f1.read()
# f2=open('demo1.txt','w')
# f2.write(data)
# f2.close()
# f2=open('demo1.txt','r')
# print(f2.read())

#---------------------------------------------------------------------------
# copy content from one file to another but in reverse order
# f1=open('demo.txt','r')
# data=f1.read()
# f2=open('demo1.txt','w')
# data=data[::-1]
# f2.write(data)
# f2.close()
# f2=open('demo1.txt','r')
# print(f2.read())

#----------------------------------------------------------------------------
#copy img from one to another location
f1=open('abc.JPG','rb')
data=f1.read()
f2=open('abc1.JPG','wb')
f2.write(data)
f2.close()
f2=open('abc1.JPG','rb')
print(f2.read())
