import pymongo

server = pymongo.MongoClient(host='localhost',port=27017)

db = server["CoinDCX"]

collection = db["User_by_phonenumber"]

deleteids = [{"name":"Zebb"},{"phonenumber":7458963265}]

for items in deleteids:
    collection.delete_one(items)
print("Deleted")