from flask import Flask, render_template, request, session
from flask_bootstrap import Bootstrap
import random

app = Flask(__name__)
app.secret_key = "#230dec61-fee8-4ef2-a791-36f9e680c9fc"

@app.route("/", methods=["GET", "POST"])
def index():
    rand1 = session.get("rand1")
    rand2 = session.get("rand2")
    answer = None

    if request.method == "POST":
        if "gen_random" in request.form:
            rand_num = random.randint(1, 99999)
        elif "gen1" in request.form:
            rand1 = random.randint(1, 99999)
            session["rand1"] = rand1
        elif "gen2" in request.form:
            rand2 = random.randint(1, 99999)
            session["rand2"] = rand2
        elif "add" in request.form:
            if rand1 is not None and rand2 is not None:
                answer = rand1 + rand2
                session["answer"] = answer

    return render_template(
        "index.html",
        rand_num=rand_num
        rand1=rand1,
        rand2=rand2,
        answer=answer
    )

@app.route('/login')  
def login():  
    a= 'Here is Login'
    return render_template('login.html', username=a)  

@app.route('/user')  
def userinfo():     
    c= 'Here is UserINFO'
    return render_template('userinfo.html', username=c) 

if __name__ == "__main__":
    app.debug = True
    app.run()
