number = 21

i = 0

while i<6:
    inp = int(input("Enter the number\n"))
    i = i + 1
    if inp<21:
        print("Smaller than This")
        print("Chances left {}".format(6-i))
        continue
    elif inp>21:
        print("Greater than this")
        print("Chances left {}".format(6-i))
        continue
    else:
        print("Correct Answer")
        break