from flask import render_template
from flask import flash
from controllers import *
from flask import redirect,url_for
#import app from class Flask from app directory
from app import app

#route to index
@app.route('/')
@app.route('/index',methods=['POST','GET'])
def login():
    return render_template("login.html")

@app.route('/dashboard', methods=['POST','GET'])
def dashboard():
    rows = getlogin()
    if rows is not None and session['token'] is not None:
        return render_template('dashboard.html')
    else:
        return redirect(url_for('login'))


@app.route('/book',methods=['GET'])
def getbooks():
    books = getbook()
    genres = getgenres()
    return render_template('bookList.html',books=books, genres=genres)


@app.route('/users', methods=['GET'])
def getregister():
    return render_template('register.html')

@app.route('/genre', methods=['GET'])
def getgenre():
    genres = getgenres()
    return render_template('dispCat_all.html',genres=genres)

@app.route('/genre', methods=['POST'])
def addgenres():
    addgenre()
    flash('Genre successfully added!')
    return redirect('/genre')

@app.route('/genre/<gid>')
def deletegenres(gid):
    deletegenre(gid)
    flash('Genre successfully deleted.')
    return redirect('/genre')

@app.route('/genre/addbook/<gid>')
def addbooktogenre(gid):
    addbookgenre(gid)
    flash('Genre successfully added!')
    return redirect('/genre/addbook/' + gid)

@app.route('/users', methods=['POST'])
def register():
    adduser()
    flash('New user successfully added!')
    return render_template('register.html')

@app.route('/users/viewlist', methods=['GET'])
def userslist():
    rows = getusers()
    print rows
    return jsonify(rows)

@app.route('/users/list', methods=['GET'])
def listuser():
    userslist()
    return render_template('userList.html')

@app.route('/users/<username>', methods=['GET'])
def getspecificuser(username):
    users = searchusers(username)
    return render_template('users.html', users=users, username=username)