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
    if 'token' in session:
        print "token: a  "+ session['token']
        return render_template("dashboard.html")
    else:
        #print "token: "+ session['token']
        return render_template("login.html")

@app.route('/dashboard', methods=['POST','GET'])
def dashboard():
    rows = getlogin()
    if rows is not None or 'token' in session:
        print "token b : "+ session['token']
        return render_template('dashboard.html')
    else:
        return redirect('/')

#getbooktemp and getbook methods used for rendering
#generating json response
@app.route('/books')
def getbooktemp():
    return render_template("bookList.html")

@app.route('/book',methods=['GET'])
def getbooks():
    current_user = session['token']
    books = getbook()
   # genres = getgenres()
    return jsonify(books)

@app.route('/book/<bid>', methods=['GET'])
def getabooks(bid):
    books = getabook(bid)
    return render_template('getBook.html', books=books)

@app.route('/book', methods=['POST'])
def addbooks():
    addbook()
    flash('New book successfully added!')
    books = getbook()
    genres = getgenres()
    return render_template('bookList.html',books=books, genres=genres)

@app.route('/book/<bid>')
def deletebooks(bid):
    deletebook(bid)
    flash('Book successfully deleted.')
    return redirect('/books')

@app.route('/users', methods=['GET'])
def getregister():
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

@app.route('/users/<uid>', methods=['GET'])
def getausers(uid):
    users = getauser(uid)
    return render_template('getUser.html', users=users)

@app.route('/users', methods=['POST'])
def register():
    adduser()
    flash('New user successfully added!')
    return render_template('register.html')

@app.route('/genre', methods=['GET'])
def getgenre():
    genres = getgenres()
    return render_template('dispCat_all.html',genres=genres)

@app.route('/genre/<gid>', methods=['GET'])
def getagenre(gid):
    genres = getagenres(gid)
    return render_template('getGenre.html', genres=genres)

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

@app.route('/genre/addbook/<gid>', methods=['GET'])
def getbooktogenre(gid):
    books = getunassignedbook(gid)
    return render_template('bookList2.html',books=books, gid=gid)

@app.route('/genre/addbook/<gid>', methods=['POST'])
def addbooktogenre(gid):
    addbookgenre(gid)
    flash('Genre successfully assigned to book!')
    return redirect('/genre/addbook/' + gid)

@app.route('/library', methods=['GET'])
def getlibrary():
    username = 'arvincea'
    books = getuserbook(username)
    return render_template('library.html', books=books)

@app.route('/library', methods=['POST'])
def addlibraries():
    addlibrary()
    flash('Added book to library!')
    return redirect('/library')

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('token', None)
   session.clear()
   return redirect(url_for('login'))
