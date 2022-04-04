# lambda function
#
# def ad(a,b):
#     return a+b
#
# minus = lambda x,y: x-y
#
# print(abs(minus(4,5)))

a = [
    [9,4],[7,8],[15,12],[1,16]
]

minus = lambda a:a[1]

a.sort(key=minus)
print(a)