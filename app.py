#imports application instance
from app import app
from app import db


from app.models import User


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9300)