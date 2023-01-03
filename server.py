from flask import Flask # 연습용
import random

app = Flask(__name__)

@app.route('/')
def index():
   return str(random.random())

app.run(port = 5001, debug = True)
