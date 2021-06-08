class App:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def execute(self):
        self.sum=self.num1+self.num2
        print(self.sum)

#__name__=='__main__' will make sure that the code below will work only when this file will run.
if __name__=='__main__':
    num1 = int(input("Enter 1st number:"))
    num2 = int(input("Enter 2nd number:"))
    run = App(num1, num2)
    run.execute()