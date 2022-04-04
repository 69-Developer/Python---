# # Python program to illustrate functions
# # can be passed as arguments to other functions
# def shout(text):
# 	return text.upper()

# def whisper(text):
# 	return text.lower()

# def greet(func):
# 	# storing the function in a variable
# 	greeting = func("""Hi, I am created by a function passed as an argument.""")
# 	print (greeting)

# greet(shout)
# greet(whisper)

# Returning the function


# def Operations(first_num):
#     def add(num):
#         return first_num+num

#     return add
# OK = Operations(25)
# print(OK(5))


# def Try_connection(responsecode):
#     if responsecode >= 200:
#         print("Server connecting \n")
#     else:
#         print("Server error. not connecting")

# def Info(fun):
    
#     def response_code():
#         code = False
#         if code is True:
#             fun(200)
#             print("Connection successfull")
#         else:
#             fun(404)
#             print("Server error. not connecting")
#     return response_code

# xxx = Info(Try_connection)
# xxx()

#import time
#import math

#list = [x for x in range(100000)]

#def timing(fun):

 #   def timeeee():
  #      start = time.localtime().tm_sec
#
 #       fun(list)

  #      end = time.localtime().tm_sec

   #     print("Time taken by "+fun.__name__+" is "+str(end-start)+"sec")

    #return timeeee

#@timing
#ef square(number_list):
  #  for item in number_list:
   #     print(f"{item*item}")

#square()

# import time

# number_lists = [1,2,3,4,5,6,7,8,9] 

# def timing(func):

#     def calculate(num_list):
#         start = time.localtime().tm_sec
#         func(num_list)
#         end = time.localtime().tm_sec
#         print("Time taken by program is "+str(end-start)+" sec")

#     return calculate

# def square(list):
#     for item in list:
#         print(item*item)

# print(timing(square(number_lists)))

from requests import get

response = get("https://my-json-server.typicode.com/typicode/demo/posts")

def give_response():
    x = response.json()
    for item in x:
        print(item)

def check_all(fun):
    def check_status():
        if response.status_code == 200:
            fun()
        else:
            print("Stop and read Theory of everything\n")
    
    return check_status

print(check_all(give_response))