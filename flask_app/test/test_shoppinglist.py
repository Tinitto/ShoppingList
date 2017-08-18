"""
Test file for the ShoppingList App.
The tests for the following classes are
included:
 - ShoppingList
"""

import unittest
from app.classes import shopping
from app.classes import utilities
from nose.plugins.attrib import attr


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
        An item delete should only be deleted if it exists
        in the list of items of the shopping list

        The item should cease to exist in that list
        """
        another_shopping_list = shopping.ShoppingList('Clothes',
         'for the children')
        item_in_another_list = another_shopping_list.add_item('shirt')
        item_in_list = self.shopping_list.add_item('shirt')
        item_in_wrong_type = 8
        self.shopping_list.delete_item(item_in_list)
        self.assertRaises(KeyError, 
                self.shopping_list.delete_item, item_in_another_list)
        self.assertRaises(TypeError, 
                self.shopping_list.delete_item, item_in_wrong_type)
        self.assertNotIn(item_in_list, self.shopping_list.items)
    
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

    def test_set_title(self):
        """
        The set_title method should set the title of
        the shopping list
        """
        new_title = "party items"
        self.shopping_list.set_title(new_title)
        self.assertEqual(new_title, self.shopping_list.title)

    def test_set_description(self):
        """
        The set_description method should set the description of
        the shopping list
        """
        new_description = "For Paul's birthday party"
        self.shopping_list.set_description(new_description)
        self.assertEqual(new_description,
                 self.shopping_list.description)




if __name__ == '__main__':
    unittest.main()
