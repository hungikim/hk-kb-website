from flask import Blueprint, render_template, request, redirect, flash, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)

# Use both GET and POST because GET can only send URL while POST can take HTTP request 
@auth.route('/sign_up/', methods = ['GET', 'POST'])
def sign_up():
   if request.method == 'POST':
      user_email = request.form.get('user_email')
      user_name = request.form.get('user_name')
      user_pw = request.form.get('user_pw')
      user_pw_confirm = request.form.get('user_pw_confirm')
      print(user_email + user_name + user_pw + user_pw_confirm)
      
      # Check if the email already exists
      user = User.query.filter_by(email=user_email).first()
      if user:
          flash('Email already exists.', category='error')
          return render_template('sign_up.html')
      
      else:
          user = User(email=user_email, name=user_name, password=generate_password_hash(user_pw, method='sha256'))
          db.session.add(user)
          db.session.commit()
          flash('Account Succesfully Created!', category='success')
          return redirect(url_for('views.home'))
   
   return render_template('sign_up.html')

@auth.route('/log_in/', methods = ['GET', 'POST'])
def log_in():
    if request.method == 'POST':
        user_email = request.form.get('user_email')
        user_pw = request.form.get('user_pw')
    
        # Check if the user with the specified email exists
        user = User.query.filter_by(email=user_email).first()
        if user:
            # Check if passwords match
            if check_password_hash(user.password, user_pw):
                flash('You are now logged in.', category='success')
            else: flash('Password does not match. Please check your password.',category='error')
        else: flash('The account with the email you type does not exist.', category='error')
        
        
             
          
       # do some check
       
    return render_template('log_in.html')

@auth.route('/log_out/')
def log_out():
   return "<div>Logged out</div>"