class Library:

    def __init__(self,id,phonenumber):
        self.id = id
        self.phonenumber = phonenumber

    def print_details(self):
        print(f"Id is {self.id} phonenumber is {self.phonenumber}")
        

Sumit = Library(7548,7821044265)
# Rohan = Library()

# Sumit.id = 4589
# Sumit.phonenumber = 7821044262

# Rohan.id = 7859
# Rohan.phonenumber = 7589652369

# print(Rohan.print_details())

"""
Insted of declearing variable of the object we can use constructor
Constructor :- Helps to get the argument
"""

Sumit.print_details()