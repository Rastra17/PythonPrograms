#A program to check conditions and give desired output

price=1000000
credit=True
if(credit==True):
    discount=10/100
    dp=price*discount
    price=price-dp
    print("The final price is:",price)
else:
    discount=20/100
    dp=price*discount
    price=price-dp
    print("The final price is:",price)