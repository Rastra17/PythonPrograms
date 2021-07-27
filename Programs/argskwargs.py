#A program to implement *args and **kwargs parameters

# A normal no return, yes argument function
def function_name_print(a,b,c,d):
    print(a,b,c,d)
print("This is a normal function:")
function_name_print("Harry","Alex","Bell","Red\n")

# Declaring *args function which takes multiple input within a function.
def funargs(strin,*args):
    lim=len(args)
    print(strin)
    for i in range(lim):
        print(args[i])
strin="This is an *args function:"
lst=["Harry","Alex","Bell","Red","Rona\n"]
funargs(strin,*lst)

# Declaring **kwargs function which takes in keys of a dictionary within a function.
def funkwargs(strin,*args,**kwargs):
    lim=len(args)
    print(strin)
    for i in range(lim):
        print(args[i])
    for key,value in kwargs.items():
        print(f"{key} is a {value}")
strin="This is a **kwargs function:"
args=["Harry","Alex","Bell","Red","Rona\n"]
kwargs={"Alex":"Monitor","Alexandra":"Student Council President","Alexsaur":"College Captain"}
funkwargs(strin,*args,**kwargs)