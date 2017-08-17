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
from nose.plugins.attrib import attr


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
        A user should be able to create a shopping list and add it to the
        his/her list of shopping lists
        """
        shopping_list = self.user.create_shopping_list('groceries')
        self.assertIn(shopping_list, self.user.shopping_lists)

    def test_user_delete_shopping_list(self):
        """
        A user can delete his/her own shoppinglist
        and it should cease to exist
        It should exist in his/her lists before it is deleted

        the shopping list  must be an instance of ShoppingList class
        """
        user2 = shopping.User('Tom Doe', 'tom@example.com', 'password')
        user_2_shopping_list = user2.create_shopping_list('hoilday shopping')
        user_shopping_list = self.user.create_shopping_list('groceries')
        third_shopping_list = 3
        self.assertRaises(KeyError, self.user.delete_shopping_list,
                         user_2_shopping_list)
        self.user.delete_shopping_list(user_shopping_list)
        self.assertNotIn(user_shopping_list, self.user.shopping_lists)
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
    # check that each set method actually sets the attributes
    def test_set_name(self):
        """
        the set_name method should set the name of the user
        """
        new_name = 'Tori Doe'
        self.user.set_name(new_name)
        self.assertEqual(new_name, self.user.name)

    def test_set_email(self):
        """
        the set_email method should set the email of the user
        """
        new_email = 'tori@example.com'
        self.user.set_email(new_email)
        self.assertEqual(new_email, self.user.email)

    def test_set_password(self):
        """
        the set_password method should set the password of the user
        """
        new_password = 'password123'
        self.user.set_password(new_password)
        self.assertEqual(new_password, self.user.password)
        
 

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

    def test_item_can_be_added(self):
        """
        An item can be added to the shopping list such that
        it becomes part of the list of items in the shopping list
        """
        item_added = self.shopping_list.add_item('mangoes')
        self.assertIn(item_added, self.shopping_list.items)

    def test_an_item_can_be_deleted(self):
        """
        Only the parent list can have the method to delete
        an item
        """

    def test_only_creator_can_edit_list(self):
        """
        only creator can set the title
        only creator can set the description
        only creator can add an item
        only creator can delete an item
        """
    
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

    # check that each set method actually sets the attributes


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

    def test_item_quantity_is_number(self):
        """
        An item quantity can only be a number of float or int type
        """
        self.assertRaises(TypeError, shopping.ShoppingItem, 
        'fruit', quantity='five')
        self.assertRaises(TypeError, self.shopping_item.set_quantity,
            {'quantity':'float or int is expected, not dict'})

    def test_item_name_is_string(self):
        """
        An item name can only be a string
        """
        self.assertRaises(TypeError, shopping.ShoppingItem, 
        5)
        self.assertRaises(TypeError, self.shopping_item.set_name,
            {'name':'string is expected, not dict'})
 
    def test_item_unit_is_string(self):
        """
        An item unit can only be a string
        """
        self.assertRaises(TypeError, shopping.ShoppingItem, 
        'fruit', unit=4)
        self.assertRaises(TypeError, self.shopping_item.set_unit,
            {'unit':'string is expected, not dict'})
    # the item belongs to a shopping list and not None

    # check that each set method actually sets the attributes
    def test_set_name(self):
        """
        the set_name method should set the name of the item
        """
        new_name = 'vegetables'
        self.shopping_item.set_name(new_name)
        self.assertEqual(new_name, self.shopping_item.name)

    def test_set_quantity(self):
        """
        the set_quantity method should set the quantity of the item
        """
        new_quantity = 40
        self.shopping_item.set_quantity(new_quantity)
        self.assertEqual(new_quantity, self.shopping_item.quantity)

    def test_set_unit(self):
        """
        the set_unit method should set the unit of the item
        """
        new_unit = 'kg'
        self.shopping_item.set_unit(new_unit)
        self.assertEqual(new_unit, self.shopping_item.unit)


class UtilitiesTests(unittest.TestCase):
    """
    Class to test the functionality of the functions
    in utilities.py
    """
    
    def test_check_type_return(self):
        """
        check_type returns True when the object is of any type in args
        check_type raises TypeError when the types are different
        check_type raises an error when the type_object is not a type        
        """
        self.assertTrue(utilities.check_type('girl', str))
        self.assertTrue(utilities.check_type('girl', float, int, str))
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
