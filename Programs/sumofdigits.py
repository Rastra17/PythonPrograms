#A program which calculates the sum of its digits

put=int(input("Enter a 3 digit number:"))
if(put>99 and put<999):
    d3 = put % 100
    d2 = put % 10
    d1 = put // 100
    sum = d3 + d2 + d1
    print(sum)
else:
    print("Wrong input!")