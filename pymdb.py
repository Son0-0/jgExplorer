from pymongo import MongoClient
from bson.objectid import ObjectId
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
  
def insertArticle(uid, title, content, level, year, month, date, day):
  db.diary.insert_one(
    {
      'uid': uid,
      'title': title,
      'content': content,
      'level': level,
      'year': year,
      'month': month,
      'date': date,
      'day': day
    }
  )

def getArticle(uid):
  result = list(db.diary.find({"uid":uid}))
  
  return_data = []
  
  for data in result:
    temp = {}
    temp['title'] = data['title']
    temp['content'] = data['content']
    date = str(data['year']) + "-" + str(data['month']) + "-" + str(data['date'])
    temp['date'] = date
    temp['_id'] = str(data['_id'])
    return_data.append(temp)
    
  return return_data

def getDate(uid):
  temp_date = []
  result = list(db.diary.find({"uid":uid}))
  
  udate = []

  for dates in result:
    temp = {}
    date = str(dates['year']) + "-" + str(dates['month']) + "-" + str(dates['date'])
    if date not in temp_date:
      temp_date.append(date)
      temp['date'] = date
      temp['level'] = dates['level']
      udate.append(temp)
  
  return udate

def getName(uid):
  result = list(db.users.find({'uid':uid}))
  return result[0]['uname']

def deleteArticle(_id):
  try:
    db.diary.delete_one({'_id': ObjectId(_id)})
    return True
  except:
    return False