import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def listen():
    return 'Echo: ' + request.args.get('message', '')