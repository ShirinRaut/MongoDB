from pymongo import MongoClient


client=MongoClient("mongodb://localhost:27017")
db=client["office"]
coll=db["workers"]

lis=coll.find()
for rec in lis:
     print(rec)





    
    
