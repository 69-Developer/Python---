class Sum_of_two:
    
    no_of_ope = 4

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def sumsS(self):
        return self.num1+self.num2

class Calculator(Sum_of_two):

    no_of_ope = 69

    def __init__(self,num1,num2,isdecimal):
        self.isdecimal = isdecimal
        self.num1 = num1
        self.num2 = num2
    
    def whattodo(self,ope):
        if ope == '+':
            return self.num1+self.num2
            

S = Calculator (5,10,True)
print(S.whattodo('+'))
print(S.no_of_ope)