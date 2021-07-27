#A program to generate codes when a string is provided and to decode that same string

def choice():
    choice=int(input("Press (1) to Code your input\nPress (2) to Decode your input\nPress Any Key to Exit\nEnter your choice:"))
    if(choice==1):
        coder()
    elif(choice==2):
        decoder()
    else:
        exit()
def coder():
    inputstring = input("Enter a string to crypt:")
    crypt = ""
    for i in inputstring:
        temp=ord(i)
        incr=temp+1
        temp=chr(incr)
        crypt= crypt + temp
    print(crypt)
    choice()
def decoder():
    inputstring = input("Enter a string to decrypt:")
    decrypt = ""
    for i in inputstring:
        temp=ord(i)
        decr=temp-1
        temp=chr(decr)
        decrypt=decrypt+temp
    print(decrypt)
    choice()
choice()