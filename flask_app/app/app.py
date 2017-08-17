"""
The entry point into the flask app
"""


from flask import Flask

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


@app.route('/signup', methods=['POST'])
def signup():
    """
    The signup route handles POST data sent from 
    the signup form on the home/index page
    """


@app.route('/signin', methods=['POST'])
def signin():
    """
    The signin route handles POST data sent 
    from the signin form on the home/index page
    """


@app.route('/user')
def show_users():
    """
    The show_users route shows(GET) the list of users
    of the app
    """


@app.route('/user/<int:user_id>',
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


@app.route('/user/<int:user_id>/shoppinglist/<int:list_id>',
methods=['POST', 'GET', 'DELETE', 'PUT'])
def show_single_shoppinglist(user_id, list_id):
    """
    This view shows(GET) all the items in a shopping list of id 
    list_id belonging to user user_id. 

    It also allows for editting(PUT) and deleting(DELETE) of a 
    shopping list.

    It also allows for creation(POST) of new shoppinglist items
    """


@app.route('/user/<int:user_id>/shoppinglist/<int:list_id>\
/item/<int:item_id>', methods=['DELETE', 'PUT'])
def edit_shopping_item(user_id, list_id, item_id):
    """
    This route deals allows deleting (DELETE) or editing(PUT) of an
    item on a list
    """
