#A program to connect MySQL database with python

import mysql.connector

#Connecting python to MySQL Server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

#Creating a cursor
my_cursor=mydb.cursor()

#Creating a database with global tuple
db=("Management",)
try:
    my_cursor.execute("CREATE DATABASE IF NOT EXISTS Management;")
except Exception as e:
    print("Something went wrong!",e)
else:
    print(mydb)

#Connecting to MySQL Server with Database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database=db[0]
)

#Creating a cursor again to strengthen it
my_cursor=mydb.cursor()

#Trying to create table if it does not exists.
try:
    my_cursor.execute("CREATE TABLE IF NOT EXISTS users(name VARCHAR(255),"
                      "email VARCHAR(255),"
                      "password VARCHAR(255),"
                      "balance INTEGER(10),"
                      "user_id INTEGER AUTO_INCREMENT Primary KEY);")
except Exception as e:
    print("Something went wrong!",e)
else:
    my_cursor.execute("SHOW TABLES;")
    result=my_cursor.fetchall()
    for row in result:
        print(row)

#CLosing the database after work.
mydb.close()