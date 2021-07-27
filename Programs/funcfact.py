#A program to print factorial of a number

def factorial(put):
    product=1
    for i in range(1,put+1):
        product=product*i
    print("The factorial of the number entered is:",product)

put=int(input("Enter a number:"))
factorial(put)