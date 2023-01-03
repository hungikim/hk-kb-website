from flask import Flask #연습용
import random

app = Flask(__name__)

@app.route('/')
def index():
   return 'welcome'

@app.route('/create/')
def create():
   return 'Create'

@app.route('/read/1/')
def read():
   return 'Read 1'

app.run(port = 5001, debug = True)
