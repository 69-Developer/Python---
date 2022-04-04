lis = ["Optimus Prime","Bumblebee","Bulkhead","Arcee","Ratchet","Wheeljack","Smokescreen","Ultra magnus"]

def function_name_autobot(autobot):
    print(autobot)

# function_name_autobot("Optimus prime")

def funcargs(normal,*auto):
    # print(type(args))
    for item in auto:
        print(normal,item)

# funcargs(True,*lis)

# normal argument should be before args and kwargs
# args and kwargs are optional

kw = {
    "Optimus Prime":"Autobot Leader",
    "Ratchet":"Autobot doctor",
    "Ultra magnus":"Autobot commander",
    "Jazz":"First Liuetinent of Autobots",
    "Bumblebee":"Soilder",
    "Wheeljack":"Wracker",
    "Alpha Trion":"Prime"
}

def auto_work(**kwargs):
    for name,work in kwargs.items():
        print(f"Name {name} work is {work}")

auto_work(**kw)

# normal , args , kwargs