class parent1:
    var1="class variable of parent1"  # class variable

    def show(self):
        self.var1="instance variable of parent1"  # instance method
        # print("show of parent",self.var1)
        return self.var1

class parent2(parent1):
    var1="class variable of parent2"
    def show(self):
        self.var1="instance variable of parent2"
        print("show of parent2",super().show())

d1=parent2()
d1.show()
