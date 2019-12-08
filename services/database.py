from pymongo import MongoClient

client = MongoClient("mongodb://db:27017")
db = client['message_database']
user_db = db['users']
