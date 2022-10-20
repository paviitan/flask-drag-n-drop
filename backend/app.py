from flask import Flask
from flask_cors import CORS
from flask import request
from flask import render_template

app = Flask(__name__)
CORS(app) # CORS allows frontend JavaScript with Python backend

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")
    
@app.route("/lobby", methods=["GET"])    
def lobby():
    return "<p>You arrive at the hotel lobby. A receptionist waits in silence...</p>"
    
@app.route("/exit/", methods=["GET"])
def exit():
    return render_template("exit.html")
    
@app.route("/greet", methods=["GET", "POST"])
def greet():
    name = request.form['Name']
    if(name == None or name == ''):
        return "<p>Hello, weary traveler!</p>"
    else:
        greeting = "<p>Hello, " + name + "!</p>"
        return greeting