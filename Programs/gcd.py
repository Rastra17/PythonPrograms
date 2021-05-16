num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
fac1=[]
fac2=[]
cd=[]
for i in range(1,num1+1):
    if(num1%i==0):
        val1=i
        fac1.append(val1)
print("The factors of first number is:",fac1)
for i in range(1,num2+1):
    if(num2%i==0):
        val2=i
        fac2.append(val2)
print("The factors of second number is:",fac2)
for i in fac1:
    for j in fac2:
        if(i==j):
            val3=i
            cd.append(val3)
print("The common divisors of the two numbers are:",cd)
length=len(cd)
gcd=cd[length-1]
print("The greatest common divisor of two numbers is:",gcd)