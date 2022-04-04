grocery = ["Harpic","Vim bar","Deodrant","Lollypop"]
numbers = [5,8,6,9,8,5,7,5,8,52,1,6186,1,61,61,61,618,161616,1616,161,16,168,6,1]
# print(grocery)

# Simple Functions
# numbers.sort() #Sort the number in ascending order
# print(numbers)
# numbers.reverse() #Reverse the number from end to start
# print(numbers)

# List slicing
number = [1,2,3,4,5,6,7,8,9]

# Positive slicing
# print(number[:]) #Prints the exact list

# print(number[1:5]) #Prints the list between 1 to 4 because 5 is not including
"""
[:4] - Blankplace before : is take the value as 0
[0:] - Blankplace after : takes as len of the list
"""

print(number[::2]) #prints the number list with skipping 1 number from left hand side

# Negative Slicing

print(number[-1:-5:-2])

# Some functions
number.append(7) #Add number at the end
number.insert(0,85) #Add number at the given index
number.remove(85) #Removes the given number
number.pop()

print(number)