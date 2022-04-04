# num1 = int(input("Enter the number 1\n"))
# num2 = int(input("Enter the number 2\n"))
# operators = str(input("Enter the operator\n"))
#
# if operators is "+":
#     if num1 == 56 and num2 == 9 or num2==56 and num1==9:
#         print(77)
#     else:
#         print(num2+num1)
#
# elif operators is "-":
#     print(num1-num2)
#     print("Note: Num2 is subtracted from Num1 ")
#
# elif operators is "*":
#     if num1 == 45 and num2 == 3 or num2==45 and num1==3:
#         print(555)
#     else:
#         print(num1*num2)
#
# elif operators is "/":
#     if num1 == 56 and num2 == 6:
#         print(4)
#     else:
#         print(num1/num2)
#         print("Note: Num2 is divide from Num1")
#
# else:
#     print("Do not do cheating MF")

print("enter your 1st number")
num1=int(input())

print("enter your 2nd number")
num2=int(input())

print("enter your mathematical action i.e; add,substract,multiply,divide")
opt= (input())

if opt== '+' and num1==56 and num2==9:
    print(" 77")
else:
    print( num1 + num2 )


if opt== '-' :
    print( num1 - num2 )


if opt== '*' and num1==45 and num2==555:
      print("555")
else:
    print( num1 * num2 )


if opt== '/' and num1==56 and num2==6:
    print(" 4")
else:
    print( num1 / num2 )
