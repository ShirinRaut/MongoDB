from pymongo import MongoClient
from pymongo.common import _CaseInsensitiveDictionary

client=MongoClient("mongodb://localhost:27017")
db=client["office"]
coll=db["workers"]

id=input('Enter  ID : ')
empnm=input('Enter employee name : ')
dept=input('Enter department : ')
pst=input('Enter post of employee : ')
ct=input('Enter city: ')
slr=float(input('Enter salary: '))
mbl=int(input('Enter mobile number: '))


dic={}
dic["_id"]=id
dic["empmnm"]=empnm
dic["dept"]=dept
dic["pst"]=pst
dic["ct"]=ct
dic["slr"]=slr
dic["mbl"]=mbl

coll.insert_one(dic)
print('New employee details added to office collection')
