import requests
from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def fbwebhook_get():
    return requests.get("http://www.google.com/?=hello world").text
