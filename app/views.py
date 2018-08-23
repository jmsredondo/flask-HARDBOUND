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
    if g.user is not None and session['usertype'] is not None:
        username = session['token']
        return render_template("bookList.html", username=username)
    else:
        return render_template("login.html"), 400

@app.route('/bookbyid')
def getbookbyidtem():
    if g.user is not None and session['usertype'] is not None:
        current_user = session['token']
        return render_template("getBook.html", current_user=current_user)
    else:
        return render_template("login.html"), 400

@app.route('/book',methods=['GET'])
def getbooks():
    if g.user is not None and session['usertype'] is not None:
        #current_user = session['token']
        books = getbook()
       # genres = getgenres()
        return jsonify(books), 200
    else:
        return render_template("login.html"), 400

@app.route('/book/<bid>', methods=['GET'])
def getabooks(bid):
    if g.user is not None and session['usertype'] is not None:
        books = getabook(bid)
        return jsonify(books), 200
    else:
        return render_template("login.html"), 400

@app.route('/book', methods=['POST'])
def addbooks():
    if g.user is not None and session['usertype'] is not None:
        result = addbook()
        if result == 'error1':
            return redirect('/getaddbookerror1')
        elif result == 'error2':
            return redirect('/getaddbookerror2')
        else:
            flash('New book successfully added!')
            books = getbook()
            genres = getgenres()
            return jsonify(result), 201
    else:
        return render_template("login.html"), 400

@app.route('/book/<bid>')
def deletebooks(bid):
    if g.user is not None and session['usertype'] is not None:
        deletebook(bid)
        flash('Book successfully deleted.')
        return redirect('/books'), 200
    else:
        return render_template("login.html"), 400

@app.route('/users/list', methods=['GET'])
def listuser():
    if g.user is not None and session['usertype'] == True:
        current_user = session['token']
        return render_template('userList.html', current_user=current_user), 200
    else:
        return render_template("login.html"), 400

@app.route('/user')
def userbyusernametemp():
    if g.user is not None and session['usertype'] == True:
        current_user = session['token']
        return render_template('getUser.html', current_user=current_user), 200
    else:
        return render_template("login.html")

@app.route('/users', methods=['GET'])
def userslist():
    if g.user is not None and session['usertype'] == True:
        rows = getusers()
        print rows
        return jsonify(rows)
    else:
        return render_template("login.html"), 400

@app.route('/users/<uid>',methods=['GET'])
def getausers(uid):
    if g.user is not None and session['usertype'] == True:
        users = getauser(uid)
        return jsonify(users),200
    else:
        return render_template("login.html"), 400

@app.route('/register', methods=['GET'])
def getregister():
    if g.user is not None and session['usertype'] == True:
        return render_template('register.html'), 200
    else:
        return render_template("login.html"), 400

@app.route('/users', methods=['POST'])
def register():
    if g.user is not None and session['usertype'] == True:
        if adduser() == 'error1':
            return redirect('/getaddusererror1')
        else:
            flash('New user successfully added!')
            return jsonify(adduser()), 201
    else:
        return render_template("login.html"), 400

#get list of genres
@app.route('/genres', methods=['GET'])
def getgenretemp():
    if g.user is not None and session['usertype'] is not None:
        current_user = session['token']
        return render_template('dispCat_all.html', current_user=current_user), 200
    else:
        return render_template("login.html"), 400

@app.route('/genrebyid')
def getgenreidtemp():
    if g.user is not None and session['usertype'] is not None:
        current_user = session['token']
        return render_template('getGenre.html', current_user=current_user), 200
    else:
        return render_template("login.html"), 400

@app.route('/genre', methods=['GET'])
def getgenre():
    if g.user is not None and session['usertype'] is not None:
        genres = getgenres()
        return jsonify(genres), 200
    else:
        return render_template("login.html"), 400

@app.route('/genre/<gid>', methods=['GET'])
def getagenre(gid):
    if g.user is not None and session['usertype'] is not None:
        genres = getagenres(gid)
        return jsonify(genres), 200
    else:
        return render_template("login.html"), 400

