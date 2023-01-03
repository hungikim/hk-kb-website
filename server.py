from flask import Flask #연습용
import random

app = Flask(__name__)

@app.route('/') #어떠한 것도 입력하지 않을 때 뜸
def index():
   return 'welcome'

@app.route('/create/')
def create():
   return 'Create'

@app.route('/read/<id>/')
def read(id):
   print(id)
   return 'Read ' + id

app.run(port = 5001, debug = True)
