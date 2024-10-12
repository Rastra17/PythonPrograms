#A program to practice class which calculates the sum of 2 numbers

class New:
    def __init__(self,inp,pro):
        self.inp=inp
        self.pro=pro
    def process(self):
        self.sum=self.inp+self.pro
    def out(self):
        print("The sum of two numbers:",self.sum)
    def main(self):
        self.process()
        self.out()
inp=int(input("Enter 1st number: "))
pro=int(input("Enter 2nd number: "))
display=New(inp,pro)
display.main()