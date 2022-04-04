# a = 9
# b = 8
# c = sum((a,b)) #Builtin function
# print(c)

def func1(a,b):
    print("Hello you are in function 1")
    print(a+b)
# func1(5,7)

def average(a,b):
    """
    This is a function which caluculate
    average of two numbers
    """
    averages = (a+b)/2
    return averages

v = average(5,7)

import random

x = random.randint(10,16)

print(x.__doc__)