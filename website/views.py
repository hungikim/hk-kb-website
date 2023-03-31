from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import current_user
from .models import Post
from . import db
import json

views = Blueprint('views', __name__)

# Root Page
@views.route('/', methods = ['GET', 'POST'])
def home():
   # Handle post request if there is any
   if request.method == 'POST':
      post_text = request.form.get('post-text-area')
      new_post = Post(text=post_text, user_id=current_user.id)
      db.session.add(new_post)
      db.session.commit()
      flash('Your post has been created', category='success')

   # Display all posts
   posts = Post.query.order_by(Post.date.desc()).all()

   return render_template('home.html', posts=posts)

@views.route('/about/')
def about():
   return render_template('about.html')

@views.route('/delete-post/', methods=['POST']) # method = POST only, because GET not needed
def delete_post():
   data = json.loads(request.data)
   post_id = data['postId']
   post = Post.query.get(post_id)
   
   if post:
      if post.user_id == current_user.id:
         db.session.delete(post)
         db.session.commit()
         flash('Your post has been deleted.', category="success")
         return jsonify({})
   
   return 

@views.route('/update-post/', methods=['POST'])
def update_post():
   data = json.loads(request.data)
   post_id = data['postId']
   post = Post.query.get(post_id)
   text = data['text']
   post.text = text
   db.session.commit()
   flash('Your post has been updated.', category="success")
   return jsonify({})