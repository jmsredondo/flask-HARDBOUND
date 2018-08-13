#create application
from flask import Flask
from config import Config

app = Flask(__name__)
app.debug = True
app.config.from_object(Config)
#import views from app directory
from app import views