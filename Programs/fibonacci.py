#A program to print fibonacci series of n numbers

def fibo(sum,mem,i):
    i=i+1
    print(sum)
    if (sum == 0):
        sum = sum + 1
        if(i<=10):
            fibo(sum,mem,i)
    else:
        sum = sum + mem
        mem = sum - mem
        if(i<=10):
            fibo(sum,mem,i)
i=1
sum=0
mem=0
fibo(sum,mem,i)