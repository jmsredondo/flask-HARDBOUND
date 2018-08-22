from flask import render_template, g
from flask import flash
from controllers import *
from flask import redirect,url_for
#import app from class Flask from app directory
from app import app

#route to index
@app.route('/')
@app.route('/user/login',methods=['POST','GET'])
def login():
    if g.user is None:
        #print "token: "+ session['token']
        return render_template("login.html")
    else:
        if session['usertype'] is not None:
            current_user = session['token']
            print "token: a  "+ session['token']
            return render_template('dashboard.html',current_user=current_user)
        else:
            return render_template("login.html")

@app.route('/admin',methods=['POST','GET'])
def adminlogin():
    if g.user is None:
        #print "token: "+ session['token']
        return render_template("login2.html")
    else:
        if session['usertype'] is not None:
            current_user = session['token']
            print "token: a  "+ session['token']
            return render_template('dashboard.html',current_user=current_user)
        else:
            return render_template("login2.html")

@app.route('/dashboard', methods=['POST','GET'])
def dashboard():
    if g.user is not None and session['usertype'] is not None:
        current_user = session['token']
        usertype = session['usertype']
        #print "token b : "+ session['token']
        return render_template('dashboard.html',current_user=current_user,usertype=usertype)
    else:
        rows = getlogin()
        if rows is not None and session['usertype'] is not None:
            current_user = session['token']
            usertype = session['usertype']
            #print "token b : "+ session['token']
            return render_template('dashboard.html',current_user=current_user,usertype=usertype)
        else:
            return redirect('/geterrorlogin')

@app.before_request
def before_request():
    g.user = None
    if 'token' in session:
        g.user = session['token']


#getbooktemp and getbook methods used for rendering
#generating json response
@app.route('/books')
def getbooktemp():
    return render_template("bookList.html")

@app.route('/bookbyid')
def getbookbyidtem():
    return render_template("getBook.html")

@app.route('/book',methods=['GET'])
def getbooks():
    #current_user = session['token']
    books = getbook()
   # genres = getgenres()
    return jsonify(books), 200

@app.route('/book/<bid>', methods=['GET'])
def getabooks(bid):
    books = getabook(bid)
    return jsonify(books), 200

@app.route('/book', methods=['POST'])
def addbooks():
    flash('New book successfully added!')
    books = getbook()
    genres = getgenres()
    return jsonify(addbook()), 201

@app.route('/book/<bid>')
def deletebooks(bid):
    deletebook(bid)
    flash('Book successfully deleted.')
    return redirect('/books'), 200

@app.route('/users/list', methods=['GET'])
def listuser():
    return render_template('userList.html'), 200

@app.route('/user')
def userbyusernametemp():
    return render_template('getUser.html'), 200

@app.route('/users', methods=['GET'])
def userslist():
    rows = getusers()
    print rows
    return jsonify(rows)

@app.route('/register', methods=['GET'])
def getregister():
    return render_template('register.html'), 200

@app.route('/users', methods=['POST'])
def register():
    flash('New user successfully added!')
    return jsonify(adduser()), 201

#get list of genres
@app.route('/genres', methods=['GET'])
def getgenretemp():
    return render_template('dispCat_all.html'), 200

@app.route('/genrebyid')
def getgenreidtemp():
    return render_template('getGenre.html'), 200

@app.route('/genre', methods=['GET'])
def getgenre():
    genres = getgenres()
    return jsonify(genres), 200

@app.route('/genre/<gid>', methods=['GET'])
def getagenre(gid):
    genres = getagenres(gid)
    return jsonify(genres), 200

@app.route('/genre', methods=['POST'])
def addgenres():
    flash('Genre successfully added!')
    return jsonify(addgenre()), 201

@app.route('/genre/<gid>')
def deletegenres(gid):
    deletegenre(gid)
    flash('Genre successfully deleted.')
    return redirect('/genre'), 200

@app.route('/genre/addbook/<gid>', methods=['GET'])
def getbooktogenre(gid):
    books = getunassignedbook(gid)
    return render_template('bookList2.html',books=books, gid=gid), 200

@app.route('/genre/addbook/<gid>', methods=['POST'])
def addbooktogenre(gid):
    addbookgenre(gid)
    flash('Genre successfully assigned to book!')
    return redirect('/genre/addbook/' + gid), 200

@app.route('/library', methods=['GET'])
def getlibrary():
    username = 'arvincea'
    books = getuserbook(username)
    return render_template('library.html', books=books), 200

@app.route('/library', methods=['POST'])
def addlibraries():
    addlibrary()
    flash('Added book to library!')
    return redirect('/library'), 201

@app.route('/rate', methods=['POST'])
def addratings():
    addrating()
    flash('Added rating!')
    return redirect('/book'), 201

@app.route('/rate/<bid>', methods=['GET'])
def getratings(bid):
    ratings = getrating(bid)
    return render_template('getRating.html', ratings=ratings), 200

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('token', None)
   return redirect(url_for('login')), 200


#Error Handling

@app.route('/geterrorlogin',methods=['GET'])
def geterrorlogin():
    errorlogin = []
    print 'error 1'
    error = {
        'description': 'Invalid username/password supplied'
    }
    errorlogin.append(error)
    return jsonify(errorlogin), 400
    #return redirect('/errorlogin')

#Error Handling

@app.route('/errorlogin')
def errorlogin():
    return render_template("login.html")

@app.route('/getaddgenereerror1',methods=['GET'])
def getaddgenereerror1():
    errorinput = []
    #print 'error 2'
    error = {
        'description': 'Invalid input'
    }
    errorinput.append(error)
    return jsonify(errorinput), 400

@app.route('/getaddgenereerror2',methods=['GET'])
def getaddgenereerror2():
    errorinput = []
    print 'error 3'
    error = {
        "message": "Authentication information is missing or invalid"
    }
    errorinput.append(error)
    return jsonify(errorinput), 401

@app.route('/getaddbookerror1',methods=['GET'])
def getaddbookerror1():
    errorinput = []
    #print 'error 2'
    error = {
        'description': 'Invalid input'
    }
    errorinput.append(error)
    return jsonify(errorinput), 400

@app.route('/getaddbookerror2',methods=['GET'])
def getaddbookerror2():
    errorinput = []
    #print 'error 3'
    error = {
        "message": "Authentication information is missing or invalid"
    }
    errorinput.append(error)
    return jsonify(errorinput), 401

@app.route('/getaddusererror1',methods=['GET'])
def getaddusererror1():
    errorinput = []
    #print 'error 2'
    error = {
        'description': 'Invalid input'
    }
    errorinput.append(error)
    return jsonify(errorinput), 400

@app.route('/getaddliberror1',methods=['GET'])
def getaddliberror1():
    errorinput = []
    #print 'error 2'
    error = {
        'description': 'Invalid input'
    }
    errorinput.append(error)
    return jsonify(errorinput), 400

@app.route('/getaddliberror2',methods=['GET'])
def getaddliberror2():
    errorinput = []
    #print 'error 3'
    error = {
        "message": "Authentication information is missing or invalid"
    }
    errorinput.append(error)
    return jsonify(errorinput), 401

@app.route('/getaddrateerror1',methods=['GET'])
def getaddrateerror1():
    errorinput = []
    #print 'error 2'
    error = {
        'description': 'Invalid input'
    }
    errorinput.append(error)
    return jsonify(errorinput), 400

@app.route('/getaddrateerror2',methods=['GET'])
def getaddrateerror2():
    errorinput = []
    #print 'error 3'
    error = {
        "message": "Authentication information is missing or invalid"
    }
    errorinput.append(error)
    return jsonify(errorinput), 401
