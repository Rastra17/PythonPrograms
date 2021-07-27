#A program to input the time in minutes and display it in 24 hours format

N=int(input("Enter the number of minutes past since midnight:"))
if(N<=1440):
    midnight = 0000
    time = midnight + N
    hour = time // 60
    mins = time % 60
    print("The time is", hour, ":", mins)
else:
    print("Invalid format!")