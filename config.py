<<<<<<< HEAD
import os
#basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'smilymarius'
   # SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    """ SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
=======
import os
#basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'smilymarius'
   # SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    """ SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
>>>>>>> bd398f8dce2507552bf3edcf5594a0c8efe20388
    SQLALCHEMY_TRACK_MODIFICATIONS = False"""