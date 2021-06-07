#Lamda function for basic math operation
x=int(input("Enter 1st number:"))
y=int(input("Enter 2nd number:"))
sum=lambda x,y:x+y
print(sum(x,y))

#Lambda function for sorting a list
lst=[[1,3],[4,9],[19,1]]
lst.sort(key=lambda lst:lst[1])
print(lst)