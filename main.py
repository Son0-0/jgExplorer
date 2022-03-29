from flask import Flask, render_template
from flask import request
import pymongo
import bcrypt

app = Flask(__name__)
SECRET_KEY = "THISISSECRETKEY"

@app.route('/login', methods=['GET', 'POST'])
def login():
  return render_template('login.html')

@app.route('/', methods=['GET', 'POST'])
def home():
  if request.method == "POST":
    data = request.form
    uid = data.get('uid')
    upw = data.get('upw')
    
    byte_plain = upw.encode('UTF-8')
    pw_hash = bcrypt.hashpw(byte_plain, bcrypt.gensalt()).hex()
    
    print(uid, upw, pw_hash)
    
    temp_pw = "123"
    tplain = temp_pw.encode('UTF-8')
    dbdata = "2432622431322475726d6f316c526d44353364556955473876466c532e796f394c2f34486f4279677a75475a6e613064635373354634793963366747"
    origin_pw = bytes.fromhex(dbdata) # DB에 저장되어 있는 값
    print(bcrypt.checkpw(tplain, origin_pw))
    
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