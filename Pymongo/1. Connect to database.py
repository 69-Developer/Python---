import pymongo

def connect(host,port):
    Server = pymongo.MongoClient(host=host,port=port)
    return Server

connect(host="localhost",port=27017)