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
        self.host = 'http://0.0.0.0:9300'
        self.samplegenre1 = {'type': 'Fiction', 'genre': 'Fantasy'}
        self.samplegenre2 = {'type': '', 'genre': ''}
        self.samplegenre3 = {'type': '1', 'genre': '1'}
        self.samplegenre4 = {'type': 'Non-Fiction', 'genre': 'Action'}
        self.samplegenre5 = {'type': '_!@#$%^&*()', 'genre': '!@#$%^&*()'}
        self.samplegenre6 = {'type': "''", 'genre': "''"}
        self.samplebook1 = {'title': 'A Wonderful Life', 'description': 'An enchanted adventure', 'author': 'Jane Doe'}
        self.samplebook2 = {'title': '', 'description': '', 'author': ''}
        self.samplebook3 = {'title': '2', 'description': '2', 'author': '2'}
        self.samplebook4 = {'title': 'Harvest Moon', 'description': 'Farming book', 'author': 'Helen Keller'}
        self.samplebook5 = {'title': '_!@#$%^&*()', 'description': '_!@#$%^&*()', 'author': '_!@#$%^&*()'}
        self.samplebook6 = {'title': "''", 'description': "''", 'author': "''"}
        self.sampleuser1 = {'username:': 'jlaurelio', 'firstname': 'Jan Lorenz', 'lastname': 'Aurelio', 'email': 'jlaurelio@gmail.com', 'balance': '0', 'phonenumber': '09868293384'}
        self.sampleuser2 = {'username:': '', 'firstname': '', 'lastname': '', 'email': '', 'balance': '', 'phonenumber': ''}
        self.sampleuser3 = {'username:': '1', 'firstname': '1', 'lastname': '1', 'email': '1', 'balance': '100', 'phonenumber': '1'}
        self.sampleuser4 = {'username:': 'ejcarantes', 'firstname': 'Ethnica Jaya', 'lastname': 'Carantes', 'email': 'ejcarantes@gmail.com', 'balance': '0', 'phonenumber': '7120538'}
        self.sampleuser5 = {'username:': '_!@#$%^&*()', 'firstname': '_!@#$%^&*()', 'lastname': '_!@#$%^&*()', 'email': '_!@#$%^&*()', 'balance': '0', 'phonenumber': '_!@#$%^&*()'}
        self.sampleuser6 = {'username:': "''", 'firstname': "''", 'lastname': "''", 'email': "''", 'balance': '0', 'phonenumber': "''"}
        self.samplelibrary1 = {'user_id': '1', 'book_id': '1'}
        self.samplelibrary2 = {'user_id': '', 'book_id': ''}
        self.samplelibrary3 = {'user_id': 'Kanye West', 'book_id': 'A Wonderful Life'}
        self.samplerating1 = {'book_id': '2', 'user_id': '2', 'rating': '5', 'comment': 'Good book'}
        self.samplerating2 = {'book_id': '3', 'user_id': '2', 'rating': '1', 'comment': 'Bad book'}
        self.samplerating3 = {'book_id': '4', 'user_id': '2', 'rating': '1', 'comment': ''}
        self.samplerating4 = {'book_id': '5', 'user_id': '2', 'rating': '3', 'comment': '3'}
        self.samplerating5 = {'book_id': '6', 'user_id': '2', 'rating': '3', 'comment': '_!@#$%^&*()'}
        self.samplerating6 = {'book_id': "7", 'user_id': "2", 'rating': '3', 'comment': "''"}
        
    def test_get_genre_status(self):
        res = res = requests.get(self.host + '/genre')
        self.assertEqual(res.status_code, 200)
