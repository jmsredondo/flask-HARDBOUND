import sqlite3
from flask import request
from app import db

from flask import jsonify

DATABASE = 'database/database_1.db'
#connect to database
db = (sqlite3.connect(DATABASE,check_same_thread=False))
cur = db.cursor()

#get book list
def get_book():
    # query
    cur.execute("SELECT * FROM books")
    query_ret = cur.fetchall()

    return (query_ret)

#get book categories
def get_category():
    pass

#get book for each category
def get_book_per_cat():
    pass

#get users
def get_users():
    cur.execute("select * from users")
    rows = cur.fetchall()
    print rows
    return rows

def login():
     cur.execute("select lastname, password from users where username='"+request.form['username']+"'and password = '"+request.form['password']+"'")
     rows=cur.fetchone()
     return rows

def add_user():
    username=request.form['registerUsername']
    firstname=request.form['registerFirstname']
    lastname=request.form['registerLastname']
    email=request.form['registerEmail']
    phonenumber=request.form['registerPhoneNum']
    cur.execute("insert into users (username, firstname, lastname, email, balance, phonenumber, password) VALUES (?,?,?,?,?,?,?)", (username, firstname, lastname, email, '0', phonenumber, '123456'))
    db.commit()

def get_genres():
    cur.execute("select * from genres")
    genres=cur.fetchall()
    return genres

"""
class User(db.Model):
    user_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    firstname = db.Column(db.String(64), nullable=False)
    lastname = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    balance = db.Column(db.Float)
    phone = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String(128),nullable =False)
    password_hash = db.Column(db.String(128), nullable=False)
    user_type = db.Column(ENUM('Admin','User'),nullable =False)
    

    # posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        data = {
            'user_id': self.user_id,
            'username': self.username,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'email': self.email,
            'balance': self.balance,
            'phone': self.phone,
            'password: self.password,
            'password_hash': self.password_hash,
            'user_type' :self.user_type
            
        }

        response = '<User %s>' % data
        return repr(response)
        
class genre(db.Model):
    genre_id =  db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    genre = db.Column(db.String(64), unique=True, nullable=False)
    type = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        data = {
            'Genre ID': self.genre_id,
            'Genre': self.genre,
            'Type': self.type
        }

        response = '<Genre %s>' %data
        return repr(response)
        """

