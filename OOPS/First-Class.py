class Adharinfo():

    def __init__(self,name,phonenumber,DOB):
        self.name = name
        self.phonenumber = phonenumber
        self.dob = DOB

    def Return_info(self):
        print(f"Name is {self.name} Phonenumber is {self.phonenumber} Date of Birth {self.dob}")

Sumit = Adharinfo("Sumit Narasing Ghotane",7821044262,'23-6-2007')
Norman = Adharinfo("Norman Sceem",7856985634,'25-45-3000')

Sumit.Return_info()
Norman.Return_info()