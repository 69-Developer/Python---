class India():
    def __init__(self,name,standerd):
        self.name = name
        self.standerd = standerd

    def print_details(self):
        print("Name is {0} class is {1}".format(self.name,self.standerd))

Country = India("Sumit","X")
Country.print_details()