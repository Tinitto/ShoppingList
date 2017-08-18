"""
The entry point into the flask app
"""


from flask import Flask, session, request, redirect, url_for, abort, \
    render_template, flash

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(
    {
        'SECRET_KEY':'development key'
    }
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
        flash('You have logged out successfully')
        return redirect(url_for('index'))
    else:
        error = 'User not found'
    return render_template('index.html', error=error)


@app.route('/signin', methods=['POST'])
def signin():
    """
    The signin route handles POST data sent 
    from the signin form on the home/index page

    user registered in session is a 
    dictionary of username, password and logged_in
    """
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
        flash('Login successful')
        return redirect(url_for('show_user_record',
                     username=saved_user['username']))
    return render_template('index.html', error=error)


@app.route('/user')
def show_users():
    """
    The show_users route shows(GET) the list of users
    of the app
    """


@app.route('/user/<str:username>',
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


@app.route('/user/<str:username>/shoppinglist/<str:title>',
methods=['POST', 'GET', 'DELETE', 'PUT'])
def show_single_shoppinglist(username, title):
    """
    This view shows(GET) all the items in a shopping list of the 
    given title belonging to user of the mentioned username. 

    It also allows for editting(PUT) and deleting(DELETE) of a 
    shopping list.

    It also allows for creation(POST) of new shoppinglist items
    """


@app.route('/user/<str:username>/shoppinglist/<str:title>\
/item/<str:name>', methods=['DELETE', 'PUT'])
def edit_shopping_item(username, title, name):
    """
    This route deals allows deleting (DELETE) or editing(PUT) of an
    item on a list
    """
