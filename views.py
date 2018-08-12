from flask import render_template
from controllers import *
from flask import jsonify
from app import app

@app.route('/',methods=['POST','GET'])
def login():
    return render_template("login.html")

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/getbook',methods=['GET'])
def getbooks():
    booklist = (getbook())
    print((booklist))
    return render_template('hello/getbook.html',book=booklist)

@app.route('/test')
def testlink():
    return render_template('hello/test.html')

@app.route('/userlist',methods=['GET'])
def userslist():
    rows = getusers()
    return render_template("hello/list.html",rows=rows)