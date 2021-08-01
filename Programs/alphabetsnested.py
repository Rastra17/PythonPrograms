#A program to print alphabets in a pattern

Var=65
for i in range(65,70):
    for j in range(65,i+1):
        print(chr(Var), end=' ')
        Var= Var + 1
    print()