from flask import Flask, request, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
app = Flask(__name__)
boostrap = Bootstrap(app=app)




@app.route('/')  
def index():  
    return render_template('index.html')  
  
  
@app.route('/login')  
def login():  
    a= 'Here is Login'
    return render_template('login.html', username=a)  
  
  
@app.route('/logout')  
def logout():      
    b= 'Here is Logout'
    return render_template('logout.html', username=b)   
  
  
@app.route('/userinfo')  
def userinfo():     
    c= 'Here is UserINFO'
    return render_template('userinfo.html', username=c)   


@app.route('/add0627')  
def add0627():     
    d= 'Here is ADD0627'
    return render_template('userinfo.html', username=d)   



if __name__ == '__main__':
    app.debug = True
    app.run()