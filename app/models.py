import re
import sqlite3
from flask import request, session
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from app import app
import os

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
    password_hash = db.Column(db.String(128), nullable=True)
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
    bookgenre = db.relationship('Book', backref='genre', lazy='dynamic')
    status = db.Column(db.Integer, default=1)

    def __repr__(self):
        genre_data = {
            'Genre ID': self.genre_id,
            'Genre': self.genre,
            'Type': self.type,
            'Status':self.status
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
    genre_id = db.Column(db.Integer,db.ForeignKey('genre.genre_id'),nullable=False)

    book_rate = db.relationship('Ratings', backref='book', lazy='dynamic')
    status = db.Column(db.Integer, default=1)

    def __repr__(self):
        book_data = {
            'Book ID': self.id,
            'Book Name': self.title,
            'Image': self.image,
            'Author': self.author,
            'Description': self.description,
            'Genre ID': self.genre_id,
            'Book Rate': self.book_rate,
            'Status': self.status
        }

        #response = '<Book %s>' % data
        #return repr(response)
        return book_data

class Ratings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    rating = db.Column(db.Integer, nullable=True)
    comment = db.Column(db.String(64))
   # date = db.Column(db.INTEGER, nullable=False, date=True)

    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))

    def __repr__(self):
        ratings_data = {
            'Rating ID': self.id,
            'Book ID': self.book_id,
            'User ID': self.user_id,
            'rating': self.rating,
            'comment': self.comment,
           # 'date': self.date
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
    rows = Book.query.filter(Book.status == 1)
    print rows
    return rows


def get_unassigned_book(gid):
    cur.execute("SELECT * FROM book")
    query_ret = cur.fetchall()
    return (query_ret)


def get_user_book(username):
    # query
    cur.execute(
        "SELECT * FROM book INNER JOIN user_library ON book.id = user_library.book_id INNER JOIN user ON user.id = user_library.user_id where username = '" + username + "'")
    query_ret = cur.fetchall()
    print (query_ret)
    return query_ret


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
    cur.execute("select * from user where username LIKE '%" + uid + "%'")
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
    if bool(re.search(r'[\d!#$%&*+-.^_`|~:]+$', request.form['registerFirstname'])) or bool(re.search(r'[\d!#$%&*+-.^_`|~:]+$', request.form['registerLastname'])) or request.form['registerUsername'] == '' or request.form['registerFirstname'] == '' or request.form['registerLastname'] == '' or request.form['registerEmail'] == '' or request.form['registerPhoneNum'] == '':
        return 'error1'
    else:
        username = request.form['registerUsername']
        firstname = request.form['registerFirstname']
        lastname = request.form['registerLastname']
        email = request.form['registerEmail']
        phone = request.form['registerPhoneNum']
        usertype = request.form['registerUserType']
        password_hash= generate_password_hash('123456')
        cur.execute(
            "insert into user (username, firstname, lastname, email, balance, phone, password,usertype,password_hash) VALUES (?,?,?,?,?,?,?,?,?)",
            (username, firstname, lastname, email, '0', phone, '123456',usertype,password_hash))
        db.commit()
        regpost = [(username,firstname, lastname,email,phone,usertype,password_hash)]
        return regpost


def add_book():
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    target = os.path.join(APP_ROOT, 'static/img/books')
    if bool(re.search(r'[\d!#$%&*+-.^_`|~:]+$', request.form['author'])):
        return 'error1'
    elif request.form['title'] == '' or request.form['description'] == '' or request.form['author'] == '':
        return 'error2'
    else:
         title=request.form['title']
         description=request.form['description']
         author=request.form['author']
         image = request.files['image']
         filename = (secure_filename(image.filename))
         destination = ("/".join([target,filename]))
         path = "/static/img/books/"+filename
         print (path)
         print(author)
         print(destination)
         image.save(destination)
         cur.execute("insert into book (title, description, author,image)"
                     " VALUES (?,?,?,?)", (title, description, author,path))
         db.commit()
         genrepost = [(title, description, author,filename)]
         print (genrepost)
         return genrepost

def add_library():
    if request.form['book'] == '':
        return 'error2'
    else:
        book=request.form['book']
        user=session['token']
        cur.execute("select id from user where username = '" + user + "'")
        user=cur.fetchone()
        user_id=user[0]
        cur.execute("insert into user_library (user_id, book_id) VALUES (?,?)", (user_id, book))
        db.commit()
        lib = [(book,user_id)]
        print(lib)
        return lib


def get_a_book(bid):
    cur.execute("select * from book where id = " + (bid))
    books = cur.fetchall()
    return books


def add_book_genre(gid):
    bid = request.form['book_id']
    cur.execute("update book set genre_id = ? where id = ?", (gid, bid))
    db.commit()
    addto_genre = [(gid, bid)]
    return addto_genre


def get_genres():
    #cur.execute("select * from genres")
    #genres = cur.fetchall()
    #return genres
    #rows = Genre.query.all()
    rows = Genre.query.filter(Genre.status == 1)
    print rows
    return rows

def get_a_genre(gid):
    cur.execute("select * from genre where genre_id = " + (gid))
    genres = cur.fetchall()
    return genres


def add_genres():
     if bool(re.search(r'[\d!#$%&*+.^_`|~:]+$', request.form['genre'])):
         return 'error1'

     elif request.form['genre'] == '':
         return 'error2'

     else:
        genre_type=request.form['type']
        genre_name=request.form['genre']
        cur.execute("insert into genre (type, genre) VALUES (?,?)", (genre_type, genre_name))
        db.commit()

        genrepost = [(genre_type,genre_name)]
        return genrepost


def add_rating():
    if request.form['book_id'] == '' or request.form['rating'] == '' or request.form['comment'] == '':
        return 'error2'
    else:
        book_id=request.form['book_id']
        rating=request.form['rating']
        comment=request.form['comment']
        user=session['token']
        cur.execute("select id from user where username = '" + user + "'")
        user=cur.fetchone()
        user_id=user[0]
        cur.execute("insert into ratings (book_id, user_id, rating, comment) VALUES (?,?,?,?)", (book_id, user_id, rating, comment))
        db.commit()
        retrate = [(book_id,rating,comment)]
        return retrate

def get_rating(bid):
    cur.execute("select * from ratings inner join book on ratings.book_id = book.id inner join user on ratings.user_id = user.id where ratings.book_id = " + (bid))
    books=cur.fetchall()
    return books

def delete_genres(gid):
    genre_id = request.form['id']
    genre = request.form['genre']
    type = request.form['type']
    cur.execute("delete from genres where genre_id = " + (gid))
    db.commit()
    delgenre = [(genre_id,genre,type)]
    return delgenre
    #gen=Genre.query.get(gid)
    #db.session.delete(gen)
    #db.session.commit()
    #print gen
    #return


def delete_books(bid):
    book_id = request.form['bookid']
    title = request.form['book_name']
    description = request.form['description']
    image = request.form['image']
    cur.execute("delete from books where book_id = " + (bid))
    db.commit()
    delbook = [(book_id,title,description,image)]
    return delbook
    # book=Book.query.get(bid)
    # db.session.delete(book)
    # db.session.commit()
    # print book
    # return


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
