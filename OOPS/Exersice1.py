class Electronicdevice:

    n = 7
    items = ["Refrigerator","Washing machine","Television"]

class Pocketdevice(Electronicdevice):

    no_of_item = 3
    items = ["Earbuds","Earphone","Cards"]

class Phone(Pocketdevice):

    items = ["Samsung","Apple","Xiaome"]

ED = Electronicdevice()
PD = Pocketdevice()
Phone = Phone()

print(Phone.items)