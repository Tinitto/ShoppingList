"""
This is the entry point for the app
"""

import os
from flask import request, redirect, url_for,\
    render_template, flash
from app import create_app
from app.classes.shopping import db
from app.crud import user as user_functions
from app.crud import shopping_list as shoppinglist_helpers

config_name = os.getenv('APP_SETTINGS') or 'development'
app = create_app(config_name)

with app.app_context():
    db.create_all()

# routes
@app.route('/')
def index():
    """
    The home/index page shows signup and signin forms
    """
    return render_template('index.html')


@app.route('/signup', methods=['POST'])
def signup():
    """
    The signup route handles POST data sent from 
    the signup form on the home/index page
    """
    error = None
    form_data = None
    try:
        form_data = user_functions.process_form_data(dict(request.form))
    except AttributeError:
        error = 'invalid request'
    if form_data:
        # get the data and attempt to create a new user
        try:
            user_functions.create_new_user(form_data)
        except ValueError:
            error = 'Unacceptable form input %s' % str(form_data)
        else:
            # if new user is created, log them in
            try:
                user_functions.add_user_to_session(form_data['username'])
            except KeyError:
                error = 'Error while logging in'
            else:
                # redirect the user to dashboard
                flash('User sign up successful')
                return redirect(url_for('show_user_record',
                                username=form_data['username']))
    if error:
        flash(error)
    return redirect(url_for('index'))


@app.route('/signout')
def signout():
    """
    The signout route logs out the user
    """
    error = None
    # remove username from session
    try:
        user_functions.remove_user_from_session()
    except KeyError:
        error = 'You are not logged in'
    if error:
        flash(error)
    return render_template('index.html')


@app.route('/signin', methods=['POST'])
def signin():
    """
    Logs in the user
    """
    error = None
    form_data = None
    # get request.form data
    try:
        form_data = user_functions.process_form_data(dict(request.form))
    except AttributeError:
        error = "Invalid form input"
    
    if form_data:
        try:
            user = user_functions.get_user_by_username(form_data['username'])
        except KeyError:
            error = "User does not exist"
        else:
            # if user exists, check against the saved password
            if user.password == form_data['password']:
                # if it is the same, save username to session
                user_functions.add_user_to_session(form_data['username'])
                flash('Login successful')
                return redirect(url_for('show_user_record',
                                username=form_data['username']))
            else:
                error = "Invalid password or username"
    if error:
        flash(error)
    return render_template('index.html')


@app.route('/user/<string:username>',
 methods=['POST', 'GET'])
def show_user_record(username):
    """
    The show_user_record route shows(GET) 
    the basic details about the user of the said
    username and the list of shopping lists
     belonging to that user. 
    
    It allows creation (POST) of new shopping
    lists also.
    """
    error = None
    editable = False
    user_details = None
    user_lists = None
    user = None
    if user_functions.get_logged_in_username():
        editable = True

    try:
        user = user_functions.get_user_by_username(username)
    except KeyError:
        error = "User does not exist"
    
    if user:
        user_details = dict(name=user.name, email=user.email,
            username=user.username)
        user_lists = list(user.get_shopping_lists())
        # show editable record to user i.e. option to add list
    if request.method == 'POST' and not error:
        # Get the form data
        try:
            form_data = user_functions.process_form_data(dict(request.form))
        except AttributeError:
            error = "Invalid form input"
        if not error:
            # Try to create a new shopping list
            user_lists.append(user.create_shopping_list(**form_data))
        
    return render_template('lists.html', user_details=user_details,
                 editable=editable, error=error, user_lists=user_lists)


@app.route('/user/<string:username>/shoppinglist/<int:list_id>',
methods=['POST', 'GET'])
def show_single_shoppinglist(username, list_id):
    """
    This view shows(GET) all the items in a shopping list of the 
    given title belonging to user of the mentioned username. 

    It also allows for editting(put) and deleting(delete) of a 
    shopping list.

    It also allows for creation(POST) of new shoppinglist items
    """
    # get the ShoppingList object
    error = None
    editable = False
    list_details = {}
    items = []
    try:
        shopping_list = shoppinglist_helpers.get_shopping_list(list_id)
    except (ValueError, KeyError):
        error = "Shopping list does not exist"
    
    if not error and user_functions.get_logged_in_username() == \
                                     shopping_list.owner.username:
        editable = True
    if request.method == 'GET':
        method = request.args.get('_method') or None
        if editable and method == 'delete':
            # attempt to delete the shoppinglist
            shopping_list.delete()
            flash('Delete successful')
            return redirect(url_for('show_user_record', username=username))
        
        if editable and method == 'put':
            pass
            # get form data
            # attempt to update the details of shopping list
        
        if not error:
            list_details = dict(title=shopping_list.title,
                            description=shopping_list.description)
            items = list(shopping_list.get_shopping_items())
        return render_template('single.html', list_details=list_details, username=username,
                 editable=editable, error=error, items=items, list_id=list_id)
        
    if request.method == 'POST' and not error:
        # get form data
        try:
            form_data = user_functions.process_form_data(dict(request.form))
        except AttributeError:
            error = "Invalid form input"
            flash(error)
    
        if form_data:
            try:
                shoppinglist_helpers.add_item_with_details(shopping_list, **form_data)
            except ValueError:
                error = "Invalid form input for item"
                flash(error)
            else:
                flash('Item has been added successfully')

            return redirect(url_for('show_single_shoppinglist', username=username,
                                list_id=list_id))


@app.route('/user/<string:username>/shoppinglist/<int:list_id>\
/item/<int:item_id>', methods=['DELETE', 'PUT'])
def edit_shopping_item(username, list_id, item_id):
    """
    This route deals allows deleting (DELETE) or editing(PUT) of an
    item on a list
    """
    if request.method == 'PUT':
        pass
        # get form data
        # attempt to update the item
    if request.method == 'DELETE':
        pass
        # attempt to delete the item

if __name__ == '__main__':
    app.run()