from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('hello/index.html')
@app.route('/test')
def testlink():
    return render_template('hello/test.html')
if __name__ == '__main__':
    app.run()
