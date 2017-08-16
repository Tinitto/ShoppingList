"""
Test file for the ShoppingList App.
The tests for the following classes are
included:
 - User
 - ShoppingList
 - ShoppingItem
"""

import unittest
from app.classes import shopping


class UserTests(unittest.TestCase):
    """
    Tests for class User
    """
    def setup(self):
        """
        Initialize the User object for all tests
        in this class to use
        """
        self.user = shopping.User() 
 

class ShoppingListTests(unittest.TestCase):
    """
    Tests for class ShoppingList
    """
    def setup(self):
        """
        initialize the ShoppingList object for all tests
        in this class to use
        """
        self.shopping_list = shopping.ShoppingList() 


class ShoppingItemTests(unittest.TestCase):
    """
    Tests for class ShoppingItem
    """
    def setUp(self):
        """
        initialize the ShoppingItem object for all tests
        in this class to use
        """
        self.shopping_item = shopping.ShoppingItem()

