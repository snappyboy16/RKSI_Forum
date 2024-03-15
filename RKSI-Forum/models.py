from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class Student(UserMixin, db.Model):
    __tablename__ = 'Student'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    group_rksi = db.Column(db.String(10))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __init__(self, nickname, name, group_rksi, email, password):
        self.nickname = nickname
        self.name = name
        self.group_rksi = group_rksi
        self.email = email
        self.password = password


class Post(db.Model):
    __tablename__ = 'Posts'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    text = db.Column(db.String(5000))
    date = db.Column(db.Date)
    author = db.Column(db.String(100))

    def __init__(self, title, text, date, email, author):
        self.title = title
        self.text = text
        self.date = date
        self.author = author
