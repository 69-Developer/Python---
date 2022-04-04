def Whoiskira(func):
    
    def Nowexe():
        print("Bringing information But Pass authentication")
        func()
        print("Check info Carefully")
    
    return Nowexe

@Whoiskira

def IDPASS():
    inp = int(input("Enter the special number"))
    if inp == 789:
        print('Light yagami is Kira')
    else:
        print("Authentication")

IDPASS()