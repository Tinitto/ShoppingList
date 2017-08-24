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
    shoppinglist = shopping.ShoppingList.query.get(list_id)
    if not shoppinglist:
        raise KeyError('The shopping list does not exist')
    return shoppinglist


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
