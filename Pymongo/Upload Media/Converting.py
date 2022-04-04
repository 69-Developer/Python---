def convert_to_binary():
    file = open("./Galaxy.jpg","rb")
    x = file.read()
    file.close()
    return x

if __name__ == '__main__':    
    x = convert_to_binary()
    print(x)