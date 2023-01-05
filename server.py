from flask import Flask #연습용
import random

app = Flask(__name__)


topics = [ # 이 부분은 데이터베이스를 이용해야한다.
      {'id':1, 'title': 'html', 'body': 'html is....'},
      {'id':2, 'title': 'css', 'body': 'css is....'},
      {'id':3, 'title': 'javascript', 'body': 'javascript is....'}
]

def template(contents, content): #중복제거 1
   return f''' <!doctype html>
   <html>
      <body>
      <h1><a href="/">WEB</a></h1>
      <ol>
          {contents} 
      </ol>
      {content}
   </body>
</html>
   '''

def getContents(): #중복제거 2
   liTags = ''
   for topic in topics:
      liTags = liTags +f'<li><a href ="/read/{topic["id"]}">{topic["title"]}</a></li>'
   return liTags

@app.route('/') #어떠한 것도 입력하지 않을 때 뜸
def index():
   return template(getContents(), '<h2>Welcome</h2>Hello, WEB')
   

@app.route('/create/')
def create():
   return 'Create'

@app.route('/read/<int:id>/') #int:id -> id를 정수라는 것으로 지정
def read(id):
   title = ''
   body = ''
   for topic in topics: #여기서 조회를 하고
      if id == topic['id']: #그 토픽과 토픽id가 일치하면
         title = topic['title'] #그것을 타이틀과 바디로 지정
         body = topic['body']
         break
   print(title, body)
   return template(getContents(), f'<h2>{title}</h2>{body}')


app.run(port = 5001, debug = True)