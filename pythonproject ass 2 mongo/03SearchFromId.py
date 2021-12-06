from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017")
db=client["office"]
coll=db["workers"]

id=input('Enter ID : ')

rec=coll.find_one({'_id':id})
print(rec)

