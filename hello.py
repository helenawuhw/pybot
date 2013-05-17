import os
import re
from flask import Flask, request, json

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/')
def listen():
  message = json.loads(request.args.get('message', ''))

  response = guacamole(message)

  if response is not None:
    return response

  return ''

"""
`message` will be of the following form:

{
  "text": "how bout u", 
  "id": 927874479, 
  "room": 382086, 
  "user": {
    "name": "Nick Heiner", 
    "email_address": "nick.heiner@opower.com", 
    "room": 382086, 
    "admin": false, 
    "id": 1284158, 
    "avatar_url": "http://dge9rmgqjs8m1.cloudfront.net/global/447cd8c718ec08087db7b11971313dff6b97f7832951b1815b766b238a8774b7e37be1e457d1e9199d969e9ce216b5b730d329452b8599399ef574257ed0cff091a49fb43115e0627eb235e5d7768835/avatar.gif?r=3&quot;", 
    "type": "Member", 
    "created_at": "2012/10/04 14:55:41 0000"
    }, 
  "done": false
}
"""

def guacamole(message):
  if re.findall('guacamole', message['text'], re.I):
    return 'hey did you that Guarapo is 7th most famous guacamole bar in the mid-atlantic region?'