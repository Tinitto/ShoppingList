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
    def setUp(self):
        """
        Initialize the User object for all tests
        in this class to use
        """
        self.user = shopping.User('John Doe', 'john@example.com', 'password') 

    def test_user_create_shoppinglist(self):
        """
        A user should be able to create a shopping list
        which has its attribute of creator equal to that user
        """
        shopping_list = self.user.create_shopping_list('groceries')
        self.assertEqual(self.user, shopping_list.creator)

    def test_user_delete_own_list(self):
        """
        A user can only delete his/her own shoppinglist
        and it should cease to exist

        the shopping list  must be an instance of ShoppinList class
        """
        user2 = shopping.User('Tom Doe', 'tom@example.com', 'password')
        user_2_shopping_list = user2.create_shopping_list('hoilday shopping')
        user_shopping_list = self.user.create_shopping_list('groceries')
        third_shopping_list = 3
        self.assertRaises(PermissionError, self.user.delete_shopping_list,
                         user_2_shopping_list)
        self.assertIsNone(self.user.delete_shopping_list(user_shopping_list))
        self.assertRaises(TypeError, self.user.delete_shopping_list,
                         third_shopping_list)
    
    def test_user_name_is_string(self):
        """
        A user's name can only be a string
        """
        self.assertRaises(TypeError, shopping.User, 5, 
                        'john@example.com', 'password')
        self.assertRaises(TypeError, self.user.set_name, 5)

    def test_user_email_format(self):
        """
        An email should have only one @ and . and is a string
        """
        self.assertRaises(ValueError, shopping.User, 'John Doe',
            'johnexample.com', 'password')
        self.assertRaises(ValueError, shopping.User, 'John Doe',
            'john@examplecom', 'password')
        self.assertRaises(TypeError, shopping.User, 'John Doe',
            6, 'password')
        self.assertRaises(ValueError, self.user.set_email,
            'johnexample.com')

 
    def test_user_password_length(self):
        """
        A user's password should be at least 6 characters long
        and is a string
        """
        self.assertRaises(ValueError, shopping.User, 'John Doe',
            'john@example.com', 'pas')
        self.assertRaises(TypeError, shopping.User, 'John Doe',
            'john@example.com', 5)
        self.assertRaises(ValueError, self.user.set_password,
            'pas')
        self.assertRaises(TypeError, self.user.set_password,
            5)
        
 

class ShoppingListTests(unittest.TestCase):
    """
    Tests for class ShoppingList
    """
    def setUp(self):
        """
        initialize the ShoppingList object for all tests
        in this class to use
        """
        self.shopping_list = shopping.ShoppingList('Groceries',
         'family daily grocery shopping list')

    # an item can be added to Shopping list
    # an item can be deleted from a shopping list
    # a shopping list's name can only be a string
    # a shopping list's description can only be a string
    # the creator of a shopping list is a User



class ShoppingItemTests(unittest.TestCase):
    """
    Tests for class ShoppingItem
    """
    def setUp(self):
        """
        initialize the ShoppingItem object for all tests
        in this class to use
        """
        self.shopping_item = shopping.ShoppingItem('fruit', 5, 'units')

    # an item's quantity can be increased
    # an item's quantity can only be a number
    # an item's name can only be a string
    # an item's unit can only be a string
    # the item belongs to a shopping list


if __name__ == '__main__':
    unittest.main()
