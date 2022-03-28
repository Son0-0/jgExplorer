from flask import Flask, render_template
app = Flask(__name__)

@app.route('/home')
def home():
   return render_template('main.html')
 
@app.route('/login')
def login():
   return render_template('login.html')
 
@app.route('/register')
def register():
   return render_template('register.html')

if __name__ == '__main__':
   app.run('0.0.0.0', port=7899, debug=True)