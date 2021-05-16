#Import everything from tkinter
from tkinter import *

#Creating a GUI box
root=Tk()

#Heading of the GUI
root.title("GUI")

#Creating an Entry Widget, Defaulting entry and Fetching values
ente=Entry(root,width=50,borderwidth=5)
ente.get()
ente.insert(0,"Enter your name")
ente.pack()

#Defining a function for button(s)
def myclick():
    hello="Hello "+ente.get()
    MyLabel0=Label(root,text=hello)
    MyLabel0.pack()

#Creating a Button Widget
MyButton=Button(root,text="Enter your Name",padx=50, pady=5,command=myclick,fg="Cyan",bg="Violet")

#Creating a Label Widget
MyLabel1=Label(root,text="Hello World")
MyLabel2=Label(root,text="My name is Rastra Dhoj Karki")

#Orienting the objects into the GUI
MyLabel1.pack()
MyLabel2.pack()
MyButton.pack()

#Running a constant loop to maintain GUI
root.mainloop()