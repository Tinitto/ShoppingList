"""
This file contains helper functions \
"""

from flask import session
from app.classes import shopping, utilities



# def add_user_to_g(user):
#    """
#    adds the user object to g
#    """
#    if not isinstance(user, shopping.User):
#        raise TypeError('Is not valid user')
    # create new user
    
#    if not hasattr(g, 'users'):
#        g.users = {user.username: user}
#    else:
#        if not user.username in g.users.keys():
#            g.users[user.username] = user
#        else:
#            raise KeyError('Username already exists')


def create_new_user(user_dict):
    """
    This function creates a user given
    a dictionary with user details 
    """
    try:
        user = shopping.User(**user_dict)
        user.save()
    except:
        raise ValueError('invalid user data')
    # add_user_to_g(user)
    return user

def get_user_by_username(username):
    """
    Get the user object given a username
    """
    if utilities.check_type(username, str):
        pass
    user = shopping.User.query.filter_by(username=username).first()
    if not user:
        raise KeyError('Username not found')
    else:
        return user


#def get_user_from_g(username):
#    """
#    gets the user object from g given a 
#    user name or throws an error if user 
#   doesn't exist
#    """
#    if utilities.check_type(username, str):
#        pass
#    if not username in get_all_usernames_in_g():
#        raise KeyError('Username not found')
#    users = get_all_users_from_g()
#    return users[username]


def get_all_users():
    """
    Get all users
    """
    return shopping.User.get_all()


# def get_all_users_from_g():
#    """
#    returns a dict of all users currently stored
#    in g
#    """
#    if hasattr(g, 'users'):
#        return g.users
#    else:
#        return {}


# def get_all_usernames_in_g():
#    """
#    returns a list of all usernames in g
#    """
#    users = get_all_users_from_g()
#    if users:
#        return users.keys()
#    else:
#        return ()

def delete_user(username):
    """
    Deletes the user with given username
    Returns True on success and False on failure
    """
    try:
        user = get_user_by_username(username)
        user.delete()
        return True
    except KeyError:
        return False

# def delete_user_from_g(username):
#    """
#    Deletes the user with the given username
#    from g
#    """
#    all_usernames = get_all_usernames_in_g()
#    if not all_usernames:
#        raise AttributeError('no usernames found')
#    if username in all_usernames:
#        del(g.users[username])
#    else:
#        raise KeyError('username does not exist')

def add_user_to_session(username):
    """
    Adds the session variable username for 
    logged in user
    """
    try:
        get_user_by_username(username)
    except KeyError:
        raise KeyError('User does not exist')

    session['username'] = username
    session.modified = True


def remove_user_from_session():
    """
    Removes the session variable username
    from the session to logout the user
    """
    if 'username' in session.keys():
        session.pop('username')
        session.modified = True
    else:
        raise KeyError('Username does not exist in the session')
        
        
def process_form_data(dict_form_data):
    """ 
    After casting form data to dict, the values 
    become lists. Transform the lists to non-iterables
    """
    new_dict = {}
    try:
        for key in dict_form_data.keys():
            new_dict[key] = dict_form_data[key][0]
    except AttributeError:
        raise AttributeError('The input should be a dictionary')
    return new_dict
