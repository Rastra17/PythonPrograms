#A program to implement inheritance in python

class Coder:
    def __init__(self,ethical,networking,computing):
        self.ethical=ethical
        self.networking=networking
        self.computing=computing

class Person(Coder):
    def test(self):
        pass

class Program(Person):
    def behaviour(self):
        pr = self.ethical + self.networking + self.computing
        print(pr)

person1=Program("1","2","3")
person1.behaviour()