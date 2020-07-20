# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask import session
import requests #To access our API
import jeopardy as jp

# -- Initialization section --
app = Flask(__name__)
## secret key for session (In production, you would set this key via an environment variable)
app.secret_key = b'HO\xf8\xff+\n\x1e\\~/;}'
# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    response = requests.get('http://jservice.io/api/random').json()
    clue = response[0]
    session ["clue"] = clue
    session ["score"] = 0
    session ["name"] = "Anjali"
    data = {
            "score": response[0]["value"],
            "question": response[0]["question"]
        }
    return render_template('index.html',data=data)

@app.route("/jeopardy",methods=["POST","GET"])
def jeopardy():
    if request.method=="GET":
        return "you're getting the answer page"
    else:
        form = request.form
        user_input = form["answer"]
        data = {
            "output" : jp.match_clue(user_input,session["clue"]["answer"])
            
        }
        return render_template("jeopardy.html",data=data)