# Python program to create a simple GUI calculator using Tkinter

# Import *(all) from tkinter library
from tkinter import *

# Var variable declared on global scope
Var = ""


# Function to update Var
def press(num):
    # To point global variable
    global Var

    # Joining the strings(Concatenation)
    Var = Var + str(num)

    # Update the Var by using set method
    equation.set(Var)


# Function to evaluate the final Var
def equalpress():
    # Try and except statement being used to handle division by zero and other errors.

    # Put that code inside the try block, which may generate the error
    try:

        global Var

        # Eval function to evaluate Var and str function to convert result into string
        total = str(eval(Var))

        equation.set(total)

        # Emptying the Var variable
        Var = ""

    # Errors handled by except, if any
    except:

        equation.set(" Error! ")
        Var = ""


# Function to make use of the clear button in calculator
def clear():
    global Var
    Var = ""
    equation.set("")


# Driver code
if __name__ == "__main__":
    # For GUI
    gui = Tk()

    # set the background colour of GUI window
    gui.configure(background="grey")

    # set the title of GUI window
    gui.title("Prototype Calculator")

    # Dimensions of the GUI
    gui.geometry("436x221")

    # StringVar() is the variable class
    # Creating an instance of this class
    equation = StringVar()

    # Create the text entry box showing the Var
    expression_field = Entry(gui, textvariable=equation)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    expression_field.grid(columnspan=160, ipadx=280)

    # create a Buttons and place at a particular
    # location inside the root window .
    # when user press the button, the command or
    # function affiliated to that button is executed .
    button1 = Button(gui, text=' 1 ', fg='black', bg='white',
                     command=lambda: press(1), height=2, width=14)
    button1.grid(row=2, column=0)

    button2 = Button(gui, text=' 2 ', fg='black', bg='white',
                     command=lambda: press(2), height=2, width=14)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' 3 ', fg='black', bg='white',
                     command=lambda: press(3), height=2, width=14)
    button3.grid(row=2, column=2)

    button4 = Button(gui, text=' 4 ', fg='black', bg='white',
                     command=lambda: press(4), height=2, width=14)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', fg='black', bg='white',
                     command=lambda: press(5), height=2, width=14)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', fg='black', bg='white',
                     command=lambda: press(6), height=2, width=14)
    button6.grid(row=3, column=2)

    button7 = Button(gui, text=' 7 ', fg='black', bg='white',
                     command=lambda: press(7), height=2, width=14)
    button7.grid(row=4, column=0)

    button8 = Button(gui, text=' 8 ', fg='black', bg='white',
                     command=lambda: press(8), height=2, width=14)
    button8.grid(row=4, column=1)

    button9 = Button(gui, text=' 9 ', fg='black', bg='white',
                     command=lambda: press(9), height=2, width=14)
    button9.grid(row=4, column=2)

    button0 = Button(gui, text=' 0 ', fg='black', bg='white',
                     command=lambda: press(0), height=2, width=14)
    button0.grid(row=5, column=0)

    plus = Button(gui, text=' + ', fg='black', bg='light blue',
                  command=lambda: press("+"), height=2, width=14)
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', fg='black', bg='light blue',
                   command=lambda: press("-"), height=2, width=14)
    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ', fg='black', bg='light blue',
                      command=lambda: press("*"), height=2, width=14)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', fg='black', bg='light blue',
                    command=lambda: press("/"), height=2, width=14)
    divide.grid(row=5, column=3)

    equal = Button(gui, text=' = ', fg='black', bg='light blue',
                   command=equalpress, height=2, width=14)
    equal.grid(row=5, column=2)

    clear = Button(gui, text='Clear', fg='black', bg='light blue',
                   command=clear, height=2, width=14)
    clear.grid(row=5, column='1')

    Decimal = Button(gui, text='.', fg='black', bg='light blue',
                     command=lambda: press('.'), height=2, width=14)
    Decimal.grid(row=6, column=0)
    # start the GUI
    gui.mainloop()