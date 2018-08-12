import sqlite3
import request

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
    return rows

def login_user():
    cur.execute("select * from users where lastname = '" + request.form['username'] + "' and password = '" + request.form[
            'username'] + "'")