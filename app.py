from flask import Flask
'''
import sqlite3
conn = sqlite3.connect('database.db')
print "Open database successfully"
#conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
print "Table created successfully"
conn.close()
'''

app = Flask(__name__)

from views import *
if __name__ == '__main__':
    app.run()
