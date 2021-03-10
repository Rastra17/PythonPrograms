#WAP to calculate the wait time of the bus. You live 4 miles from the university.
#The bus drives at 25mph but stops 2 minutes at each 10 stops on the way.
#How long will the bus journey take?
#Alternatively, you could run to the university and your speed is 7mph for the first mile.
#The next 2 miles at 15mph before jogging the last at 7mph.
#Will the bus be quicker or slower than you?
speed=25
intervals=2*10
distance=4
startstop=7
mid=15
timebybus=(distance/speed)+intervals
timebyus=distance/(startstop+mid+startstop)
if(timebybus>timebyus):
    print("The bus is quicker to reach the destination taking",timebybus,"minutes.")
else:
    print("The bus is slower to reach the destination",timebyus,"minutes.")