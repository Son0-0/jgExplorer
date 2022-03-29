from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.user

def register(uname, uid, upw):
  result = db.users.insert_one({'uname': uname, 'uid': uid, 'upw': upw})
  
def isMember(uid):
  member_pw = list(db.users.find({'uid':uid}))
  if len(member_pw) > 0:
    return True
  else:
    return False
  
def extractName(uid):
  member_name = list(db.users.find({'uid':uid}))
  if len(member_name) > 0:
    return member_name[0]['uname']
  
def memberPW(uid):
  member_pw = list(db.users.find({'uid':uid}))
  if len(member_pw) > 0:
    return member_pw[0]['upw']

def isExist(uid):
  result = list(db.users.find({"uid":uid}))
  if len(result) > 0:
    return False
  else:
    return True
  
def insertArticle(uid, title, content, year, month, date, day):
  print(uid, title, content, year, month, date, day)
  db.diary.insert_one(
    {
      'uid': uid,
      'title': title,
      'content': content,
      'year': year,
      'month': month,
      'date': date,
      'day': day
    }
  )

def getArticle(uid):
  result = list(db.diary.find({"uid":uid}))
  return result