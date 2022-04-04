import time as t

k = 0

initial = t.time()
print(initial)
while (k<45):
    k = k + 1
    print("This is a sumit bhai")

print(t.time() - initial)
initial_2 = t.time()
for i in range(45):
    print("This is harry bhai")

print(t.time() - initial_2)