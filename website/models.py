from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
   id = db.Column(db.Integer, primary_key=True)
   email = db.Column(db.String(50), unique=True)
   name = db.Column(db.String(50))
   password = db.Column(db.String(30))
   notes = db.relationship('Post')

class Post(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   data = db.Column(db.String(5000))
   date = db.Column(db.DateTime(timezone=True), default=func.now()) # TODO: Display time in EST no matter where the user is loated?
   user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


 
