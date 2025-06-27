from flask import Flask, render_template,request,url_for, flash, redirect, abort
from flask_bootstrap import Bootstrap
import sqlite3
import datetime

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn
Mnow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
w=0.0
h=0.0
bmi=0.0
info=''


@app.route("/user", methods=('GET', 'POST'))
def user():
    if request.method == 'POST':
        global w
        global h
        global bmi
        global info
        global Mnow    

        conn = get_db_connection()
        posts = conn.execute('INSERT INTO bmi (w, h, bmi, info, time ) VALUES (?, ?, ?, ?, ?)',
                        (w, h, bmi, info, Mnow ))        
        
        conn.commit()        
        return redirect(url_for("login")) 



@app.route('/login')
def login():   

    conn = get_db_connection()    
    posts = conn.execute('SELECT * FROM bmi').fetchall()
    conn.commit() 
    conn.close()       
    return render_template('list.html', posts=posts)

@app.route('/', methods=['GET', 'POST']) 
def index():
    global w
    global h
    global bmi
    global info 
    if request.method == 'POST': 
        #BMI = 體重(公斤) / 身高2(公尺2)
        w = float(request.form.get('w'))
        h = float(request.form.get('h'))
        bmi= w/(h*h)*10000
        if bmi>=0 and bmi<18.5:
            info='體重過輕'
        elif bmi>=18.5 and bmi<24  :
            info='正常範圍'
        elif bmi<0:
            info='-資料有誤，重新輸入-'
        else:
            if bmi>=24 and bmi<27:
                info='過重'
            elif bmi>=27 and bmi<30:
                info='輕度肥胖'
            elif bmi>=30 and bmi<35:
                info='中度肥胖'
            else:
                info='重度肥胖'
        
        
  
        return render_template('index.html',bmi=bmi,h=h,w=w,info=info)
    else:
        return render_template('index.html',bmi=bmi,h=h,w=w,info=info)

if __name__ == '__main__':
    app.run()