import mysql.connector

#Connecting python to TestDataBase database of 'root' user
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rastra9860009091",
    database="TestDataBase"
)

#Creating a cursor
my_cursor=mydb.cursor()

#Creating a database
'''
my_cursor.execute("CREATE DATABASE TestDataBase;")
'''

#Executing command to show Databases
'''
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db[0])
'''

#Creating Table and its columns
'''
my_cursor.execute("CREATE TABLE users(name VARCHAR(255),"
                  "email VARCHAR(255),"
                  "age INTEGER(10),"
                  "user_id INTEGER AUTO_INCREMENT Primary KEY);")
'''

#Executing command to show table
'''
my_cursor.execute("SHOW TABLES")
for table in my_cursor:
    print(table[0])
'''

#Inserting data into the table
'''
insert="INSERT INTO users(name,email,age) VALUES (%s,%s,%s);"
names=input("Enter your name:")
emails=input("Enter your email:")
age=int(input("Enter your age:"))
record=(names,emails,age)
my_cursor.execute(insert,record)
'''

#Showing the contents of a table
my_cursor.execute("SELECT name,email,age FROM TestDataBase.users;")
result = my_cursor.fetchall()
for row in result:
    print(row)
    print("\n")

#Saving data into the database
'''
mydb.commit()
'''