#A program to simply check weather and print appropriate comment

temp=int(input("Enter the temperature:"))
if(temp>30):
    print("It's a hot day.")
elif(temp<10):
    print("It's a cold day.")
else:
    print("It's neither hot or cold day.")