from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017")
db=client["office"]
coll=db["workers"]

dept=input("Department name: ")

all=coll.find({"dept":dept})
for worker in all:
    print(worker)