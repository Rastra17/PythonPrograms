#A progrm which sorts the elements in a list

lst=[]
limit=int(input("Enter the limit of list:"))
for i in range(limit):
    values=int(input("Enter values:"))
    lst.append(values)
length=len(lst)
for i in range(length):
    for j in range(i):
        if (lst[j] > lst[i]):
            temp = lst[j]
            lst[j] = lst[i]
            lst[i] = temp
print("List has been sorted to ascending order:",lst)
def choice():
    choice=int(input("What do you want to do with the list?\nPress (1) for Location Search\nPress (2) for Number Search"
                    "\nPress Any Key to Exit\nChoose any one:"))
    if (choice == 1):
        location_search()
    elif (choice == 2):
        number_search()
    else:
        exit()
def location_search():
    number = int(input("Enter the number to return it's location:"))
    if (number in lst):
        high = length
        low = 0
        mid = (high + low) // 2
        if (number == lst[mid]):
            if(length%2==0):
                print("The location of the number is:",mid)
            else:
                print("The location of the number is:",mid+1)
        elif(number>=lst[mid]):
            for i in range(mid+1,high):
                if(number==lst[i]):
                    print("The location of the number is:",i)
        else:
            for i in range(low,mid):
                if(number==lst[i]):
                    print("The location of the number is:",i)
    else:
        print("Error:Number Not Found in List!")
    choice()
def number_search():
    location = int(input("Enter the location to return it's number:"))
    if (location<=length):
        high = length
        low = 0
        mid = (high + low) // 2
        if(location==mid):
            if (length % 2 == 0):
                print("The number at the location is:", lst[mid])
            else:
                print("The number at the location is:", lst[mid + 1])
        elif(location>=mid):
            for i in range(mid+1,high):
                if(location==i):
                    print("The number at the location is:",lst[i])
        else:
            for i in range(low,mid):
                if(location==i):
                    print("The number at the location is:",lst[i])
    else:
        print("Error:List Index OutOfBounds!")
    choice()
choice()