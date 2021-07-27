#A program to print alphabets in a pattern

for i in range(65,70):
    Var=i
    for j in range(65,i+1):
        print(chr(Var), end=' ')
        Var= Var + 1
    print()