# Create your models here.
from app import db
from sqlalchemy.orm import backref
from flask_login import UserMixin
import enum

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(280), nullable=False)
    publish_date = db.Column(db.Date)

    replies - db.relationship('Reply', back_populates='post')

    user = db.relationship('User', back_populates='posts')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Reply(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(280), nullable=False)
    publish_date = db.Column(db.Date)

    user = db.relationship('User', back_populates='replies')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    post = db.relationship('Post', back_populates='replies')
    post_id = db.Column(db.Integer, db.ForeignKey('post_id'), nullable=False)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    display_name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(200), nullable=False)

    posts = db.relationship('Post', back_populates='user')
    replies = db.relationship('Reply', back_populates='user')

    def __repr__(self):
        return f'<User: {self.username}>'


    