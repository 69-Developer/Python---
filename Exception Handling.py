num1 = int(input("Enter the number\n"))


try:
    num2 = int(input("Enter the number 2\n"))
    print(num2+num1)
except Exception as E:
    print(E)

print("Very important code")