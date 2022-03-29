from flask import Flask, render_template, redirect, url_for
from flask import request
import pymongo
import pymdb
import bcrypt

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
  if request.method == "POST":
    data = request.form
    uid = data.get('uid')
    upw = data.get('upw')
    
    plain_text = upw.encode('UTF-8')
    pw_hash = bcrypt.hashpw(plain_text, bcrypt.gensalt()).hex() # DB에 저장될 값
    
    pymdb.register(uid, pw_hash)
    print(uid, upw, pw_hash)
    
    # redirect to /mypage
    #return render_template('mypage.html')
    
    # # DB 저장될 값과 비교
    # temp_pw = "123"
    # db_text_plain = temp_pw.encode('UTF-8')
    # # DB에서 가져온 값
    # dbdata = "2432622431322468765958716939574a45614c677957694756586b6b65424e45344234334a7769794c444836517156475238536c79724d484257754b"
    # origin_pw = bytes.fromhex(dbdata)
    # print(bcrypt.checkpw(db_text_plain, origin_pw))
    
  return render_template('login.html')
 
@app.route('/register', methods=['GET', 'POST'])
def register():
  if request.method == "POST":
    data = request.form
    uid = data.get('uid')
    upw = data.get('upw')
    uname = data.get('uname')
    print(uname, uid, upw)
  return render_template('register.html')

if __name__ == '__main__':
   app.run('0.0.0.0', port=7800, debug=True)
   
@app.route('/mypage', methods=['GET', 'POST'])
def mypage():
  
  return render_template('mypage.html')