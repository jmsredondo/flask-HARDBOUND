# test_bucketlist.py
import unittest
import os
import json

import requests
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from config import app_config


class UserTestCase(unittest.TestCase):
    """This class represents the bucketlist test case"""
    app = Flask(__name__)
    api = Api(app)
    app.config.from_object(app_config['development'])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db = SQLAlchemy()
    db.init_app(app)

    def setUp(self):
        self.host = 'http://localhost:5000'
        self.samplegenre1 = {'type': 'Fiction', 'genre': 'Fantasy'}
        self.samplegenre2 = {'type': '', 'genre': ''}
        self.samplegenre3 = {'type': '1', 'genre': '1'}
        self.samplegenre4 = {'type': 'Non-Fiction', 'genre': 'Action'}
        self.samplegenre5 = {'type': '_!@#$%^&*()', 'genre': '!@#$%^&*()'}
        self.samplebook1 = {}

    def test_get_genre(self):
        res = res = requests.get(self.host + '/genre')
        self.assertEqual(res.status_code, 200)
            
    def test_add_genre1(self):
        res = requests.post(self.host+'/genre', data=self.samplegenre1)
        self.assertEqual(res.status_code, 201)
        res = res = requests.get(self.host + '/genre')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Fantasy', str(res.text))

    def test_add_genre2(self):
        res = requests.post(self.host+'/genre', data=self.samplegenre2)
        self.assertEqual(res.status_code, 201)

    def test_add_genre3(self):
        res = requests.post(self.host+'/genre', data=self.samplegenre3)
        self.assertEqual(res.status_code, 201)

    def test_add_genre4(self):
        res = requests.post(self.host+'/genre', data=self.samplegenre4)
        self.assertEqual(res.status_code, 201)
        res = res = requests.get(self.host + '/genre')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Fiction', str(res.text))

    def test_add_genre5(self):
        res = requests.post(self.host+'/genre', data=self.samplegenre5)
        self.assertEqual(res.status_code, 201)
        res = res = requests.get(self.host + '/genre')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Fiction', str(res.text))

    def test_add_book1(self):
        res = requests.post(self.host='/book', data=self.samplebook1)
        self.assertEqual(res.status_code, 201)

'''
    def test_api_get_genre_list(self):
        """Test get user list (GET request)."""
        res = res = requests.get(self.host+'/genre')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Action', str(res.text))

    def setUp(self):
        """Define test variables and initialize app."""
        self.host = 'http://localhost:5000'
        self.sampleuser1 = {'username': 'abesmith', 'firstname': 'Abe', 'lastname': 'Smith', 'email': 'abesmith@gmail.com',
                           'balance': '100', 'phonenumber': '09460292951', 'usertype':'False', 'password': 'N0virus01'
                           }
        self.sampleuser2 = {}
        self.sampleuser3 = {'username': 'bennycole'}
        self.sampleuser4 = {'username': 'xxxxxxxxxx', 'firstname': 'xxxxxxxxxx', 'lastname': 'xxxxxxxxxx', 'email': 'xxxxxxxxxx',
                           'balance': 'xxxxxxxxxx', 'phonenumber': 'xxxxxxxxxx', 'usertype':'xxxxxxxxxx', 'password': 'xxxxxxxxxx'}
        self.sampleuser5 = {'username': '', 'firstname': '', 'lastname': '', 'email': '',
                           'balance': '', 'phonenumber': '', 'usertype':'', 'password': ''}

        # # binds the app to the current context
        # with self.app.app_context():
        #     # create all tables
        #     db.create_all()

    def test_Register_User(self):
        """Test register user (POST request)"""
        res = requests.post(self.host+'/users', data=self.sampleuser1)
        self.assertEqual(res.status_code, 201)
        res = res = requests.get(self.host + '/users/list')
        self.assertEqual(res.status_code, 200)
        self.assertIn('abesmith', str(res.text))

    def test_api_Get_User_List(self):
        """Test get user list (GET request)."""
        res = res = requests.get(self.host+'/users/list')
        self.assertEqual(res.status_code, 200)
        self.assertIn('jsmith', str(res.text))
'''


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
