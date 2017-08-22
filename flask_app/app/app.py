"""
The entry point into the flask app
"""


from flask import Flask, session, request, redirect, url_for, abort, \
    render_template, flash
from app.classes import shopping
from app.crud import user as user_functions

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
        #form_data = dict(request.form)
        form_data = user_functions.process_form_data(dict(request.form))
    except AttributeError:
        error = 'invalid request'        
    if form_data:
       # get the data and attempt to create a new user in g
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
            user = user_functions.get_user_from_g(form_data['username'])
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
    flash('successful redirect')
    return render_template('lists.html')


@app.route('/user/<string:username>/shoppinglist/<string:title>',
methods=['POST', 'GET', 'DELETE', 'PUT'])
def show_single_shoppinglist(username, title):
    """
    This view shows(GET) all the items in a shopping list of the 
    given title belonging to user of the mentioned username. 

    It also allows for editting(PUT) and deleting(DELETE) of a 
    shopping list.

    It also allows for creation(POST) of new shoppinglist items
    """


@app.route('/user/<string:username>/shoppinglist/<string:title>\
/item/<string:name>', methods=['DELETE', 'PUT'])
def edit_shopping_item(username, title, name):
    """
    This route deals allows deleting (DELETE) or editing(PUT) of an
    item on a list
    """
