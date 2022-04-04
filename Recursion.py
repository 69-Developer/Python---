
import sys
sys.setrecursionlimit(10000)
print(sys.getrecursionlimit())
u = 0
def greet():
    global u
    u+=1
    print(u)
    print("Hello")
    greet()

greet()