from app import app
import unittest

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
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
        self.login = {'username: arvincea', 'password: arvincea'}

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_get_genre_status(self):
        tester = app.test_client(self)
        response = tester.get('/genre', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_get_books_status(self):
        tester = app.test_client(self)
        response = tester.get('/book', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_get_users_status(self):
        tester = app.test_client(self)
        response = tester.get('/users', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_get_library_status(self):
        tester = app.test_client(self)
        response = tester.get('/library', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_get_logout_status(self):
        tester = app.test_client(self)
        response = tester.get('/users/logout', content_type='html/text')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()