

class Demo:
    def getdata(self):
        a,b=int(input("enter first value:")),int(input("enter second value:"))
        self.a=a
        self.b=b

    def putdata(self):
        print("value of a {},value of b {}".format(self.a,self.b))

    def __add__(self, other):      #tinder method is available to overload -,*,/
        x=self.a+d2.a
        y=self.b+d2.b
        return x,y


d1=Demo()
d2=Demo()
d1.getdata()
d2.getdata()
d1.putdata()
d2.putdata()

d3=d1+d2
print((d3))