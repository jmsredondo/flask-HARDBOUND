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
            'title': book[0],
            'description': book[1],
            'author': book[4],
            'genre_id': book[5]
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
            'username': user[1],
            'firstname': user[2],
            'lastname': user[3],
            'email': user[4],
            'balance': user[5],
            'phone': user[6],
        }
        users_dict.append(user_as_dict)

    #print (users_dict)
    return users_dict

def searchusers(username):
    users_dict = []

    for user in search_users(username):
        user_as_dict = {
            'username': user[1],
            'firstname': user[2],
            'lastname': user[3],
            'email': user[4],
            'balance': user[5],
            'phone': user[6],
        }
        users_dict.append(user_as_dict)

    #print (users_dict)
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

def getgenres():
    genres_dict = []

    for genre in get_genres():
        genre_as_dict = {
            'type': genre[0],
            'genre': genre[1],
            'genre_id': genre[2]
        }
        genres_dict.append(genre_as_dict)

    print (genres_dict)
    return genres_dict

def adduser():
    add_user()

def addgenre():
    add_genres()

def deletegenre(gid):
    delete_genres(gid)