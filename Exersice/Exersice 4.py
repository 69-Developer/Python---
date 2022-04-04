number = int(input("Enter the no of star rows\n"))
bo = int(input("Type 1 or 0\n"))
val = bool

if bo == 1:
    val = True
else:
    val = False

if val == True:
    for i in range(0,number+1):
        print(i*"*")
else:
    for i in range(-int(number),0):
        j = abs(i)
        print(j*"*")

