from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017")
db=client["office"]
coll1=db["workers"]
coll2=db["exworkers"]

id=input("Enter id to delete: ")
data=coll1.find_one({"_id":id})

if data:
    coll1.find_one_and_delete({"_id":id})
    b=coll2.insert_one(data)
    print(b)
    print("Data inserted into exworkers")
if not data:
    print("Worker not found")