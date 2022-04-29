class Employees:

    emp = 69

    def __init__(self,name,phonenumber):
        self.name = name
        self.phonenumber = phonenumber

    def print_details(self):
        print(f"Name is {self.name} Phonenumber is {self.phonenumber}")

    @classmethod
    def change_employees(cls,new_no_of_employess):
        cls.emp = new_no_of_employess

    
Sumit = Employees("Sumit Ghotane",74856985632)
Raj = Employees("Raj Magdum",7458965236)

Sumit.no_of_employees = 64
Sumit.positon = "CEO"
Raj.no_of_employees = 63

# Employees before class method
print(Employees.emp)
print(Sumit.__dict__)

# Employees after class method
Sumit.change_employees(75)
print(Employees.emp)


# From class methods and instance get's an power to change the class variable without creating an instance variable and the class variable are only get by cls.variable_name?