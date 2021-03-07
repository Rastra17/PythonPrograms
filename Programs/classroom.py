#WAP to calculate the distribution of desks in the least amount in 3 classrooms where 2 students can occupy a desk.
def clsA(A):
    if(A%2==0):
        least = (A // 2)
        print("The least number of desks for classroom A is:", least)
        return least
    else:
        least = (A // 2)+1
        print("The least number of desks for classroom A is:", least)
        return least
def clsB(B):
    if(B%2==0):
        least = (B // 2)
        print("The least number of desks for classroom B is:", least)
        return least

    else:
        least = (B // 2)+1
        print("The least number of desks for classroom B is:", least)
        return least
def clsC(C):
    if(C%2==0):
        least = (C // 2)
        print("The least number of desks for classroom C is:", least)
        return least
    else:
        least = (C // 2)+1
        print("The least number of desks for classroom C is:", least)
        return least
a=int(input("Enter the number of students in classroom A:"))
b=int(input("Enter the number of students in classroom B:"))
c=int(input("Enter the number of students in classroom C:"))
sumleast=clsA(a)+clsB(b)+clsC(c)
print("The total least amount of benches needed is:",sumleast)