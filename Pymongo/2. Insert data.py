import pymongo

if __name__ == "__main__":
    def connect(host,port):
        Server = pymongo.MongoClient(host=host,port=port)
        return Server

    Connection = connect(host="localhost",port=27017)

    db = Connection["User"]
    collection = db["Id_pass"]

    # Add single data
    # Data = {'id':1,'name':"Aditya Badkar",'location':"Dundagae"}
    # collection.insert_one(Data)

    #Add many data

    Data = [
        {
            '_id':2,
            'name':"Ruturaj Chougule",
            'location':"Jahanum"
        },

        {
            '_id':3,
            'name':"Sahil Daddi",
            'location':"Gadhinglaj"
        },

        {
            '_id':4,
            'name':"Mayur Desai",
            'location':"Gadhinglaj"
        },

        {
            '_id':5,
            'name':"Sumit Ghotane",
            'location': "Hasurwadi"
        },
    ]

    collection.insert_many(Data)
