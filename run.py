from flask import Flask
from flask import render_template
from flask import jsonify

import controllers
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello/index.html')
@app.route('/getbook')
def getbooks():
   return 'kk'

if __name__ == '__main__':
    app.run()