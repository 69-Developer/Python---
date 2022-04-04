import datetime

Intro = """
----------------------------------------------------------------------------------
Steps for proceed further
1. Diet - for show the Diet
2. Exersice or Ex - for show the Exersice
3. Entry - for entry the food details
----------------------------------------------------------------------------------
"""

print(Intro)

# Functions

# Initial Date and time
def get_date():
    return datetime.date.today()

def Rohan(Action):
    if str(Action).capitalize() == "Diet":
        file = open("Rohan\\Diet.txt","r")
        print(file.read())

    elif str(Action).capitalize() == "Exersice" or "Ex":
        file = open("Rohan\\Exersice.txt","r")
        print(file)

    elif str(Action).capitalize() == "Entry":
        Date = f"[{get_date()}]"
        file = open("Rohan\\Time.txt","r+")
        while True:
            inp = input("Enter the food or E for exit\n")
            if inp != "E":
                file.write(f"{Date} {inp} \n")
            else:
                exit()

def Harry(Action):
    if str(Action).capitalize() == "Diet":
        file = open("Harry\\Diet.txt","r")
        print(file.read())

    elif str(Action).capitalize() == "Exersice" or "Ex":
        file = open("Harry\\Exersice.txt","r")
        print(file)

    elif str(Action).capitalize() == "Entry":
        Date = f"[{get_date()}]"
        file = open("Harry\\Time.txt","r+")
        while True:
            inp = input("Enter the food or E for exit\n")
            if inp != "E":
                file.write(f"{Date} {inp} \n")
            else:
                exit()


def Hammad(Action):
    if str(Action).capitalize() == "Diet":
        file = open("Hammad\Diet.txt","r")
        print(file.read())

    elif str(Action).capitalize() == "Exersice" or "Ex":
        file = open("Hammad\Exersice.txt","r")
        print(file)

    elif str(Action).capitalize() == "Entry":
        Date = f"[{get_date()}]"
        file = open("Hammad\Time.txt","a")
        while True:
            inp = input("Enter the food or E for exit\n")
            if inp != "E":
                file.write(f"\n{Date} {inp}")
            else:
                exit()

def Inputs():
    Actionss = input("Enter the Name\n")
    Actions = input("Enter the work\n")
    if Actionss.capitalize() == "Rohan":
        Rohan(Actions)
    elif Actionss.capitalize() == "Harry":
        Harry(Actions)
    elif Actionss.capitalize() == "Hammad":
        Hammad(Actions)

if __name__ == '__main__':
    Inputs()
