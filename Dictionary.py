dl = {
    "Harry":"Burger",
    "Sumit":"Chicken",
    "Rohan":"Egg",
    "Skillf":"Hugi",
    "Sandesh":{
        "Breakfast":"Andda",
        "Launch":"Chicken",
        "Dinner":"Insaan"
    }
    }

# print(dl)
# print(dl["Harry"])
# print(dl["Sandesh"]["Dinner"])

# Adding Elements
dl["Ankit"] = "Junk Food"
dl[420] = "Kabab"
# print(dl)

# Removeing elements

del  dl[420]

# print(dl)

# Some function

df = dl.copy() #Creates the new dict and Copy the element
# del df["Harry"]
print(dl.get("Sumit"))

# Add an element
dl.update({"Alvaro Morte":"Tiki"})
# print(dl)
print(dl.keys()) #print all keys in the dict
print(dl.items()) #print all the items in the dict

# print(df)
# print(dl)