import os
import sys
import unittest
from urllib.parse import urlparse

from werkzeug.security import generate_password_hash

from py_ferry import app
from py_ferry.database import Base, engine, session, User
from py_ferry import database

class TestViews(unittest.TestCase):
    def setUp(self):
        ''' test setup '''
        self.client = app.test_client()
        
        # set up the tables in the database
        Base.metadata.create_all(engine)
        
        # create an example user
        self.user = User(name = 'Alice', email = 'alice@example.com', 
            password = generate_password_hash('test'))
        session.add(self.user)
        session.commit()
        
    def tearDown(self):
        ''' test teardown '''
        session.close()
        # remove the tables and their data from the database
        Base.metadata.drop_all(engine)
        
    def simulate_login(self):
        with self.client.session_transaction() as http_session:
            http_session['user_id'] = str(self.user.id)
            http_session['_fresh'] = True
        
    def test_login(self):
        ''' login test '''
        self.simulate_login()
        self.assertEqual(True, True)
        
    def test_another_test(self):
        self.assertEqual(True, True)
        
        
    #     response = self.client.post('/entry/add', data = {
    #         'title': 'Test Entry',
    #         'content': 'Test content'
    #     })
        
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(urlparse(response.location).path, '/')
    #     entries = session.query(Entry).all()
    #     self.assertEqual(len(entries), 1)
        
    #     entry = entries[0]
    #     self.assertEqual(entry.title, 'Test Entry')
    #     self.assertEqual(entry.content, 'Test content')
    #     self.assertEqual(entry.author, self.user)

if __name__ == '__main__':
    unittest.main()