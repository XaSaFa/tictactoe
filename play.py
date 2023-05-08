from flask import Flask, request
from jinja2 import Environment, FileSystemLoader
from flask import Flask, redirect, url_for, session
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

def newGame():
    board = [0,0,0,0,0,0,0,0,0]
    session["tokens1"] = 1
    session["tokens2"] = 0
    session["board"] = board
    session["playerActive"] = 1


@app.route('/')
def default():
    newGame()
    enviroment = Environment(loader=FileSystemLoader("Template/"))
    template = enviroment.get_template("base.html")
    info = {"tokens1": session['tokens1'],"tokens2": session['tokens2'], "board": session["board"]}
    contingut = template.render(info)
    return f'{contingut}'

@app.route('/movement', methods = ['POST', 'GET'])
def move():
    position = request.form['position']
    print(position)
    session["board"][int(position) - 1] = session["playerActive"]
    if session["playerActive"] == 1:
        session["playerActive"] = 2
        session["tokens1"] = 0
        session["tokens2"] = 1
    else:
        session["playerActive"] = 1
        session["tokens1"] = 1
        session["tokens2"] = 0
    info = {"tokens1": session['tokens1'], "tokens2": session['tokens2'], "board": session["board"]}
    enviroment = Environment(loader=FileSystemLoader("Template/"))
    template = enviroment.get_template("base.html")
    contingut = template.render(info)
    return f'{contingut}'