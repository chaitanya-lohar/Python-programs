class Demo:
    def prime(self):

        n=int(input("enter any number:"))
        for i in range(1,n+1):
            if(n%i==0):
                print("NO is prime")
                break
        else:
            print("NO is not prime")

obj1=Demo()
obj1.prime()


