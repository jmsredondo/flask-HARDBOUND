#run this instead of app

from flask import Flask, request
from flask import render_template
import books
import category
import library
import rate
import users
import subprocess

import sqlite3
conn = sqlite3.connect('database.db')
print "Open database successfully"
#conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
print "Table created successfully"
conn.close()


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('hello/login.html')

@app.route('/test')
def testlink():
    return render_template('hello/test.html')

@app.route('/addrec',methods=['POST','GET'])
def run_add_users():
    users.do_addrec()

@app.route('/users')
def run_users():
    users.do_list()

if __name__ == '__main__':
    app.run()