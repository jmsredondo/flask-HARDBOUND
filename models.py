import sqlite3
from flask import jsonify

DATABASE = 'test.db'
#connect to database
db = (sqlite3.connect(DATABASE))
cur = db.cursor()

#get book list
def get_book():
    # connect to database
    db = (sqlite3.connect(DATABASE))
    cur = db.cursor()
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
    pass