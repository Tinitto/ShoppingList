"""
This file tests the functionality of the \
helper functions in the app/crud folder
"""

import unittest
from flask import current_app, g
from app.app import app
from app.crud import user as crud_user
from app.classes import shopping

class UserCrudTests(unittest.TestCase):
    """
    Has tests for all helper functions for 
    a user found inapp/crud
    """
    def setUp(self):
        self.user_data = {'name': 'John Doe',
                          'username': 'johndoe',
                          'password': 'password123',
                          'email': 'john@example.com'}
        self.user = shopping.User(**self.user_data)

    def test_add_user_to_g(self):
        """
        checks if user is added to g
        """
        with app.app_context():
            another_user_with_same_username = shopping.User(**self.user_data)
            crud_user.add_user_to_g(self.user)
            self.assertIn(self.user, g.users.values())
            self.assertRaises(TypeError, crud_user.add_user_to_g,
             2)
            self.assertRaises(KeyError, crud_user.add_user_to_g,
                        another_user_with_same_username)

    def test_user_can_be_got(self):
        """
        checks if a user can be got by username form g
        """
        with app.app_context():
            if not hasattr(g, 'users'):
                g.users = {self.user.username: self.user}
            else:
                g.users[self.user.username] = self.user
            self.assertEqual(crud_user.get_user_from_g(self.user.username),
                            self.user)
            self.assertRaises(TypeError, crud_user.get_user_from_g,
                    23)

    def test_create_new_user(self):
        """
        checks if a user can be created from a dictionary
        of user information
        """
        with app.app_context():
            created_user = crud_user.create_new_user(self.user_data)
            self.assertIn(created_user, g.users.values())
            self.assertRaises(ValueError, crud_user.create_new_user,
                             {'hi':'hey'})

    def test_get_all_users_from_g(self):
        """
        checks if all users in g can be retrieved
        """
        with app.app_context():
            g.users = {self.user.username: self.user}
            
            users = {self.user.username: self.user}
            new_user_data = self.user_data
            for value in range(25):
                new_user_data['username'] = str(value)
                new_user = shopping.User(**new_user_data)
                g.users[new_user.username] = new_user
                users[new_user.username] = new_user

            self.assertEqual(users, crud_user.get_all_users_from_g())

    def test_delete_user_from_g(self):
        """
        delete_user_from_g should remove the user from 
        g.users
        """
        with app.app_context():
            g.users = {self.user.username: self.user}
            self.assertIn(self.user, g.users.values())
            self.assertRaises(KeyError, crud_user.delete_user_from_g,
                              self.user.username+'noone')   
            crud_user.delete_user_from_g(self.user.username)
            self.assertNotIn(self.user, g.users.values())
            # g.users is empty
            self.assertRaises(AttributeError, crud_user.delete_user_from_g,
                              self.user.username) 
               
            
            
