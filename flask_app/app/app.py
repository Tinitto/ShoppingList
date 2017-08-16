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
