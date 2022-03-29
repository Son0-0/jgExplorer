from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.user

def register(uid, upw):
  db.users.insert_one({'uid': uid, 'upw': upw})
  all_users = list(db.users.find({}))
  print(all_users)
  