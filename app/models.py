import sqlite3
from flask import request

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
