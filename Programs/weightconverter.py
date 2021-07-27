#A program to convert weight from pounds to kg and vice versa

print("(1) Weight in kilograms.")
print("(2) Weight in pounds.")
choice=int(input("Enter your choice:"))
if(choice==1):
    kgs=int(input("Enter your weight in kilograms:"))
    pounds=kgs*2.205
    print("Your weight in pounds is",pounds)
elif(choice==2):
    pounds=int(input("Enter your weight in kilograms:"))
    kgs=pounds*2.205
    print("Your weight in kilograms is", kgs)
else:
    print("Invalid choice!")