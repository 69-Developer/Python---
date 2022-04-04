# For loops in list

list = ["Harry","Rohan","Skillf","Sumit","Aurangzeb"]

for item in list:
    # print(item)
    pass

"""
Itrate each item with the list and print the each element within the list
"""

# For loop for multiple list

list2 = [["Harry",3,2],["Sumit",1,2],["Skillf",2,4],["Aurangzeb",1000,100000]]

for item,computers,keyboards in list2:
    # print(item," have",computers," computers"," and " ,keyboards , " Keyboards")
    pass

"""
Here when their is data type inside a data type it will return a list which we can further iterate 
by a key word in the for loop statement because this uses that keyword as its to print list 1 index
it changes according to no of item in return list
"""

#for loop in dict
dict = {
    "Harry":3,
    "John":1,
    "Aurangzeb":1000000,
    "Johhny":1
}

for item,mouse in dict.items():
    # print(item+" Have this much mouse",mouse)
    pass

for item in dict:
    # print(item)
    pass
"""
For loop of dictionary returns a tuple using the keyword statement in for loop syntax we can iterate its element
Without doing .items() method if we use for loop we will get all the keys
"""

# Quiz

list = ["Kiran","Atharv",1,53,8,5,3,6,4,8]

for item in list:
    if str(item).isnumeric() and item>=6:
        print(item)
