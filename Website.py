from flask import Flask, render_template
import random

app = Flask(__name__)

topics = [ # type: List of Dictionaries (나중에 쓰기기능을 구현하게 되면 값들이 초기화 됨)
      {'id':1, 'title': 'html', 'body': 'html is....'},
      {'id':2, 'title': 'css', 'body': 'css is....'},
      {'id':3, 'title': 'javascript', 'body': 'javascript is....'}
]

# Content to display when nothing is entered in the URI after the domain
@app.route('/')
def index(): # Display each topic in the topics list as links
   liTags = ''
   for topic in topics:
      liTags = liTags + f'<li><a href = "/read/{topic["id"]}/">{topic["title"]}</a></li>' # use f-string to print strings with variables
   return f''' <!doctype html>
   <html>
      <head>
         <title>Board</title>
      </head>
      <body>
      <h1 align="center"><a href="/">WELCOME</a></h1> <!-- Note: text within an 'a' tag is underlined -->
      <ol>
         {liTags}
      </ol>
      <h2>Welcome</h2>
      Hello, Web
   </body>
</html>
'''

@app.route('/create/')
def create():
   return 'Create'

@app.route('/read/<int:id>/') # int:id -> makes sure that the variable 'id' is an integer
def read(id):
   print(id)
   return f'Read {id}'

@app.route('/hello/')
def hello():
   return render_template('hello.html')

@app.route('/list/')
def list():
   return render_template('list.html')

@app.route('/result/')
def result():
   return render_template('result.html')

@app.route('/user/')
def user():
   return render_template('user.html')


app.run(port = 5001, debug = True)