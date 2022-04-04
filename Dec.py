import time

def to_upper(text):
    print(text.upper())

def to_lower(text):
    print(text.lower())

def timing(func):

    def knowx():
        print("To lower")
        func()
    return knowx

x = timing(to_upper("My name is sumit"))

