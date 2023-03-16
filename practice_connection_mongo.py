from pymongo import MongoClient
user = 'root'
password = 'MTMzNzgtbWFuYWdi' # insert you own password
host = 'localhost'


#create the connection url
connecturl = "mongodb://{}:{}@{}:27017/?authSource=admin".format(user,password,host)


# connect to mongodb server
print("Connecting to mongodb server")
connection = MongoClient(connecturl)


# select the 'training' database
print("connecting and using the training database") 
db = connection.training


# select the 'mongodb_glossary' collection 
print("using the mongodb_glossary collection") 
collection = db.mongodb_glossary


# creating the documents in a list to be stored
print("Generating the list of documents")
doclist = [{"database": "a database contains collections"}, 
           {"collection": "a collection stores the documents"},
           {"document": "a document contains the data in the form of key value pairs"}
           ]


# inserting the list of documents into collection
print("Inserting the list of documents")
for doc in doclist:
    db.collection.insert_one(doc)


# query to check the docs in mongodb_glossary collection inside the taining database
print("Printing the documents in the collection.")
docs = db.collection.find()
for documents in docs:
    print(documents)


# closing the connection to the database
print("Closing the connection to the database")
connection.close()

