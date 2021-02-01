from pymongo import MongoClient

uri = "mongodb://{}:{}@{}:{}/{}".format("testUser", "testPassword", 'localhost', int(26016), "test_db")
print(uri)
instanceConnection = MongoClient(uri,connect=False)
dbs = instanceConnection.list_database_names()
db = instanceConnection.get_database("test_db")
print(dbs)
#// 콜렉션 정보를 가져온다
str_collection_name = 'test_table'
db.drop_collection(str_collection_name) #// 작업 전 콜렉션 초기화
collection = db.get_collection(str_collection_name)
collection.insert_one({'name': 'Trump', 'age': 70}) #// 도큐먼트를 추가한다
collection.insert_one({'name': 'Obama', 'age': 60}) #// 도큐먼트를 추가한다

#// Who is over 60 years old? (60세 이상 조회)
results = collection.find({"age": {"$gte": 60}})
for result in results:
    print(result)
#// {'_id': ObjectId('5ec7166de54cb8384dc8893f'), 'name': 'Trump', 'age': 70}
#// {'_id': ObjectId('5ec7166de54cb8384dc88940'), 'name': 'Obama', 'age': 60}
