def Value(Func):
    def Returning_func():
        print("Darth Vader is")
        Func()
        print("Anakin Skywalker")
    return Returning_func

@Value
def Enter_name():
    inp = input("Enter you name\n")

Enter_name()