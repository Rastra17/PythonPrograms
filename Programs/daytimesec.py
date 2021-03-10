sec=int(input("Enter the time in seconds:"))
day=sec//86400
hour=(sec-day*86400)//3600
mins=(sec-day*86400-hour*3600)//60
sec=sec-day*86400-hour*3600-mins*60
print("It is",day,"day(s),",hour,"hour(s),",mins,"minute(s),",sec,"second(s).")