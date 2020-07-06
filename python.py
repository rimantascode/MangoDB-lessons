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


"""coll.update_one({'nationality':'american'}, {'$set':{'hair_color':'ginger'} })"""

coll.insert({'first':'John', 'last':'lennon', 'dob':'09/08/1985', 'gender':'m', 'hair_color':'brown', 'nationality': 'English', 'occupation':'Beatle'})

"""coll.remove({'first':'John'})"""


documents = coll.find({"first":"John"})
i=0
for doc in documents:
    i=i+1
    print(doc)
print("This is how many is inthe document{}".format(i))
