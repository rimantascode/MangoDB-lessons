import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "myFirstMDB"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        
conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]


new_docs= [{'first':'rob', 'last':'kirt', 'dob':'11/08/20','hair_colour':'blue', 'occupation':'singer', 'nationality':'American'},{'first':'dream', 'last':'dreamer', 'dob':'10/09/1957','hair_colour':'red', 'occupation':'dreamer', 'nationality':'legoland'}]

coll.insert_many(new_docs)


documents = coll.find({'first':'duaglas'})

for doc in documents:
    print(doc)