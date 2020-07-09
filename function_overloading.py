class demo:
    def func1(self,a=None,b=None,c=None):
        if(a!=None and b!=None and c!=None):
            self.a=a
            self.b=b
            self.c=c
            print(self.a+self.b+self.c)
        elif(a!=None and b!=None):
            self.a=a
            self.b=b

            print(self.a+self.b)
        else:
            self.a=a
            print(self.a)
obj1=demo()
obj1.func1(10)
obj1.func1(10,20)
obj1.func1(10,20,30)
