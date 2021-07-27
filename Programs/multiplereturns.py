#A program which returns mutiple values in a function

def ReturnInSV():
    return 20,1990,300,"Rastra"

def ReturnInMV():
    return 40,"Red",1200,1443

single=ReturnInSV()
m,u,l,t=ReturnInMV()

print(single)
print(m,u,l,t)