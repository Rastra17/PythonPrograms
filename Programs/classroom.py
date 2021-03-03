#WAP to calculate the distribution of desks in the least amount in 3 classrooms where 2 students can occupy a desk.
def clsA(A):
    least=(A//2)
    print("The least number of desks for classroom A is:",least)
    return least
def clsB(B):
    least=(B//2)
    print("The least number of desks for classroom B is:",least)
    return least
def clsC(C):
    least=(C//2)
    print("The least number of desks for classroom C is:",least)
    return least
a=int(input("Enter the number of students in classroom A:"))
b=int(input("Enter the number of students in classroom B:"))
c=int(input("Enter the number of students in classroom C:"))
sumleast=clsA(a)+clsB(b)+clsC(c)
print("The total least amount of benches needed is:",sumleast)