from tkinter import *
import mysql.connector
from tkinter import messagebox
from tkinter import ttk

#Global variables to assist the program
counter=0
iteration=0
flag=False

#Main GUI for the System
manage=Tk()
manage.title("Bank Management System")

#Connecting python to TestDataBase database of 'root' user
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rastra9860009091",
    database="Management"
)

#Creating a cursor
my_cursor=mydb.cursor()

#Creating a database
'''
my_cursor.execute("CREATE DATABASE Management;")
'''

#Creating Table and its columns
'''
my_cursor.execute("CREATE TABLE users(name VARCHAR(255),"
                  "email VARCHAR(255),"
                  "password VARCHAR(255),"
                  "user_id INTEGER AUTO_INCREMENT Primary KEY);")
'''

#Labels for Register Entries
username=Label(manage,text="Username",font=18)
username.grid(row=0,column=0)
email=Label(manage,text="Email:",font=18)
email.grid(row=1,column=0)
password=Label(manage,text="Password:",font=18)
password.grid(row=2,column=0)

#Entries for Registration
Entry_username=Entry(manage,width=25,borderwidth=5)
Entry_username.grid(row=0,column=1)
Entry_email=Entry(manage,width=25,borderwidth=5)
Entry_email.grid(row=1,column=1)
Entry_password=Entry(manage,width=25,borderwidth=5)
Entry_password.grid(row=2,column=1)

def show_records():
    global iteration
    showrec = Tk()
    showrec.title("Records Database")

    # Creating a tree view for database
    my_tree = ttk.Treeview(showrec)
    my_tree['columns'] = ("Names", "Emails", "Passwords", "User IDs")

    # Formatting the columns
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("Names", width=100, minwidth=25)
    my_tree.column("Emails", width=150, minwidth=25)
    my_tree.column("Passwords", width=120, minwidth=25, anchor=CENTER)
    my_tree.column("User IDs", width=60, minwidth=25, anchor=CENTER)

    # Headings of Tree columns
    my_tree.heading("#0", text="")
    my_tree.heading("Names", text="Names")
    my_tree.heading("Emails", text="Emails")
    my_tree.heading("Passwords", text="Passwords")
    my_tree.heading("User IDs", text="User IDs")

    # Adding data into the tree
    my_cursor.execute("SELECT name,email,password,user_id FROM Management.users;")
    result = my_cursor.fetchall()
    for row in result:
        my_tree.insert(parent='', index='end', iid=iteration, text="",
                       values=(row[counter], row[counter + 1], "********", iteration+1))
        iteration = iteration + 1
    my_tree.grid(row=1, column=0)
    showrec.mainloop()


#Inserting data into the table
def registration():
    global flag
    global counter
    insert = "INSERT INTO users(name,email,password) VALUES (%s,%s,%s);"
    record = (Entry_username.get(), Entry_email.get(), Entry_password.get(),)
    my_cursor.execute("SELECT name, email, password FROM Management.users;")
    result = my_cursor.fetchall()
    if (Entry_username.get() != "" or Entry_email.get() != "" or Entry_password.get() != ""):
        for row in result:
            flag = False
            if(Entry_email.get()==row[counter+1]):
                messagebox.showinfo("Failed!", "Entry already exists!")
                break
            else:
                flag=True
        if(flag):
            my_cursor.execute(insert, record)
            mydb.commit()
            Entry_username.delete(0, 'end')
            Entry_email.delete(0, 'end')
            Entry_password.delete(0, 'end')
            Entry_username.focus_set()
            messagebox.showinfo("Successful", "Registration Completed!")
    else:
            messagebox.showinfo("Failed!", "Empty Fields")
    counter=0
    flag=False

#Logging in the user
def login():
    global counter
    global flag
    my_cursor.execute("SELECT name, email, password FROM Management.users;")
    result = my_cursor.fetchall()
    if (Entry_username.get() != "" or Entry_email.get() != "" or Entry_password.get() != ""):
        for row in result:
            flag=False
            if (Entry_username.get() == row[counter] and Entry_email.get() == row[
                counter + 1] and Entry_password.get() == row[counter + 2]):
                flag=True
                break
        if(flag):
            Entry_username.delete(0, 'end')
            Entry_email.delete(0, 'end')
            Entry_password.delete(0, 'end')
            Entry_username.focus_set()
            messagebox.showinfo("Logged in!", "You have logged in successfully!")
        else:
            messagebox.showinfo("Failed!", "Record does not exist!")

    else:
        messagebox.showinfo("Failed!", "Empty Fields")
    counter=0
    flag=False

#Deleting records from database
def delete():
    global counter
    global flag
    my_cursor.execute("SELECT name, email, password FROM Management.users;")
    result = my_cursor.fetchall()
    if (Entry_username.get() != "" or Entry_email.get() != "" or Entry_password.get() != ""):
        for row in result:
            flag=False
            if (Entry_username.get() == row[counter] and Entry_email.get() == row[
                counter + 1] and Entry_password.get() == row[counter + 2]):
                flag=True
                break
        if(flag):
            delet = "DELETE FROM Management.users WHERE Management.users.email = (%s);"
            frm = (Entry_email.get(),)
            my_cursor.execute(delet,frm)
            mydb.commit()
            Entry_username.delete(0, 'end')
            Entry_email.delete(0, 'end')
            Entry_password.delete(0, 'end')
            Entry_username.focus_set()
            messagebox.showinfo("Successful!", "Deleted record!")
        else:
            messagebox.showinfo("Failed!","Record does not exist!")
    else:
        messagebox.showinfo("Warning!","Empty Fields!")
    counter=0
    flag=False

#Button(s) for GUI
regis=Button(manage,text="Register",command=registration)
regis.grid(row=3,column=0)
log=Button(manage,text="Login",command=login)
log.grid(row=4,column=0)
rec=Button(manage,text="Show Records",command=show_records)
rec.grid(row=3,column=1)
dele=Button(manage,text="Delete",command=delete)
dele.grid(row=4,column=1)

#Putting main GUI in a loop
manage.mainloop()

#Close connection of database and cursor
my_cursor.close()
mydb.close()