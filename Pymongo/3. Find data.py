import pymongo

if __name__ == "__main__":
    def connect(host,port):
        print("Connecting...............")
        Server = pymongo.MongoClient(host=host,port=port)
        print("Connected to server")
        return Server

    Connection = connect(host="localhost",port=27017)

    db = Connection["User"]
    collection = db["Id_pass"]

    # Find
    possiblity = collection.find({'name':"Sumit Ghotane"}).limit(1)

    for item in possiblity:
        print(item)

    