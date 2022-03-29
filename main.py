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