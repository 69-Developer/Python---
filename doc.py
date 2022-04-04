# def decor_result(func):
#     def returning(marks):
#         for mark in marks:
#             if mark >=75:
#                 print("DISTINCTION")
#         func(marks)
#     return returning

# @decor_result
# def passorwhat(markslist):
#     for itme in markslist:
#         if itme >=35:
#             pass
#         else:
#             print("FAIL")
#             break
#     else:
#         print("PASS")

# marks = [75,80,78,84,87] 

# passorwhat(marks)

from requests import get as g

url = "https://my-json-server.typicode.com/typicode/demo/posts"

req = g(url)

import json

x = json.loads(req.text)

for item in x:
    for itemns in item.items()["id"]:
        print(itemns)