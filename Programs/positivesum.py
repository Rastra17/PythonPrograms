#A program to print the sum of first n positive integers

num=int(input("Enter the limit of loop:"))
sum=0
for i in range(0,num+1):
    if(i%2==0):
        sum=sum+i
print("The sum of first n positive integers is:",sum)