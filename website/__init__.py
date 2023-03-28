from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
   app = Flask(__name__)
   app.secret_key = 'some random key haha'
   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DB_NAME # We're using sqlite for db
   db.init_app(app)

   from .views import views
   from .auth import auth

   app.register_blueprint(views, url_prefix='/')
   app.register_blueprint(auth, url_prefix='/')

   from .models import User, Post

   create_database(app)

   return app

def create_database(app):
   if not path.exists('website/' + DB_NAME):
      with app.app_context():
         db.create_all()
      print("Database has been created")




