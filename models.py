import sqlite3
from flask import jsonify

DATABASE = 'test.db'
#connect to database
db = (sqlite3.connect(DATABASE))
cur = db.cursor()

#database connection
def get_book():
    # connect to database
    db = (sqlite3.connect(DATABASE))
    cur = db.cursor()
    # query
    cur.execute("SELECT * FROM books")
    query_ret = cur.fetchall()

    return (query_ret)


