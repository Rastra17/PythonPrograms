#A program to print sum of elements in a list using recursion

def add(lst,sum,i):
    length=len(lst)
    sum = sum + lst[i]
    i=i+1
    if(i<length):
        add(lst,sum,i)
    else:
        print(sum)
lst=[]
put=int(input("Enter the limit of list:"))
for i in range(1,put+1):
    value=int(input("Enter the value(s):"))
    lst.append(value)
sum=0
i=0
add(lst,sum,i)