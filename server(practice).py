from flask import Flask, request, redirect
import random

app = Flask(__name__)

nextId = 4 
topics = [ # 이 부분은 데이터베이스를 이용해야한다.
      {'id':1, 'title': 'html', 'body': 'html is....'},
      {'id':2, 'title': 'css', 'body': 'css is....'},
      {'id':3, 'title': 'javascript', 'body': 'javascript is....'}
]

def template(contents, content): #중복제거, ul은순서가 없을 때 사용한다. 
   return f''' <!doctype html>
   <html>
      <body>
      <h1><a href="/">WEB</a></h1>
      <ol>
          {contents}
      </ol>
      {content} 
      <ul> 
         <li><a href ="/create/">create<a/></li>
      </ul>
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
   

@app.route('/create/', methods = ['GET','POST'])
def create():
   if(request.method == 'GET'):
      content = '''
      <form action ="/create/" method = "POST">
            <p><input type ="text" name = "title" placeholder = "title"></p>
            <p><textarea name = "body" placeholder = "body"></textarea></p>
            <p><input type = "submit" value = "create"></p>
      </form>
      '''
      return template(getContents(), content)

   elif request.method == 'POST':
      global nextId #nextId를 전역변수로 지정
      title = request.form['title']
      body = request.form['body']
      newTopic = {'id': nextId, 'title': title, 'body': body}
      topics.append(newTopic) #데이터 추가
      url = '/read/'+str(nextId)+'/' #nextId를 문자열로, 이유:nextId를 문자열과 결합해야하니까
      nextId = nextId + 1 
      return redirect(url)

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
