from pymongo import MongoClient
from Converting import convert_to_binary
def connection():
    try:
        conn = MongoClient(host='localhost',port=27017)
        print("connected securely")
    except Exception as E:
        print("Connection failed")

    return conn

Conn = connection()
db = Conn["Images"]
collection = db.create_collection("Galaxy")
data = {
    '_id':'Galaxy 1',
    'image':convert_to_binary()
}
collection.insert_one(data)
print("Image uploaded")
Conn.close()