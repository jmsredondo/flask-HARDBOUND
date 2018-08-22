import re
import sqlite3
from flask import request, session
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

from flask import jsonify


class User(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False,autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    firstname = db.Column(db.String(64), nullable=False)
    lastname = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    balance = db.Column(db.Float)
    phone = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    usertype = db.Column(db.String(128))
    user_rate = db.relationship('Ratings', backref='user', lazy='dynamic')

    # user_type = db.Column(ENUM('Admin', 'User'), nullable=False)

    # posts = db.relationship('Post', backref='author', lazy='dynamic')
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        user_data = {
            'user_id': self.id,
            'username': self.username,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'email': self.email,
            'balance': self.balance,
            'phone': self.phone,
            'password': self.password,
            'password_hash': self.password_hash,
            'usertype': self.usertype,
            'user_rate': self.user_rate
            # 'user_type': self.user_type

        }

        #response = '<User %s>' % data
        #return repr(response)
        return user_data

class Genre(db.Model):
    genre_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    genre = db.Column(db.String(64), unique=True, nullable=False)
    type = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        genre_data = {
            'Genre ID': self.genre_id,
            'Genre': self.genre,
            'Type': self.type
        }

        #response = '<Genre %s>' % data
        #return repr(response)
        return genre_data

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    image = db.Column(db.BLOB)
    author = db.Column(db.String(64))
    description = db.Column(db.String(64))

    book_rate = db.relationship('Ratings', backref='book', lazy='dynamic')

    def __repr__(self):
        book_data = {
            'Book ID': self.id,
            'Book Name': self.title,
            'Image': self.image,
            'Author': self.author,
            'Description': self.description,
            'Book Rate': self.book_rate
        }

        #response = '<Book %s>' % data
        #return repr(response)
        return book_data

class Ratings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    rating = db.Column(db.Integer, nullable=True)
    comment = db.Column(db.String(64))

    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))

    def __repr__(self):
        ratings_data = {
            'Rating ID': self.id,
            'Book ID': self.book_id,
            'User ID': self.user_id,
            'rating': self.rating,
            'comment': self.comment
        }

        #response = '<Ratings %s>' % data
        #return repr(response)
        return ratings_data

class User_Library(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))

    def __repr__(self):
        library_data = {
            'Library ID': self.id,
            'Book ID': self.book_id,
            'User ID': self.user_id
        }
        return library_data

DATABASE = 'app.db'
# connect to database
db = (sqlite3.connect(DATABASE, check_same_thread=False))
cur = db.cursor()


# get book list
def get_book():
    # query
    #cur.execute("SELECT * FROM books")
    #query_ret = cur.fetchall()
    #return (query_ret)
    rows = Book.query.all()
    #print rows
    return rows


def get_unassigned_book(gid):
    cur.execute("SELECT * FROM books where genre_id !=" + gid + " or genre_id is null")
    query_ret = cur.fetchall()

    return (query_ret)


def get_user_book(username):
    # query
    cur.execute(
        "SELECT * FROM books INNER JOIN user_library ON books.book_id = user_library.book_id INNER JOIN users ON users.id = user_library.user_id where username = '" + username + "'")
    query_ret = cur.fetchall()
    print ('EY')
    print (query_ret)
    return (query_ret)


# get book categories
def get_category():
    pass


# get book for each category
def get_book_per_cat():
    pass


# get users
def get_users():
    #cur.execute("select * from users")
    #rows = cur.fetchall()
    #return rows
    # print rows
    rows = User.query.all()
    return rows



def get_a_user(uid):
    cur.execute("select * from users where username LIKE '%" + uid + "%'")
    rows = cur.fetchall()
    return rows


'''
def search_users(username):
    cur.execute("select * from users where username LIKE '%" + username + "%'")
    users = cur.fetchall()
    return users
'''


def login():
     cur.execute("select username, password, usertype from users where username='"+request.form['username']+"'and password = '"+request.form['password']+"'")
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


