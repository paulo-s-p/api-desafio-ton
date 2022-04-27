from email.policy import default
from flask_sqlalchemy import SQLAlchemy
import datetime
from werkzeug.utils import secure_filename


db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(84), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    firstName = db.Column(db.String(40), nullable=False)
    lastName = db.Column(db.String(60), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.datetime.now())
    posts = db.relationship("Account", backref='users')

    def __init__(self, email, password, firstName, lastName):
        self.email = email
        self.password = password
        self.firstName = firstName
        self.lastName = lastName

class Account(db.Model):
    __tablename__ = 'account'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    value = db.Column(db.String(200) , nullable=False)
    author_id = db.Column(
        db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self,  title, value, author_id):
        
        self.title = title
        self.value = value
        self.author_id = author_id
        
class Access(db.Model):
    __tablename__ = 'access'
    id = db.Column(db.Integer, primary_key=True)
    access = db.Column(db.Integer)

    def __init__(self, id, access):
        self.id = id
        self.access = access
        

