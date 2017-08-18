"""
Test file for the ShoppingList App.
The tests for the following classes are
included:
 - ShoppingItem
"""

import unittest
from app.classes import shopping
from app.classes import utilities

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

if __name__ == '__main__':
    unittest.main()