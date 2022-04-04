file = open("Lang.txt")

print(file.tell())
print(file.readline())
print(file.tell())
print(file.readline())
print(file.tell())
print(file.readline())
file.seek(8)
print(file.readline())

file.close()