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
from app.classes import utilities


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

    # a user can delete/edit items that belong to shopping list he/she owns
        
 

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
    
    def test_title_is_string(self):
        """
        The title of the shopping list is 
        of type string (str) 
        """
        self.assertRaises(TypeError, shopping.ShoppingList, 
        5, 'A dummy description')
        self.assertRaises(TypeError, self.shopping_list.set_title,
            {'title':'string expected not dict'})
 
    def test_description_is_string(self):
        """
        The description of a shopping list is 
        of type string (str)
        """
        self.assertRaises(TypeError, shopping.ShoppingList, 
        'groceries', 55)
        self.assertRaises(TypeError, self.shopping_list.set_description,
            {'description':'string expected not dict'})

    def test_creator_is_right_type(self):
        """
        A creator of a shopping list should be
        an instance of the User class only (not even None)
        """



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


class UtilitiesTests(unittest.TestCase):
    """
    Class to test the functionality of the functions
    in utilities.py
    """
    
    def test_check_type_return(self):
        """
        check_type returns True when types are the same
        check_type raises TypeError when the types are different
        check_type raises an error when the type_object is not a type
        """
        self.assertTrue(utilities.check_type('girl', str))
        self.assertRaises(TypeError, utilities.check_type, 5, bool)
        self.assertRaises(ValueError, utilities.check_type, 5, 9)
    
    def test_check_email_format(self):
        """
        check_email_formart returns True when email is right format
        check_email_format raises a ValueError when email format is wrong
        check_email_format raises a TypeError when email is not string
        """
        self.assertTrue(utilities.check_email_format('tom@example.com'))
        self.assertRaises(ValueError, utilities.check_email_format,
                        'tomexample.com')
        self.assertRaises(TypeError, utilities.check_email_format,
                        56)

    def test_check_password_format(self):
        """
        check_password_format returns True for a String of more characters
        check_password_format raises a ValueError when password string
        is of length less than min_length (default 6)
        check_password_format raises a TypeError when password is not string
        check_password_format raises a TypeError when min_length is not an int
        """
        self.assertTrue(utilities.check_password_format('rango679kiy'))
        self.assertRaises(ValueError, utilities.check_password_format, 'present',
                        10)
        self.assertRaises(TypeError, utilities.check_password_format, 43.5)
        self.assertRaises(TypeError, utilities.check_password_format, 'password',
                        '34r')



if __name__ == '__main__':
    unittest.main()
