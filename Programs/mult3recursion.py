def multiply(n,i):
    product=n*i
    print(n,"X",i,"=",product)
    i=i+1
    if(i<=10):
        multiply(n,i)
i=1
n=int(input("Enter a number for the table of multiplication:"))
multiply(n,i)