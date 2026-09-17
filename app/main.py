# build 9cd980f0f9
# (auto) fd40b4
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'ok'
