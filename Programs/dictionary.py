#A program to practice dictionary in python with its key-value pairs

a={"Name1":"Harry","Roll No.1":120,"Address1":"London"}
b={"Name2":"ALice","Roll No.2":150,"Address2":"New York"}
c={"Name3":"Giorno","Roll No.3":180,"Address3":"Paris"}
put=input("Enter the key:")
if(put in a):
    print(a[put])
elif(put in b):
    print(b[put])
elif(put in c):
    print(c[put])
else:
    print("Invalid Input!")