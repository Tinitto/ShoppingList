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
    def __init__(self, name, email, password):
        if utilities.check_type(name, str,
             "A user's name can only be a string"):
             self.name = name
        if utilities.check_email_format(email):
            self.email = email
        if utilities.check_password_format(password):
            self.password = password

    def set_name(self, name):
        """
        Set the name of the user
        """
        if utilities.check_type(name, str,
             "A user's name can only be a string"):
             self.name = name
    
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


class ShoppingList(object):
    """
    A ShoppingList represents one shopping list
    It contains shopping items
    """
    def __init__(self, title, description='', creator=None):
        self.creator = creator
        self.title = title
        self.description = description


class ShoppingItem(object):
    """
    A ShoppingItem represents a single item in 
    a shopping list
    """
    def __init__(self, name, quantity=0, unit='', parent_list=None):
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.parent_list = parent_list