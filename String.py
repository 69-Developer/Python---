mystr = "sumit is a Good Boy"
"""
print(mystr)
"""

# Get length
"""
print(len(mystr))
"""

# String Slicing
"""
print(mystr[0:5])
"""

"""
print(mystr[78]) # IndexError: string index out of range - 
When the len of the string is more than the given index number of the element
"""

"""
print(mystr[0:78])
"""

"""
This is not error because len of the string is 19 and given element index is 
78 so now the elements after the 19 is blank spaces
"""

# Few slicing techniques
"""
mystr[:5] - now before the : python takes the value as 0

mystr[0:] - now after the : python takes the len of the that string variable

mystr[:] - here it will print the full string because here before : takes as 0 and after : takes as len of the string
"""

# ------------------------------------------------------------------------------------------------
"""
print(mystr[:10])
print(mystr[0:])
print(mystr[:])
"""
# ------------------------------------------------------------------------------------------------

# Elements skipping in the string

"""
print(mystr[::2])
"""

"""
print(mystr[0:len(mystr):] - The blank value after : takes as the 1
"""

# Negative slicing

"""
print(mystr[-4:-2])
"""

"""
When you use - sign the python use started slicing it from end to start and -1 is the first index
"""

"""
print(mystr[::-1])
"""

"""
This reverse the string and started printing it from end to 1

number greater than -1 for skiping started skipping the string from end to start
"""

# String Functions

print(mystr.endswith("Boy")) # Check the given word is also ending with that word in the string
print(mystr.count("s")) # gives the no of times the element repeat
print(mystr.capitalize()) #Captilize the first letter
print(mystr.find("is")) #get the given word starting index and if the word does exist it give -1
print(mystr.lower()) #Converts a string into lower case
print(mystr.upper()) #Converts a string into upper case
print(mystr.replace("is","are")) #Replaces the word in the string by the given word

