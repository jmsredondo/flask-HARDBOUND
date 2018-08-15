from flask import render_template
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
    booklist = getbook()
    print((booklist))
    return render_template('bookList.html',book=booklist)


@app.route('/users', methods=['GET'])
def getregister():
    return render_template('register.html')

@app.route('/genre', methods=['GET'])
def getgenre():
    genres = get_genres()
    return render_template('dispCat_all.html',genres=genres)

@app.route('/users', methods=['POST'])
def register():
    adduser()
    return render_template('register.html')

@app.route('/users/list',methods=['GET'])
def userslist():
    rows = getusers()
    return jsonify(rows)

@app.route('/users/viewlist',methods=['GET'])
def listuser():
    userslist()
    return render_template('userList.html')