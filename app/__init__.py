#create application
#from flask import Flask
#from config import Config

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.debug = True
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

#import views from app directory
from app import views
from app import models