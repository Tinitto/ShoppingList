"""
This file contains the following functionality
- create, read, update and delete shopping list
"""

from flask import session
from app.classes import shopping, utilities


def get_shopping_list(list_id):
    """
    Try to get the shoppinglist object
    """
    if not utilities.check_type(list_id, int):
        raise ValueError('Id should be an integer')
    shopping_list = shopping.ShoppingList.query.get(list_id)
    if not shopping_list:
        raise KeyError('The shopping list does not exist')
    return shopping_list

def get_shopping_item(item_id):
    """
    Try to get the ShoppingItem object
    """
    if not utilities.check_type(item_id, int):
        raise ValueError('Id should be an integer')
    shopping_item = shopping.ShoppingItem.query.get(item_id)
    if not shopping_item:
        raise KeyError('The shopping list item does not exist')
    return shopping_item


def add_item_with_details(shopping_list, name='', quantity=0,
                            unit=''):
    """
    Adds a new item to the shopping list
    """
    if not utilities.check_type(shopping_list, shopping.ShoppingList):
        raise ValueError('The item should be added to a shopping list object')
    try:
        item = shopping.ShoppingItem(name=str(name), quantity=float(quantity), unit=str(unit),
                        parent_list=shopping_list)
        item.save()
    except ValueError:
        raise ValueError('Invalid arguments')
