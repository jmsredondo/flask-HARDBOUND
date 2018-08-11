from flask import Flask
from flask import render_template
from controllers import getbook
from flask import g,jsonify
app = Flask(__name__)

DATABASE = 'test.db'
@app.route('/get_book')
#database connection
def get_book():
    return getbook()

book = {'book_name':'Harry Potter'}

@app.route('/')
def hello_world():
    return render_template('hello/index.html')

@app.route('/getbook')
def getbooks():
    return get_book()

@app.route('/test')
def testlink():
    return render_template('hello/test.html')


if __name__ == '__main__':
    app.run()
