# f = open("Lang.txt","w")
# f.write("C#")
# f.close()

# f = open("Lang.txt","a")
# A = f.write("\nPython\nC\nC++")
# print(A)
# f.close()

# Read and write both

f = open("Lang.txt","r+")
print(f.read())
f.write("\nSQL")
f.close()