lim=int(input("Enter a limit:"))
if(lim<=1000):
    for i in range(lim):
        a = i // 100
        b = (i // 10) - (a * 10)
        c = (i % 100) - (b * 10)
        armstrong = (a ** 3) + (b ** 3) + (c ** 3)
        if (i == armstrong):
            print(i)
else:
    print("Limit needs to be less than or equal to 1000!")