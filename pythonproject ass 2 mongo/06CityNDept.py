from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017")
db=client["office"]
coll=db["workers"]

id=input("Enter id to update it's salary: ")
data=coll.find_one({"_id":id})
if data:
    ct=input("Enter new city: ")
    dept=input("Enter new department: ")

    coll.find_one_and_update({"_id":id},{"$set":{"city":ct,"dept":dept}})

    print("updated successfully")
    print(coll.find_one({"_id":id}))

if not data:
   print("worker not found")