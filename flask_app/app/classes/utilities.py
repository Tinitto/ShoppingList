"""
This module has functions used across different classes
"""

import re


def check_type(obj, type_object, error_string='Invalid type'):
    """
    Checks the type of obj against the type_object
    and returns True is the same or else raises TypeError
    """
    if isinstance(obj, type_object):
            return True
    else:
        raise TypeError(error_string)


def check_email_format(email):
    """
    Checks that the email is in the right format with at
    least one @ and one period (.)
    """
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValueError('Invalid email format')
    return True


def check_password_format(password):
    """
    Checks to ensure that the password is a string of not less
    than 6 characters
    """
    if check_type(password, str):
        if len(password) < 6:
            raise ValueError("Your password is too short")
        return True
