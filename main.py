from flask import Flask, render_template, redirect, url_for, jsonify, flash, session
from datetime import timedelta
from flask import request
import pymongo
import pymdb
import bcrypt

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
  if 'uid' in session:
    uid = session['uid']
    uname = pymdb.getName(uid)
    return render_template('mypage.html', uid=uid, uname=uname)
  else:
    return redirect(url_for("login"))
  
@app.route('/login', methods=["GET", "POST"])
def login():
  if request.method == "POST":
    data = request.form
    uid = data.get('uid')
    upw = data.get('upw')
    
    if uid != 'None' and upw != 'None':
      plain_text = upw.encode('UTF-8')

    if pymdb.isMember(uid) == True:
      dbdata = pymdb.memberPW(uid)
      origin_pw = bytes.fromhex(dbdata) # DB에 저장되어 있는 값
      if bcrypt.checkpw(plain_text, origin_pw) == True: # 로그인 성공 case
        session['uid'] = uid
        return redirect(url_for("home")) # alert
      else:
        flash("아이디 및 비밀번호를 다시 확인하세요!", category='error')
        return render_template('login.html')
    else:
      flash("아이디 및 비밀번호를 다시 확인하세요!", category='error')
      return render_template('login.html')
  else:
    return render_template('login.html')

@app.route('/logout')
def logout():
  session.pop('uid', None)
  return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
  return render_template('register.html')

@app.route('/memberRegister', methods=['POST'])
def registerMember():
  data = request.get_json()
  uid = data['uid']
  upw = data['upw']
  uname = data['uname']
    
  if pymdb.isExist(uid) == True:
    plain_text = upw.encode('UTF-8')
    pw_hash = bcrypt.hashpw(plain_text, bcrypt.gensalt()).hex() # DB에 저장될 값
    pymdb.register(uname, uid, pw_hash)
    print("Register Success: ", uname, uid)
    return jsonify(result="success", result2="등록이 완료되었습니다!")
  else:
    print("Register Fail")
    return jsonify(result="fail", result2="등록에 실패하였습니다. 관리자에게 문의하세요")

@app.route('/isExist', methods=['POST'])
def isExist():
  data = request.get_json()
  if pymdb.isExist(data['uid']) == False:
    return jsonify(result = "fail", result2 = "이미 등록된 아이디 입니다.")
  else:
    return jsonify(result = "success", result2 = "사용 가능한 아이디 입니다.")
  
@app.route('/getArticle/<uid>', methods=['GET'])
def getArticle(uid):
  result = pymdb.getArticle(uid)
  date = pymdb.getDate(uid)
  return jsonify(result="success", result2=result, date=date)

@app.route('/submitArticle', methods=['POST'])
def submitArticle():
  data = request.get_json()
  uid = data['uid']
  title = data['title']
  content = data['content']
  level = data['level']
  year = data['year']
  month = data['month']
  date = data['date']
  day = data['day']
  pymdb.insertArticle(uid, title, content, level, year, month, date, day)
  return jsonify(result="success")

@app.route('/deleteArticle/<id>', methods=['GET'])
def deleteArticle(id):
  result = pymdb.deleteArticle(id)
  if result == True:
    return jsonify(result="success")
  else:
    return jsonify(result="fail")
    
if __name__ == '__main__':
  app.secret_key = 'THISISSECRETKEYFORJUNGLE'
  app.config['SESSION_TYPE'] = 'filesystem'
  app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=30)
  app.run('0.0.0.0', port=5555, debug=True)