# WAP to find sum of elements of list using while loop.
lst=[10,31,37,40,56,63,70]
length=len(lst)
i=0
sum=0
while i<length:
    sum=sum+lst[i]
    i=i+1
print(length,"is the length of this list.")
print(sum,"is the sum.")