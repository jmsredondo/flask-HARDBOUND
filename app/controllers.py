from flask import Flask
from flask import session
from flask import render_template
from models import *
from flask import jsonify
#from flask_sqlalchemy import SQLAlchemy
from app import app

#get list of books
def getbook():
    book_list = []
    for book in get_book():
        book_as_dict = {
            'title': book.title,
            'image':book.image,
            'description': book.description,
            'book_id': book.id,
            'author': book.author,
            'status':book.status,
            'user_type': session['usertype']
            #'genre_id': book[5]
        }
        book_list.append(book_as_dict)

    print (book_list)
    return book_list

def getuserbook(username):

    query_dict = []

    for book in get_user_book(username):
        book_as_dict = {
            'title': book[1],
            'book_id': book[0],
            'author': book[2],
            'description': book[3]
        }
        query_dict.append(book_as_dict)
    return query_dict

def getabook(bid):
    query_dict = []
    for book in get_a_book(bid):
        book_as_dict = {
            'title': book[1],
            'description': book[4],
            'book_id': book[0],
            'author': book[3],
            'genre_id': book[5]
        }
    query_dict.append(book_as_dict)
    return (query_dict)

#same as top function, but do not delete
def getunassignedbook(gid):

    query_dict = []

    for book in get_unassigned_book(gid):
        book_as_dict = {
            'title': book[1],
            'description': book[3],
            'book_id': book[0],
            'author': book[2],
            'genre_id': book[6],
            'image': book[5]
        }
        query_dict.append(book_as_dict)

    return (query_dict)


#get list of categories
def getcategories():
    pass
#get book for each category
def getbook_per_cat():
    pass

def getusers():
    userlist=[]
    for user in User.query.all():
        userli = {
            'username': user.username,
            'firstname': user.firstname,
            'lastname': user.lastname,
            'email': user.email,
            'balance': user.balance,
            'phone': user.phone,
        }
        userlist.append(userli)
    return userlist


    """for user in users_dict():
        user_as_dict = {
            'username': user[1],
            'firstname': user[2],
            'lastname': user[3],
            'email': user[4],
            'balance': user[5],
            'phone': user[6],
        }
        users_dict.append(user_as_dict)"""

    #return jsonify(users_dict), 200

def getauser(uid):
    users_dict = []

    for user in get_a_user(uid):
        user_as_dict = {
            'username': user[1],
            'firstname': user[2],
            'lastname': user[3],
            'email': user[4],
            'balance': user[5],
            'phone': user[6],
        }
        users_dict.append(user_as_dict)

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

    return users_dict

def getlogin():
    userlogin = login()
    return userlogin


def login():
     cur.execute("select username, password, usertype from user where username='"+request.form['username']+"'and password = '"+request.form['password']+"'")
     rows=cur.fetchone()
     if rows != None:
        session['token'] = rows[0]
        if rows[2] == 'admin' and request.form['usertype'] == 'admin':
            session['usertype'] = True
        elif rows[2] == 'user' and request.form['usertype'] == 'user':
            session['usertype'] = False
        else:
            session['usertype'] = None
     else:
        session['token'] = None
     return rows


def getgenres():
    genres_dict = []

    for genre in get_genres():
        genre_as_dict = {
            'type': genre.type,
            'genre': genre.genre,
            'genre_id': genre.genre_id,
            'status': genre.status,
            'user_type': session['usertype']
        }
        genres_dict.append(genre_as_dict)

    return genres_dict

def getagenres(gid):
    genres_dict = []

    for genre in get_a_genre(gid):
        genre_as_dict = {
            'type': genre[2],
            'genre': genre[1],
            'genre_id': genre[0]
        }
        genres_dict.append(genre_as_dict)

    return genres_dict

def getrating(bid):
    rating_dict = []

    for rating in get_rating(bid):
        rating_as_dict = {
            'rating': rating[2],
            'comment': rating[3],
            'firstname': rating[14],
            'lastname': rating[15]

        }
        rating_dict.append(rating_as_dict)

    return rating_dict

def adduser():
    # if add_user() == 'error1':
    #     return add_user()
    # else:
        adduser_dict = []

        for aduser in add_user():
            addusers_as_dict = {
                'username': aduser[0],
                'firstname': aduser[1],
                'lastname': aduser[2],
                'email': aduser[3],
                'phonenumber': aduser[4],
            }
            adduser_dict.append(addusers_as_dict)
        return adduser_dict

def addgenre():
    result = add_genres()
    if result == 'error1' or result == 'error2':
        return add_genres()
    else:
       addgenre_dict = []

       for adgen in result:
           addgenres_as_dict = {
               'type': adgen[0],
               'genre': adgen[1]
           }
           addgenre_dict.append(addgenres_as_dict)
       return addgenre_dict


def addbook():
    result = add_book()
    if result == 'error1' or result == 'error2':
        return add_book()
    else:
        addbook_dict = []

        for adbook in result:
            addbook_as_dict = {
                'title': adbook[0],
                'description': adbook[1],
                'author': adbook[2],
                'image': adbook[3]
            }
            addbook_dict.append(addbook_as_dict)
        return addbook_dict

def addbookgenre(gid):
    addtogenre_dict = []

    for adtogen in add_book_genre(gid):
        addtogenre_as_dict = {
            'genre_id': adtogen[0],
            'book_id': adtogen[1]
        }
        addtogenre_dict.append(addtogenre_as_dict)
    return addtogenre_dict

def addlibrary():
    addtolib_dict = []
    for adlib in add_library():
        addtolib_as_dict = {
            'book': adlib[0],
            'user': adlib[1]
        }
        addtolib_dict.append(addtolib_as_dict)
    return addtolib_dict

def addrating():
    addtorate_dict = []
    for adrate in add_rating():
        addtorating_as_dict = {
            'book_id': adrate[0],
            'rating': adrate[1],
            'comment': adrate[2]
        }
        addtorate_dict.append(addtorating_as_dict)
    return addtorate_dict

def deletegenre(gid):
    delete_genre_dict = []
    for delgen in delete_genres(gid):
        delete_genre_as_dict = {
            'genre_id': delgen[0],
            'genre': delgen[1],
            'type': delgen[2],
        }
        delete_genre_dict.append(delete_genre_as_dict)
    return delete_genre_dict

def deletebook(bid):
    delete_book_dict = []
    for delbook in delete_books(bid):
        delete_book_as_dict = {
            'book_id': delbook[0],
            'title': delbook[1],
            'description': delbook[2],
            'image': delbook[3]
        }
        delete_book_dict.append(delete_book_as_dict)
    return delete_book_dict
