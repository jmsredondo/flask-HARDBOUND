from flask import Flask
from flask import session
from flask import render_template
from models import *
from flask import jsonify
#from flask_sqlalchemy import SQLAlchemy
from app import app

#get list of books
def getbook():

    query_dict = []

    for book in get_book():
        book_as_dict = {
            'book_id': book[0],
            'book_name': book[1]
        }
        query_dict.append(book_as_dict)

    print (query_dict)

    return (query_dict)

#get list of categories
def getcategories():
    pass
#get book for each category
def getbook_per_cat():
    pass
def getusers():
    users_dict = []

    for user in get_users():
        user_as_dict = {
            'id': user[0],
            'username': user[1],
            'firstname': user[2],
            'lastname': user[3],
            'email': user[4],
            'balance': user[5],
            'phonenumber': user[6],
            'password': user[7]
        }
        users_dict.append(user_as_dict)

    print (users_dict)
    return users_dict

def getlogin():
    userlogin = login()
    print userlogin
    return userlogin

def login():
     cur.execute("select lastname, password from users where username='"+request.form['username']+"'and password = '"+request.form['password']+"'")
     rows=cur.fetchone()
     if rows != None:
        session['token'] = rows[0]
     else:
        session['token'] = []
     return rows
def adduser():
    add_user()

