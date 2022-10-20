from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # CORS allows frontend JavaScript with Python backend

@app.route("/", methods=["GET"])
def lobby():
    return "<p>You arrive at the hotel lobby. A receptionist waits in silence...</p>"
    
@app.route("/greet", methods=["GET"])
def greet():
    return "<p>Hello, weary traveler!</p>"