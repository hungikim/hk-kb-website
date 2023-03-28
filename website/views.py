from flask import Blueprint, render_template, request, flash
from flask_login import current_user
from .models import Post
from . import db

views = Blueprint('views', __name__)

# Root Page
@views.route('/', methods = ['GET', 'POST'])
def home():
   if request.method == 'POST':
      print("posting..")
      post = request.form.get('post')
      new_post = Post(text=post, user_id=current_user.id)
      db.session.add(new_post)
      db.session.commit()
      flash('Your post has been created', category='success')
   
   posts = Post.query.all()

   return render_template('home.html', posts=posts)

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