@app.route('/genre', methods=['POST'])
def addgenres():
    if g.user is not None and session['usertype'] is not None:
        result = addgenre()
        if result == 'error1':
            return redirect('/getaddgenereerror1')
        elif result == 'error2':
            return redirect('/getaddgenereerror2')
        else:
            flash('Genre successfully added!')
        return jsonify(result), 201
    else:
        return render_template("login.html"), 400

@app.route('/genre/<gid>')
def deletegenres(gid):
    if g.user is not None and session['usertype'] is not None:
        flash('Genre successfully deleted.')
        return deletegenre(gid), 200
    else:
        return render_template("login.html"), 400

@app.route('/genre/addbookstogenre')
def getbookstoadd():
    if g.user is not None and session['usertype'] is not None:
        current_user = session['token']
        return render_template("bookList2.html", current_user=current_user)
    else:
        return render_template("login.html"), 400

@app.route('/genre/getaddbook/<gid>', methods=['GET'])
def getbooktogenre(gid):
    if g.user is not None and session['usertype'] is not None:
        books = getunassignedbook(gid)
        return jsonify(books), 200
    else:
        return render_template("login.html"), 400

@app.route('/genre/addbook/<gid>', methods=['POST'])
def addbooktogenre(gid):
    if g.user is not None and session['usertype'] is not None:
        flash('Genre successfully assigned to book!')
        return jsonify(addbookgenre(gid))
    else:
        return render_template("login.html"), 400


@app.route('/libraries', methods=['GET'])
def getlibrarytemp():
    return render_template('library.html')

@app.route('/library', methods=['GET'])
def getlibrary():
    if g.user is not None and session['usertype'] is not None:
        username = session['token']
        current_user = session['token']
        books = getuserbook(username)
        return jsonify(books), 200
    else:
        return render_template("login.html"), 400


@app.route('/library', methods=['POST'])
def addlibraries():
    if g.user is not None and session['usertype'] is not None:

        """
    if addlibrary() == 'error1':
        return redirect('/getaddlibeerror1')
    elif addlibrary() == 'error2':
        return redirect('/getaddlibeerror2')
    else:
    """

        flash('Added book to library!')
        return jsonify(addlibrary()), 201
    else:
        return render_template("login.html"), 400

@app.route('/rate', methods=['POST'])
def addratings():
    if g.user is not None and session['usertype'] is not None:
        """
        if addrating() == 'error1':
            return redirect('/getaddrateeerror1')
        elif addrating() == 'error2':
            return redirect('/getaddrateerror2')
        else:
        """
        addrating()
        flash('Added rating!')
        return redirect('/book'), 201
    else:
        return render_template("login.html"), 400

@app.route('/rate/<bid>', methods=['GET'])
def getratings(bid):
    if g.user is not None and session['usertype'] is not None:
        ratings = getrating(bid)
        current_user = session['token']
        return render_template('getRating.html', ratings=ratings, current_user=current_user), 200
    else:
        return render_template("login.html"), 400

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
    return jsonify(errorlogin)
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
      "field": "genre",
      "reason": "Invalid input"
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
      "field": "author",
      "reason": "Invalid input"
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
      "field": "first name or last name",
      "reason": "Invalid input"
    }
    errorinput.append(error)
    return jsonify(errorinput), 400

@app.route('/getaddliberror1',methods=['GET'])
def getaddliberror1():
    errorinput = []
    #print 'error 2'
    error = {
      "field": "book",
      "reason": "Invalid input"
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
"""
@app.route('/getaddrateerror1',methods=['GET'])
def getaddrateerror1():
    errorinput = []
    #print 'error 2'
    error = {
      "field": "genre",
      "reason": "Invalid input"
    }
    errorinput.append(error)
    return jsonify(errorinput), 400
"""
@app.route('/getaddrateerror2',methods=['GET'])
def getaddrateerror2():
    errorinput = []
    #print 'error 3'
    error = {
        "message": "Authentication information is missing or invalid"
    }
    errorinput.append(error)
    return jsonify(errorinput), 401
