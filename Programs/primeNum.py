#A program that checks for prime numbers

def prime(num):
    flag=False
    for i in range(2,num):
        if(num%i==0):
            flag=True
            break
    if(flag):
        print(num,"is not a prime number")
    else:
        print(num,"is a prime number")
        
num=int(input("Enter a number:"))
prime(num)