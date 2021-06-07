class New:
    def __init__(self,inp,pro):
        self.inp=inp
        self.pro=pro
    def process(self):
        self.sum=self.inp+self.pro
    def out(self):
        print("The sum of two numbers:",self.sum)
num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))
r1=New(num1,num2)
r1.process()
r1.out()