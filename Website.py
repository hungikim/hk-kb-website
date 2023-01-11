from flask import Flask
import random

app = Flask(__name__)

topics = [ # 리스트와 딕셔너리를 사용했다. (나중에 쓰기기능을 구현하게 되면 값들이 초기화 됨)
      {'id':1, 'title': 'html', 'body': 'html is....'},
      {'id':2, 'title': 'css', 'body': 'css is....'},
      {'id':3, 'title': 'javascript', 'body': 'javascript is....'}
]


@app.route('/') #어떠한 것도 입력하지 않을 때 뜸
def index():
   liTags = ''
   for topic in topics:
      liTags = liTags + f'<li><a href = "/read/{topic["id"]}/">{topic["title"]}</a></li>' #문자열을 변수와 같이 섞을 때 편리한 도구가 f스트링 ('<li>'+topic['title']+'</li> 를 편리하게)
   return f''' <!doctype html> <!-- a는 밑줄을 긋는다 -->
   <html>
      <body>
      <h1><a href="/">WEB</a></h1>
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

@app.route('/read/<id>/') #int:id -> id를 정수라는 것으로 지정
def read(id):
   print(id)
   return 'Read ' + id

app.run(port = 5001, debug = True)