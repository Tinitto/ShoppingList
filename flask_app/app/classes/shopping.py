"""
The module contains the following classes
 - User
 - ShoppingList
 - ShoppingItem
"""
from app.classes import utilities


class User(object):
    """
    A User is the owner of shopping lists
    """
    def __init__(self, name, email, password, username):
        if utilities.check_type(name, str,
            error_string="A user's name can only be a string"):
             self.name = name
        if utilities.check_email_format(email):
            self.email = email
        if utilities.check_password_format(password):
            self.password = password
        if utilities.check_type(username, str,
            error_string="A user's username can only be a string"):
             self.username = username
        self.shopping_lists = []

    def set_name(self, name):
        """
        Set the name of the user
        """
        if utilities.check_type(name, str,
             error_string="A user's name can only be a string"):
             self.name = name

    def set_username(self, username):
        """
        Set the username of the user
        """
        if ' ' in username:
            raise ValueError('Username should have no space')
        if utilities.check_type(username, str,
             error_string="A user's username can only be a string"):
             self.username = username
    
    def set_email(self, email):
        """
        Set the email of the User
        """
        if utilities.check_email_format(email):
            self.email = email

    def set_password(self, password):
        """
        Sets the password of the user
        """
        self.password = password
        if utilities.check_password_format(password):
            self.password = password

    def create_shopping_list(self, title):
        """
        Creates a ShoppingList object whose creator attribute
        points to this user object
        """
        shopping_list = ShoppingList(title)
        self.shopping_lists.append(shopping_list)
        return shopping_list

    def delete_shopping_list(self, shopping_list):
        """
        Allows user to delete a shopping
        list that they own
        """
        if not isinstance(shopping_list, ShoppingList):
            raise TypeError('Object is not a shopping list object')
        if shopping_list not in self.shopping_lists:
            raise KeyError('Shopping list does not exist')
        self.shopping_lists.remove(shopping_list)
        shopping_list = None


class ShoppingList(object):
    """
    A ShoppingList represents one shopping list
    It contains shopping items
    """
    def __init__(self, title, description=''):
        #self.creator = creator
        if utilities.check_type(title, str):
            self.title = title
        if utilities.check_type(description, str):
            self.description = description
        self.items = []

    #def is_creator(self, user):
      #  """
      #  Checks whether the object passed is the 
      #  same as self.creator
      #  """
      #  return user == self.creator

    def set_title(self, title):
        """
        Sets the title of the shopping list
        """
        if utilities.check_type(title, str):
            self.title = title

    def set_description(self, description):
        """
        Sets the description of the shopping list
        """
        if utilities.check_type(description, str):
            self.description = description
    
    def add_item(self, item_name):
        """
        Adds an item to the list giving it the name
        item_name
        """
        item = ShoppingItem(item_name)
        self.items.append(item)
        return item

    def delete_item(self, item):
        """
        Deletes an item from a shopping list
        """
        if not isinstance(item, ShoppingItem):
            raise TypeError('The item is of invalid type')
        if item in self.items:
            self.items.remove(item)
        else:
            raise KeyError('The item does not exist')


class ShoppingItem(object):
    """
    A ShoppingItem represents a single item in 
    a shopping list
    """
    def __init__(self, name, quantity=0, unit='', parent_list=None):
        if utilities.check_type(name, str):
            self.name = name
        if utilities.check_type(quantity, float, int):
            self.quantity = quantity
        if utilities.check_type(unit, str):
            self.unit = unit
        self.parent_list = parent_list

    def set_name(self, name):
        """
        Sets the name of the shopping list item
        """
        if utilities.check_type(name, str):
            self.name = name

    def set_unit(self, unit):
        """
        Sets the unit of the shopping list item
        """
        if utilities.check_type(unit, str):
            self.unit = unit

    def set_quantity(self, quantity):
        """
        Sets the quantity of the shopping list item
        """
        if utilities.check_type(quantity, float, int):
            self.quantity = float(quantity)