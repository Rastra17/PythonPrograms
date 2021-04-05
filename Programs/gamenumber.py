a=5
i=0
while(i<3):
    match=int(input("Guess a number:"))
    if(match==a):
        print("The number you have guessed is correct.")
        break
    else:
        print("The number you have guessed is incorrect.")
        if(i==2):
            print("You have used all your tries.")
    i=i+1