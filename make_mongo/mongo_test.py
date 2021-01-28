from pymongo import MongoClient

uri = "mongodb://{}:{}@{}:{}/{}".format("root", "root", 'localhost', int(26016), "test_db")
instanceConnection = MongoClient(uri,connect=False)
dbs = instanceConnection.list_database_names()
 
print(dbs)