class Employees:

    def __init__(self,name,phonenumber):
        self.name = name
        self.phonenumber = phonenumber

    def printself(self):
        return self.__dic

    def salary(self,job):
        self.job = job

        if self.job == "Programmer":
            return "70000"

    @staticmethod
    def talk(name,message,to):
        return f"{name} - {message} - {to}"

Sumit = Employees("Sumit ghotane",7821044262)
# print(Sumit.talk("Sumit Ghotane","Are you free tonight let us go for a coffee","Akansha murti"))
print(Sumit.printself())

"""
As the self have all the instructor arguments and hence it have an memory and when you want a function which have no any use of the self class to get the instance variables you can have the static method where the self with the data is not passed and in this class we create a function which show the arguments have with self and therefore use of static method is important to provide efficiency to the Users
"""