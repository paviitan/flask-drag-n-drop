from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request, render_template, redirect, url_for, send_from_directory

from utils import file_handler, config

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] =  config['UPLOAD_FOLDER']
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
        return "<p>Hello, anonymous weary traveler!</p>"
    else:
        greeting = "<p>Hello, " + name + "! Do you need a room?</p>" + "<br>" + "<a href=\"/upload\"> Yes, please</a>" + "<br>"
        return greeting
        
@app.route("/upload", methods=["GET", "POST"])
#@cross_origin('*')  # not needed?
def upload():
    if request.method == 'POST':
        print(request.headers)
        # check if the post request has the file part
        if 'file' not in request.files:
            return "POST request does not have the file part"
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            # flash('No selected file')
            return "No selected file? Browser submitted an empty file without a filename"
        if file:
            return file_handler(file)
    return render_template("upload.html")

@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)