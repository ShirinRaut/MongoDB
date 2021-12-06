from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017")
db=client["office"]
coll=db["workers"]


sal=input("Enter salary of worker: ")
a=coll.find({"salary":{"$gt":sal}})

for doc in a:
    print(doc)
