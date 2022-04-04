s = set()

# s_from_list = set([1,2,3,4])
#
# print(s_from_list)
# print(type(s_from_list))

s.add(1)
s.add(10)
s2 = s.intersection({1,2,3})
print(len(s2))

# Remove elements
s2.remove(1)