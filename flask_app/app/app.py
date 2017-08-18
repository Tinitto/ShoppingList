"""
The entry point into the flask app
"""


<<<<<<< HEAD
from flask import Flask
=======
from flask import Flask, session, request, redirect, url_for, abort, \
    render_template, flash
from app.classes import shopping
>>>>>>> crud_setup

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    SECRET_KEY='development key'
    )
)

app.config.from_envvar('SHOPPINGLIST_SETTINGS', silent=True)

# routes
@app.route('/')
def index():
    """
    The home/index page shows signup and signin forms
    """


@app.route('/signup', methods=['POST'])
def signup():
    """
    The signup route handles POST data sent from 
    the signup form on the home/index page
    """
    error = None
    form_data = None
    try:
        form_data = dict(request.form)
    except AttributeError:
        error = 'invalid request'
    if request.form['name']:
        #try:
        #    user = shopping.User(**form_data)
        #except:
        #    error = 'Error creating user. Check your input'

        if not error:
            # login immediately
            form_data['logged_in'] = True
            session['user'] = form_data # wrong form_data is 
            session.modified = True
            flash('Sign up has been successful')
            return redirect(url_for('show_user_record',
                     username=form_data['username']))
    flash(error)
    return redirect(url_for('index'))


<<<<<<< HEAD
=======
@app.route('/signout')
def signout():
    """
    The signout route logs out the user
    """
    error = None
    if session['user']:
        user = session['user']
        user['logged_in'] = False
        session['user'] = user
        session.modified = True
        flash('You have logged out successfully')
        return redirect(url_for('index'))
    else:
        error = 'User not found'
    return render_template('index.html', error=error)

>>>>>>> crud_setup

@app.route('/signin', methods=['POST'])
def signin():
    """
    The signin route handles POST data sent 
    from the signin form on the home/index page
    """
<<<<<<< HEAD


@app.route('/user')
def show_users():
    """
    The show_users route shows(GET) the list of users
    of the app
    """


@app.route('/user/<int:user_id>',
=======
    error = None
    try:
        saved_user = session['user']
    except KeyError:
        error = 'an error occured in your session. Try refreshing'
        return render_template('index.html', error=error)
    
    if saved_user['logged_in']:
        error = 'Already logged in'
    elif request.form['username'] != saved_user['username']:
        error = 'Invalid username'
    elif request.form['password'] != saved_user['password']:
        error = 'Invalid password'
    else:
        saved_user['logged_in'] = True
        session['user'] = saved_user
        session.modified = True
        flash('Login successful')
        return redirect(url_for('show_user_record',
                     username=saved_user['username']))
    return render_template('index.html', error=error)


@app.route('/user/<string:username>',
>>>>>>> crud_setup
 methods=['POST', 'GET'])
def show_user_record(user_id):
    """
    The show_user_record route shows(GET) 
    the basic details about the user of id,
    user_id and the list of shopping lists
     belonging to that user. 
    
    It allows creation (POST) of new shopping
    lists also.
    """
    flash('successful redirect')
    return render_template('lists.html')


<<<<<<< HEAD
@app.route('/user/<int:user_id>/shoppinglist/<int:list_id>',
=======
@app.route('/user/<string:username>/shoppinglist/<string:title>',
>>>>>>> crud_setup
methods=['POST', 'GET', 'DELETE', 'PUT'])
def show_single_shoppinglist(user_id, list_id):
    """
    This view shows(GET) all the items in a shopping list of id 
    list_id belonging to user user_id. 

    It also allows for editting(PUT) and deleting(DELETE) of a 
    shopping list.

    It also allows for creation(POST) of new shoppinglist items
    """


<<<<<<< HEAD
@app.route('/user/<int:user_id>/shoppinglist/<int:list_id>\
/item/<int:item_id>', methods=['DELETE', 'PUT'])
def edit_shopping_item(user_id, list_id, item_id):
=======
@app.route('/user/<string:username>/shoppinglist/<string:title>\
/item/<string:name>', methods=['DELETE', 'PUT'])
def edit_shopping_item(username, title, name):
>>>>>>> crud_setup
    """
    This route deals allows deleting (DELETE) or editing(PUT) of an
    item on a list
    """
