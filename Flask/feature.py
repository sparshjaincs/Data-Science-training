from flask import Flask,redirect,url_for,render_template,request,make_response,session,flash
from werkzeug import secure_filename
import os
app=Flask(__name__)
app.secret_key = 'Sparshj18@'


@app.route("/")
def fun1():
    return "hello world"

@app.route("/home/")
def fun2():
    return "home"


@app.route("/<var>/")   # string var
def fun3(var):
    return var

@app.route("/home/<int:var1>/<int:var2>/<int:var3>/")
def fun5(var1,var2,var3):
    return f"<h1 style='color:blue;font-size=30px;' >Your marks is :{var1+var2+var3}</h1>"
@app.route("/home/<name>/<int:var1>/<int:var2>/<int:var3>")
def index2(name,var1,var2,var3):
    return f"<h1 style='color:blue;font-size=30px;' >{name} Your marks is :{var1+var2+var3}</h1>"

# url building
@app.route('/admin')
def hello_admin():
       return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
       return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
       if name =='admin':
          return redirect(url_for('hello_admin'))
       else:
          return redirect(url_for('hello_guest',guest = name))

#  render templates
@app.route("/file")
def file():
    return render_template('file.html')

# cookies
@app.route("/cookies")
def cook():
    return render_template("cookie.html")
@app.route("/getcookie")
def showcookies():
   name = request.cookies.get('USERID')
   return '<h1>welcome '+name+'</h1>'

@app.route("/setcookies" , methods=['POST','GET'])
def cookies():
    if request.method=="POST":
        user=request.form['tex']
        resp=make_response(render_template("readcookie.html"))
        resp.set_cookie('USERID',user)
        return resp


# session
@app.route("/session")
def sess():
    return render_template("session.html")
@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('index'))
@app.route("/login")
def index():
    if 'username' in session:
      username = session['username']
      return 'Logged in as ' + username + '<br>' + "<b><a href = '/logout'>click here to log out</a></b>"
    return "You are not logged in <br><a href = '/session'></b>" + "click here to log in</b></a>"
    
@app.route("/setsession" , methods=['POST','GET'])
def set():
    if request.method=="POST":
        session['username']=request.form['mail']
        return redirect(url_for('index'))
        
## flash
@app.route('/flash')
def index1():
   return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
   error = None
   
   if request.method == 'POST':
      if request.form['username'] != 'admin' or \
         request.form['password'] != 'admin':
         error = 'Invalid username or password. Please try again!'
      else:
         flash('You were successfully logged in')
         return redirect(url_for('index1'))
			
   return render_template('login.html', error = error)


# file upload
@app.route("/file1")
def file1():
    return render_template("upload.html")

@app.route("/uploader" ,methods=['POST','GET'])
def uploades():
    if request.method=="POST":
        f=request.files['fileasd'] 
        f.save(os.path.join('upload',secure_filename(f.filename)))
        return "file uploaded successfully"


if __name__ =='__main__':
    
    app.run(debug=True)
  
    
