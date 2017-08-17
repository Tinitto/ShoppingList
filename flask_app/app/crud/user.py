"""
This file contains funcitonality for 
- user login
- user signup
- user logout
"""


def login(**kwargs):
    """
    This checks provided credentials against 
    those available and returns a user object
    storing it in the session
    """


def signup(**kwargs):
    """
    This validates data and saves it in the session 
    as a new user to allow user to login
    After successful signup, the user is automatically logged in
    """


def logout(user):
    """
    This removes the logged in user from the session
    """