from pymongo import MongoClient
from Backconverting import convert_to_image

def connection():
    try:
        conn = MongoClient(host='localhost',port=27017)
        print("connected securely")
    except Exception as E:
        print("Connection failed")

    return conn

Conn = connection()
db = Conn["Images"]["Galaxy"]
raw_binary_data = db.find_one({'_id':'Galaxy 1'})

for key,value in raw_binary_data.items():
    if key=='image':
        x = value
        

convert_to_image(x)