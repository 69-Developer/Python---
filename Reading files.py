f = open("Lang.txt","rt")
# content = f.read()
# print(content)
#
# for line in f:
#     print(line)
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())

x= f.readlines()
for imte in x:
    print(imte)
f.close()