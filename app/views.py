from flask import render_template, g
from flask import flash
from controllers import *
from flask import redirect,url_for
#import app from class Flask from app directory
from app import app

#route to index
@app.route('/')
@app.route('/index',methods=['POST','GET'])
def login():
    if g.user is None:
        #print "token: "+ session['token']
        return render_template("login.html")
    else:
        current_user = g.user
        print "token: a  "+ session['token']
        return render_template('dashboard.html',current_user=current_user)

@app.route('/dashboard', methods=['POST','GET'])
def dashboard():
    rows = getlogin()
    if rows is not None:
        current_user = session['token']
        usertype = session['usertype']
        #print "token b : "+ session['token']
        return render_template('dashboard.html',current_user=current_user,usertype=usertype)
    else:
        return redirect('/')

@app.before_request
def before_request():
    g.user = None
    if 'token' in session:
        g.user = session['token']

#getbooktemp and getbook methods used for rendering
#generating json response
@app.route('/books')
def getbooktemp():
    if g.user is None:
        return render_template("bookList.html")

@app.route('/bookbyid')
def getbookbyidtem():
    if g.user is None:
        return render_template("getBook.html")

@app.route('/book',methods=['GET'])
def getbooks():
    if g.user is None:
        current_user = session['token']
        books = getbook()
       # genres = getgenres()
        return jsonify(books)

@app.route('/book/<bid>', methods=['GET'])
def getabooks(bid):
    if g.user is None:
        books = getabook(bid)
        return jsonify(books)

@app.route('/book', methods=['POST'])
def addbooks():
    if g.user is None:
        addbook()
        flash('New book successfully added!')
        books = getbook()
        genres = getgenres()
        return render_template('bookList.html',books=books, genres=genres)

@app.route('/book/<bid>')
def deletebooks(bid):
    if g.user is None:
        deletebook(bid)
        flash('Book successfully deleted.')
        return redirect('/books')

@app.route('/users/list', methods=['GET'])
def listuser():
    if g.user is None:
        return render_template('userList.html')

@app.route('/user')
def userbyusernametemp():
    if g.user is None:
        return render_template('getUser.html')

@app.route('/users', methods=['GET'])
def userslist():
    if g.user is None:
        rows = getusers()
        print rows
        return jsonify(rows)

@app.route('/users/<uid>', methods=['GET'])
def getausers(uid):
    if g.user is None:
        users = getauser(uid)
        return jsonify(users)

@app.route('/users', methods=['GET'])
def getregister():
    if g.user is None:
        return render_template('register.html')

@app.route('/users', methods=['POST'])
def register():
    if g.user is None:
        adduser()
        flash('New user successfully added!')
        return render_template('register.html')

#get list of genres
@app.route('/genres', methods=['GET'])
def getgenretemp():
    if g.user is None:
        return render_template('dispCat_all.html')

@app.route('/genrebyid')
def getgenreidtemp():
    if g.user is None:
        return render_template('getGenre.html')

@app.route('/genre', methods=['GET'])
def getgenre():
    if g.user is None:
        genres = getgenres()
        return jsonify(genres)

@app.route('/genre/<gid>', methods=['GET'])
def getagenre(gid):
    if g.user is None:
        genres = getagenres(gid)
        return jsonify(genres)

@app.route('/genre', methods=['POST'])
def addgenres():
    if g.user is None:
        addgenre()
        flash('Genre successfully added!')
        return redirect('/genre')

@app.route('/genre/<gid>')
def deletegenres(gid):
    if g.user is None:
        deletegenre(gid)
        flash('Genre successfully deleted.')
        return redirect('/genre')

@app.route('/genre/addbook/<gid>', methods=['GET'])
def getbooktogenre(gid):
    if g.user is None:
        books = getunassignedbook(gid)
        return render_template('bookList2.html',books=books, gid=gid)

@app.route('/genre/addbook/<gid>', methods=['POST'])
def addbooktogenre(gid):
    if g.user is None:
        addbookgenre(gid)
        flash('Genre successfully assigned to book!')
        return redirect('/genre/addbook/' + gid)

@app.route('/library', methods=['GET'])
def getlibrary():
    if g.user is None:
        username = g.user
        books = getuserbook(username)
        return render_template('library.html', books=books)

@app.route('/library', methods=['POST'])
def addlibraries():
    if g.user is None:
        addlibrary()
        flash('Added book to library!')
        return redirect('/library')

@app.route('/rate', methods=['POST'])
def addratings():
    if g.user is None:
        addrating()
        flash('Added rating!')
        return redirect('/book')

@app.route('/rate/<bid>', methods=['GET'])
def getratings(bid):
    if g.user is None:
        ratings = getrating(bid)
        flash('Added rating!')
        return render_template('getRating.html', ratings=ratings)

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('token', None)
   session.clear()
   return redirect(url_for('login'))
