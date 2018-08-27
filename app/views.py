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
            current_user = 'test'
            print ("token: a  "+ session['token'])
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
            current_user = 'test'
            print ("token: a  "+ session['token'])
            return render_template('dashboard.html',current_user=current_user)
        else:
            return render_template("login2.html")

@app.route('/dashboard', methods=['POST','GET'])
def dashboard():
    if g.user is not None and session['usertype'] is not None:
        current_user = 'test'
        usertype = session['usertype']
        #print "token b : "+ session['token']
        return render_template('dashboard.html',current_user=current_user,usertype=usertype)
    else:
        rows = getlogin()
        if rows is not None and session['usertype'] is not None:
            current_user = 'test'
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
    current_user = 'test'
    return render_template("bookList.html",current_user=current_user)

@app.route('/bookbyid')
def getbookbyidtem():
    current_user = 'test'
    return render_template("getBook.html",current_user=current_user)

@app.route('/book',methods=['GET'])
def getbooks():
    #current_user = 'test'
    books = getbook()
   # genres = getgenres()
    return jsonify(books), 200

@app.route('/book/<bid>', methods=['GET'])
def getabooks(bid):
    ratings = getrating(bid)
    return jsonify(getabook(bid)), 200

@app.route('/book', methods=['POST'])
def addbooks():
    result = addbook()
    if result == 'error1':
        return redirect('/getaddbookerror1'),400
    elif result == 'error2':
        return redirect('/getaddbookerror2'),401
    else:
        flash('New book successfully added!')
        books = getbook()
        genres = getgenres()
        return jsonify(result), 201

@app.route('/book/<bid>', methods=['POST'])
def deletebooks(bid):
    flash('Book successfully deleted.')
    return jsonify(deletebook(bid)), 200

@app.route('/users/list', methods=['GET'])
def listuser():
    current_user = 'test'
    return render_template('userList.html',current_user=current_user), 200

@app.route('/user')
def userbyusernametemp():
    current_user = 'test'
    return render_template('getUser.html',current_user=current_user), 200

@app.route('/users', methods=['GET'])
def userslist():
    rows = getusers()
    return jsonify(rows)

@app.route('/users/<uid>',methods=['GET'])
def getausers(uid):
    users = getauser(uid)
    return jsonify(users),200

@app.route('/register', methods=['GET'])
def getregister():
        current_user = 'test'
        return render_template('register.html',current_user=current_user), 200


@app.route('/users', methods=['POST'])
def register():
    if adduser() == 'error1':
        return redirect('/getaddusererror1'),400
    else:
        flash('New user successfully added!')
        return jsonify(adduser()), 201

#get list of genres
@app.route('/genres', methods=['GET'])
def getgenretemp():
    current_user = 'test'
    return render_template('dispCat_all.html',current_user=current_user), 200

@app.route('/genrebyid')
def getgenreidtemp():
    current_user = 'test'
    return render_template('getGenre.html',current_user=current_user), 200

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
    result = addgenre()
    if result == 'error1':
        return redirect('/getaddgenereerror1'),400
    elif result == 'error2':
        return redirect('/getaddgenereerror2'),401
    else:
        flash('Genre successfully added!')
        return jsonify(result), 201

@app.route('/genre/<gid>', methods=['POST'])
def deletegenres(gid):
    flash('Genre successfully deleted.')
    return jsonify(deletegenre(gid)), 200

@app.route('/genre/addbookstogenre')
def getbookstoadd():
    current_user = 'test'
    return render_template("bookList2.html",current_user=current_user)

@app.route('/genre/getaddbook/<gid>', methods=['GET'])
def getbooktogenre(gid):
    books = getunassignedbook(gid)
    return jsonify(books), 200

@app.route('/genre/addbook/<gid>', methods=['POST'])
def addbooktogenre(gid):
    flash('Genre successfully assigned to book!')
    return jsonify(addbookgenre(gid))

@app.route('/libraries', methods=['GET'])
def getlibraries():
    current_user = session['token']
    return render_template('library.html',current_user=current_user)

@app.route('/library', methods=['GET'])
def getlibrary():
    username = session['token']
    books = getuserbook(username)
    return jsonify(books), 200

@app.route('/library', methods=['POST'])
def addlibraries():

    if addlibrary() == 'error1':
        return redirect('/getaddlibeerror1'),400
    elif addlibrary() == 'error2':
        return redirect('/getaddlibeerror2'),401
    else:

        addlibrary()
        flash('Book successfully added to your library!')
        return redirect('/library'), 201

@app.route('/rate', methods=['POST'])
def addratings():

    if addrating() == 'error1':
        return redirect('/getaddrateeerror1'),400
    elif addrating() == 'error2':
        return redirect('/getaddrateerror2'),401
    else:

        flash('Added rating!')
        return jsonify(addrating()), 201

@app.route('/rate/<bid>', methods=['GET'])
def getratings(bid):
    ratings = getrating(bid)
    print(ratings)
    return jsonify(ratings)

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('token', None)
   return render_template('login.html'), 200


#Error Handling

@app.route('/geterrorlogin',methods=['GET'])
def geterrorlogin():
    errorlogin = []
    print ('error 1')
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