'''
    def test_get_books_status(self):
        res = res = requests.get(self.host + '/book')
        self.assertEqual(res.status_code, 200)

    def test_get_users_status(self):
        res = res = requests.get(self.host + '/users')
        self.assertEqual(res.status_code, 200)

    def test_get_library_status(self):
        res = res = requests.get(self.host + '/library')
        self.assertEqual(res.status_code, 200)

    def test_get_logout_status(self):
        res = res = requests.get(self.host + '/users/logout')
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
        self.assertIn('Non-Fiction', str(res.text))

    def test_add_genre5(self):
        res = requests.post(self.host+'/genre', data=self.samplegenre5)
        self.assertEqual(res.status_code, 201)
        res = res = requests.get(self.host + '/genre')
        self.assertEqual(res.status_code, 200)
        self.assertIn('_!@#$%^&*()', str(res.text))

    def test_add_genre6(self):
        res = requests.post(self.host+'/genre', data=self.samplegenre5)
        self.assertEqual(res.status_code, 201)

    def test_add_book1(self):
        res = requests.post(self.host+'/book', data=self.samplebook1)
        self.assertEqual(res.status_code, 201)
        res = res = requests.get(self.host + '/book')
        self.assertEqual(res.status_code, 200)
        self.assertIn('A Wonderful Life', str(res.text))

    def test_add_book2(self):
        res = requests.post(self.host+'/book', data=self.samplebook2)
        self.assertEqual(res.status_code, 201)

    def test_add_book3(self):
        res = requests.post(self.host+'/book', data=self.samplebook3)
        self.assertEqual(res.status_code, 201)
        res = res = requests.get(self.host + '/book')
        self.assertEqual(res.status_code, 200)
        self.assertIn('2', str(res.text))

    def test_add_book4(self):
        res = requests.post(self.host+'/book', data=self.samplebook4)
        self.assertEqual(res.status_code, 201)

    def test_add_book5(self):
        res = requests.post(self.host+'/book', data=self.samplebook5)
        self.assertEqual(res.status_code, 201)

    def test_add_book6(self):
        res = requests.post(self.host+'/book', data=self.samplebook5)
        self.assertEqual(res.status_code, 201)

    def test_add_user1(self):
        res = requests.post(self.host+'/users', data=self.sampleuser1)
        self.assertEqual(res.status_code, 201)
        res = res = requests.get(self.host + '/book')
        self.assertEqual(res.status_code, 200)
        self.assertIn('jlaurelio', str(res.text))

    def test_add_user2(self):
        res = requests.post(self.host+'/users', data=self.sampleuser1)
        self.assertEqual(res.status_code, 201)

    def test_add_user3(self):
        res = requests.post(self.host+'/users', data=self.sampleuser1)
        self.assertEqual(res.status_code, 201)

    def test_add_user4(self):
        res = requests.post(self.host+'/users', data=self.sampleuser1)
        self.assertEqual(res.status_code, 201)

    def test_add_user5(self):
        res = requests.post(self.host+'/users', data=self.sampleuser1)
        self.assertEqual(res.status_code, 201)

    def test_add_user6(self):
        res = requests.post(self.host+'/users', data=self.sampleuser1)
        self.assertEqual(res.status_code, 201)

    def test_add_library1(self):
        res = requests.post(self.host+'/library', data=self.samplelibrary1)
        self.assertEqual(res.status_code, 201)

    def test_add_library2(self):
        res = requests.post(self.host+'/library', data=self.samplelibrary2)
        self.assertEqual(res.status_code, 201)

    def test_add_library3(self):
        res = requests.post(self.host+'/library', data=self.samplelibrary3)
        self.assertEqual(res.status_code, 201)

    def test_get_books_id(self):
        res = res = requests.get(self.host + '/books/2')
        self.assertEqual(res.status_code, 200)
        res = res = requests.get(self.host + '/book')
        self.assertEqual(res.status_code, 200)
        self.assertIn('2', str(res.text))

    def test_get_genre_id(self):
        res = res = requests.get(self.host + '/genre/2')
        self.assertEqual(res.status_code, 200)
        res = res = requests.get(self.host + '/genre')
        self.assertEqual(res.status_code, 200)
        self.assertIn('2', str(res.text))

    def test_get_ratings1(self):
        res = requests.post(self.host+'/rate', data=self.samplerating1)
        self.assertEqual(res.status_code, 201)
        res = res = requests.get(self.host + '/rate/2')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Good book', str(res.text))

    def test_get_ratings2(self):
        res = requests.post(self.host+'/rate', data=self.samplerating2)
        self.assertEqual(res.status_code, 201)
        res = res = requests.get(self.host + '/rate/3')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Bad book', str(res.text))

    def test_get_ratings3(self):
        res = requests.post(self.host+'/rate', data=self.samplerating3)
        self.assertEqual(res.status_code, 201)
        res = res = requests.get(self.host + '/rate/4')
        self.assertEqual(res.status_code, 200)
        self.assertIn('', str(res.text))

    def test_get_ratings4(self):
        res = requests.post(self.host+'/rate', data=self.samplerating4)
        self.assertEqual(res.status_code, 201)
        res = res = requests.get(self.host + '/rate/5')
        self.assertEqual(res.status_code, 200)
        self.assertIn('3', str(res.text))

    def test_get_ratings5(self):
        res = requests.post(self.host+'/rate', data=self.samplerating5)
        self.assertEqual(res.status_code, 201)
        res = res = requests.get(self.host + '/rate/6')
        self.assertEqual(res.status_code, 200)
        self.assertIn('_!@#$%^&*()', str(res.text))

    def test_get_ratings6(self):
        res = requests.post(self.host+'/rate', data=self.samplerating6)
        self.assertEqual(res.status_code, 201)
        res = res = requests.get(self.host + '/rate/7')
        self.assertEqual(res.status_code, 200)
        self.assertIn("''", str(res.text))

    def test_api_get_genre_list(self):
        """Test get user list (GET request)."""
        res = res = requests.get(self.host+'/genre')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Action', str(res.text))
'''
'''
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