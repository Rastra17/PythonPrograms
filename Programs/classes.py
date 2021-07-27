#A program to practice GUI witihin a class

from tkinter import *
root=Tk()
root.title('Classes')
root.geometry("400x400")

class App:
    def __init__(self,master):
        myFrame=Frame(master)
        myFrame.pack()

        self.myButton=Button(master,text="Click Me!",command=self.clicker)
        self.myButton.pack(pady=20)

    def clicker(self):
        print("Clicked a button!")
e=App(root)

root.mainloop()