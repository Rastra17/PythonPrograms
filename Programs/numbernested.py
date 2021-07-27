#A program to print numbers in a pattern

Var=1
for i in range(1,5):
    for j in range(1,i+1):
        print(Var, end=' ')
        Var= Var + 1
    print()