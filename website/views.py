from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

#
topics = [ # type: List of Dictionaries
      {'id':1, 'title': 'html', 'body': 'html is....'},
      {'id':2, 'title': 'css', 'body': 'css is....'},
      {'id':3, 'title': 'javascript', 'body': 'javascript is....'}
]
#

# Root Page
@views.route('/')
def home():
    return render_template('home.html', topics = topics)

@views.route('/about/')
def about():
   return render_template('about.html')

@views.route('/read/<int:id>/')
def read(id):
   print(id)
   return f'Read {id}'

@views.route('/hello/')
def hello():
   return render_template('hello.html')

@views.route('/list/')
def list():
   return render_template('list.html')

@views.route('/result/')
def result():
   return render_template('result.html')
