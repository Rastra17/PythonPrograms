f=open('writeread.txt','r+')
r=f.read()
strg='\nThank you for joining!'
if(strg not in r):
    w=f.write(strg)
print(type(r))
print(r)
f.close()