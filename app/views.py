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
        current_user = session['token']
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
    else:
        return redirect('/')

@app.route('/book',methods=['GET'])
def getbooks():
    if g.user is None:
        current_user = session['token']
        books = getbook()
       # genres = getgenres()
        return jsonify(books)
    else:
        return redirect('/')

@app.route('/book/<bid>', methods=['GET'])
def getabooks(bid):
    if g.user is None:
        books = getabook(bid)
        return render_template('getBook.html', books=books)
    else:
        return redirect('/')

@app.route('/book', methods=['POST'])
def addbooks():
    if g.user is None:
        addbook()
        flash('New book successfully added!')
        books = getbook()
        genres = getgenres()
        return render_template('bookList.html',books=books, genres=genres)
    else:
        return redirect('/')

@app.route('/book/<bid>')
def deletebooks(bid):
    if g.user is None:
        deletebook(bid)
        flash('Book successfully deleted.')
        return redirect('/books')
    else:
        return redirect('/')

@app.route('/users', methods=['GET'])
def getregister():
    if g.user is None:
        return render_template('register.html')
    else:
        return redirect('/')

@app.route('/users/viewlist', methods=['GET'])
def userslist():
    if g.user is None:
        rows = getusers()
        print rows
        return jsonify(rows)
    else:
        return redirect('/')

@app.route('/users/list', methods=['GET'])
def listuser():
    if g.user is None:
        userslist()
        return render_template('userList.html')
    else:
        return redirect('/')

@app.route('/users/<uid>', methods=['GET'])
def getausers(uid):
    if g.user is None:
        users = getauser(uid)
        return render_template('getUser.html', users=users)
    else:
        return redirect('/')

@app.route('/users', methods=['POST'])
def register():
    if g.user is None:
        adduser()
        flash('New user successfully added!')
        return render_template('register.html')
    else:
        return redirect('/')

@app.route('/genre', methods=['GET'])
def getgenre():
    if g.user is None:
        genres = getgenres()
        return render_template('dispCat_all.html',genres=genres)
    else:
        return redirect('/')

@app.route('/genre/<gid>', methods=['GET'])
def getagenre(gid):
    if g.user is None:
        genres = getagenres(gid)
        return render_template('getGenre.html', genres=genres)
    else:
        return redirect('/')

@app.route('/genre', methods=['POST'])
def addgenres():
    if g.user is None:
        addgenre()
        flash('Genre successfully added!')
        return redirect('/genre')
    else:
        return redirect('/')

@app.route('/genre/<gid>')
def deletegenres(gid):
    if g.user is None:
        deletegenre(gid)
        flash('Genre successfully deleted.')
        return redirect('/genre')
    else:
        return redirect('/')

@app.route('/genre/addbook/<gid>', methods=['GET'])
def getbooktogenre(gid):
    if g.user is None:
        books = getunassignedbook(gid)
        return render_template('bookList2.html',books=books, gid=gid)
    else:
        return redirect('/')

@app.route('/genre/addbook/<gid>', methods=['POST'])
def addbooktogenre(gid):
    if g.user is None:
        addbookgenre(gid)
        flash('Genre successfully assigned to book!')
        return redirect('/genre/addbook/' + gid)
    else:
        return redirect('/')

@app.route('/library', methods=['GET'])
def getlibrary():
    if g.user is None:
        username = session['token']
        books = getuserbook(username)
        return render_template('library.html', books=books)
    else:
        return redirect('/')

@app.route('/library', methods=['POST'])
def addlibraries():
    if g.user is None:
        addlibrary()
        flash('Added book to library!')
        return redirect('/library')
    else:
        return redirect('/')

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('token', None)
   return redirect(url_for('login'))
