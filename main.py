from flask import Flask, render_template, redirect, url_for, jsonify, flash, session
from datetime import timedelta
from flask_jwt_extended import *
from flask import request
import pymongo
import pymdb
import bcrypt

app = Flask(__name__)


# jwt 환경변수 등록
app.config.update(
  DEBUG = True,
  JWT_SECRET_KEY = "THISISSECRETKEYFORJUNGLEJWT"
)

jwt = JWTManager(app)

@app.route('/logout')
def logout():
  session.pop('uid', None)
  return redirect(url_for('home'))


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

@app.route('/getArticle/<uid>', methods=['GET'])
def getArticle(uid):
  result = pymdb.getArticle(uid)
  return jsonify(result="success", result2=result)

@app.route('/deleteArticle/<id>', methods=['GET'])
def deleteArticle(id):
  result = pymdb.deleteArticle(id)
  if result == True:
    return jsonify(result="success")
  else:
    return jsonify(result="fail")

@app.route('/mypage', methods=['GET', 'POST'])
def mypage():
  if 'uid' in session:
    uid = session['uid']
    uname = pymdb.getName(uid)
    date = pymdb.getDate(uid)
    print(date)
    return render_template('mypage.html', uid=uid, uname=uname)
  else:
    return redirect(url_for("home"))

@app.route('/', methods=['GET', 'POST'])
def home():
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
        name = pymdb.extractName(uid)
        session['uid'] = uid
        return redirect(url_for("mypage")) # alert
      else:
        flash("아이디 및 비밀번호를 다시 확인하세요!", category='error')
    else:
      flash("아이디 및 비밀번호를 다시 확인하세요!", category='error')
      
  return render_template('login.html')
 
@app.route('/register', methods=['GET', 'POST'])
def register():
  return render_template('register.html')

@app.route('/test', methods=['GET', 'POST'])
def test():
  if 'uid' in session:
    uid = session['uid']
    uname = pymdb.getName(uid)
    result = pymdb.getArticle(uid)
    date = pymdb.getDate(uid)
    print(date)
    if len(result) == 0:
      return render_template('test.html', uid=uid, uname=uname)
    else:
      return render_template('test.html', uid=uid, result=result, uname=uname)
  else:
    return redirect(url_for("home"))

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
    print("Register Success: ", uname, uid, upw)
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
  
@app.route('/login', methods=["POST"])
def loginproc():
  data = request.get_json()
  uid = data['uid']
  upw = data['upw']
  
  if uid != 'None' and upw != 'None':
    plain_text = upw.encode('UTF-8')

    if pymdb.isMember(uid) == True:
      dbdata = pymdb.memberPW(uid)
      origin_pw = bytes.fromhex(dbdata) # DB에 저장되어 있는 값
      if bcrypt.checkpw(plain_text, origin_pw) == True: # 로그인 성공 case
        name = pymdb.extractName(uid)
        return jsonify(result="success")
      else:
        flash("아이디 및 비밀번호를 다시 확인하세요!", category='error')
        return jsonify(result="fail")
    else:
      flash("아이디 및 비밀번호를 다시 확인하세요!", category='error')
      return jsonify(result="fail")
    
if __name__ == '__main__':
  app.secret_key = 'THISISSECRETKEYFORJUNGLE'
  app.config['SESSION_TYPE'] = 'filesystem'
  app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=5)
  app.run('0.0.0.0', port=5500, debug=True)