from pymongo import MongoClient

#client = MongoClient('178.128.38.170:27017')
client = MongoClient('localhost:27017')

#db.createUser(
#    {
#        user: "niklas2",
#        pwd: "abc123",
#        roles: []
#    }
#)

#def my_function(mydb):
#    db = client.get_database(mydb)
#    return db.mycol.find()


#print(my_function('mycol'))

mydb = client["mynewcol"]
mycoll = mydb["test"]
mydict = {"name": "Niklas", "lastname": "nielsen"}

x = mycoll.insert_one(mydict)

#cursor = mycoll.find({"lastname": "bla"})

#myquery = {"lastname": "Nielsen"}

#mycoll.delete_many(myquery)

#mycoll.delete_one(cursor)

#for document in cursor:
#    print(document.get("lastname"))

#for document in cursor:
#    print(document.get("lastname"))

#x = mycoll.delete_many(myquery)

#print(x.deleted_count)