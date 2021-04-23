def sumoflist(lst):
    sum=0
    for i in lst:
        sum=sum+i
    print("The sum of list is:",sum)
lst=[]
put=int(input("Enter the limit of list:"))
for i in range(1,put+1):
    value=int(input("Enter the value(s):"))
    lst.append(value)
sumoflist(lst)