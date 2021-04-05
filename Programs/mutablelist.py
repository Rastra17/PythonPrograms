lst=[]
limit=int(input("Enter the limit to input values for a list:"))
i=1
while(i<=limit):
    values=int(input("Enter the value(s) to input in list sequence:"))
    lst.append(values)
    i=i+1
def choice():
    choice=int(input("Press (1) to check values of the list.\nPress (2) to change the values within the list.\nPress (3) to exit the program.\n"))
    if(choice==1):
        check()
    elif(choice==2):
        mutate()
    elif(choice==3):
        exit()
    else:
        print("Invalid choice!")
        recursion()
def check():
    print("The values in list are:",lst)
    choice()
def mutate():
    print(lst)
    for i in range(0,limit):
        print("The location of",lst[i],"is",i)
    replace = int(input("Enter the location of the value to replace:"))
    lst[replace] = int(input("Enter the value for replacement:"))
    print(lst)
    choice()
def recursion():
    choice()
choice()