def add_user():
    if bool(re.search(r'\d', request.form['registerFirstname'])) or bool(re.search(r'\d', request.form['registerLastname'])) or request.form['registerUsername'] == '' or request.form['registerFirstname'] == '' or request.form['registerLastname'] == '' or request.form['registerEmail'] == '' or request.form['registerPhoneNum'] == '':
        return 'error1'
    else:
        username = request.form['registerUsername']
        firstname = request.form['registerFirstname']
        lastname = request.form['registerLastname']
        email = request.form['registerEmail']
        phonenumber = request.form['registerPhoneNum']
        cur.execute(
            "insert into users (username, firstname, lastname, email, balance, phonenumber, password) VALUES (?,?,?,?,?,?,?)",
            (username, firstname, lastname, email, '0', phonenumber, '123456'))
        db.commit()
        regpost = [(username,firstname, lastname,email,phonenumber)]
        return regpost


def add_book():
    # if bool(re.search(r'\d', request.form['title'])) or bool(re.search(r'\d', request.form['description'])) or bool(re.search(r'\d', request.form['author'])):
    #     return 'error1'
    # elif request.form['title'] == '' or request.form['description'] == '' or request.form['author'] == '':
    #     return 'error2'
    # else:
        title=request.form['title']
        description=request.form['description']
        author=request.form['author']
        cur.execute("insert into books (title, description, author) VALUES (?,?,?)", (title, description, author))
        db.commit()
        genrepost = [(title, description, author)]
        return genrepost


def add_library():
    if bool(re.search(r'\d', request.form['book'])):
        return 'error1'
    elif request.form['book'] == '':
        return 'error2'
    else:
        book=request.form['book']
        user=session['token']
        cur.execute("select id from users where username = '" + user + "'")
        user=cur.fetchone()
        user_id=user[0]
        cur.execute("insert into user_library (user_id, book_id) VALUES (?,?)", (user_id, book))
        db.commit()


def get_a_book(bid):
    cur.execute("select * from books where book_id = " + (bid))
    books = cur.fetchall()
    return books


def add_book_genre(gid):
    bid = request.form['book_id']
    cur.execute("update books set genre_id = ? where book_id = ?", (gid, bid))
    db.commit()


def get_genres():
    #cur.execute("select * from genres")
    #genres = cur.fetchall()
    #return genres
    rows = Genre.query.all()
    return rows

def get_a_genre(gid):
    cur.execute("select * from genres where genre_id = " + (gid))
    genres = cur.fetchall()
    return genres


def add_genres():
    # if bool(re.search(r'\d', request.form['genre'])):
    #     return 'error1'
    #
    # elif request.form['genre'] == '':
    #     return 'error2'
    #
    # else:
        genre_type=request.form['type']
        genre_name=request.form['genre']
        cur.execute("insert into genre (type, genre) VALUES (?,?)", (genre_type, genre_name))
        db.commit()

        genrepost = [(genre_type,genre_name)]
        return genrepost


def add_rating():
    if bool(re.search(r'\d', request.form['book_id'])) or bool(re.search(r'\d', request.form['rating'])) or bool(re.search(r'\d', request.form['comment'])):
        return 'error1'
    elif request.form['book_id'] == '' or request.form['rating'] == '' or request.form['comment'] == '':
        return 'error2'
    else:
        book_id=request.form['book_id']
        rating=request.form['rating']
        comment=request.form['comment']
        user=session['token']
        cur.execute("select id from users where username = '" + user + "'")
        user=cur.fetchone()
        user_id=user[0]
        cur.execute("insert into ratings (book_id, user_id, rating, comment) VALUES (?,?,?,?)", (book_id, user_id, rating, comment))
        db.commit()

def get_rating(bid):
    cur.execute("select * from ratings inner join books on ratings.book_id = books.book_id where ratings.book_id = " + (bid))
    books=cur.fetchall()
    return books

def delete_genres(gid):
    cur.execute("delete from genres where genre_id = " + (gid))
    db.commit()


def delete_books(bid):
    cur.execute("delete from books where book_id = " + (bid))
    db.commit()


"""      
class genre(db.Model):
    genre_id =  db.Column(db.Integer, unique=True, primary_key=True, nullable=False,auto_increment)
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
        
class book(db.Model):
    book_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False,auto_increment)
    title = db.Column(db.String(128), nullable=False)
    image = db.Column(db.BLOB)
    author = db.Column(db.String(64))
    description = db.Column(db.String(64))


    def __repr__(self):
        data = {
            'Book ID': self.book_id,
            'Book Name': self.title,
            'Image': self.image,
            'Description': self.description
        }

        response = '<Book %s>' %
        """
