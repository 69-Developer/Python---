l = 10 #Global

def function1(n):
    global l
    l = 105+100 #Local
    # global m = 9 #Local
    print(l)
    print(n,"I have printed")

# function1("This is me")
# print(l)

def harry():
    x = 20
    def rohan():
        global x
        x = 88

    print("Before calling rohan",x)
    rohan()
    print("After calling Rohan",x)

# harry()
# print(x)

p = 56

def haeey():
    p = 97

    def rohans():
        global p
        p = 84
        print(p ,"Inside rohan")
    rohans()

haeey()
print(p)