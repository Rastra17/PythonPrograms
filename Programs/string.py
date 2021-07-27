#A program which uses different kinds of string manipulation

name = input("Enter your name:")
age = int(input("Enter age:"))

print("Hello my name is " + name + " and I am " + str(age) + " years old")

print("Hello my name is", name, "and I am", age, "years old")

print("Hello my name is %s and I am %d years old" % (name, age))

print("Hello my name is {} and I am {} years old".format(name, age))