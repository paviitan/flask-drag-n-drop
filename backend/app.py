from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # CORS allows frontend JavaScript with Python backend

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"