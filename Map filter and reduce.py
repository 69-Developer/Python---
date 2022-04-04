num = []

for i in range(0,25):
    x = i
    num.append(x)

Square = list(map(lambda x : x * x , num))

print(Square)

# --------------------------FILTER-----------------------------

numlist = [1, 2, 3, 4]

def is_great_5(num):
    return num<5

is_greter_5 = list(filter(is_great_5,numlist))

print(is_greter_5)

# --------------------------REDUCE-----------------------------

lists = [1,2,3,4]
num = 0
for i in lists:
    num = num+i

print(num)