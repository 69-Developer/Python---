class Dad:
    basketball = 1

class Son(Dad):
    dance = 1

    def isdance(self):
        return f"Yes i dance {self.dance}"

class GrandSon(Son,):
    
    basketball = 7
    dance = 6
    
Da = Dad()
So = Son()
GS = GrandSon()

print(GS.basketball)
