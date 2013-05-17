import os
from flask import Flask, request, json

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/')
def listen():
  message = json.loads(request.args.get('message', ''))
  return 'Echo: ' + json.dumps(message)