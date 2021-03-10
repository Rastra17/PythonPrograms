name=input("Enter your name:")
length=len(name)
if(length<=3):
    print("The name is too short.")
elif(length>50):
    print("The name is too long.")
else:
    print("The name is good.")