
class library:

    def __init__(self,list1,name):
        self.list1=list(list1)
        self.name=name
        self.issuebook={}

    def display(self):
        for i in self.list1:
            print(i)

    def newbook(self,newbook1):
        self.newbook1=newbook1
        self.list1.append(self.newbook1)
        print("book has been added")

    def issue(self,book,user):
        self.book=book
        self.user=user
        if book not in self.issuebook.keys():

            self.issuebook.update({self.book:self.user})
            print(self.issuebook)


        elif book in self.issuebook.keys():
            print(f"book is already issued by {self.issuebook[book]}")
        else:
            pass

    def returnbook(self,rbook):
        self.rbook=rbook
        self.issuebook.pop(rbook)
        print("book has been returned")

if __name__ == '__main__':
    obj1=library(["c++","java","python","asp.net","php"],"chetanlibrary")
    while(True):
        print(f"welcome to {obj1.name}, select your choice")
        print("1. display all")
        print("2. issue book")
        print("3.add new book")
        print("4. return book")
        print("5. exit")

        choice=int(input("select your choice:"))
        if choice not in [1,2,3,4,5]:
            print("enter valid choice:")
            continue
        elif choice==1:
            obj1.display()

        elif choice==2:
            book=input("enter book name:")
            user=input("enter user name:")
            obj1.issue(book,user)
            print("your book has been issued")

        elif choice==3:
            newbook1=input("enter book name you want to add:")
            obj1.newbook(newbook1)
        elif choice==4:
            rbook=input("enter book name you want to return:")
            obj1.returnbook(rbook)

        elif choice==5:
            exit()

