# ShoppingList [![Build Status](https://travis-ci.org/Tinitto/ShoppingList.png?branch=master)](https://travis-ci.org/Tinitto/ShoppingList)
An app that allows you to keep and share a list of the items you want to spend money on

## About
This project is part of the [Andela Fellowship](https://andela.com/) Self Learning Clinic Curriculum.

The ShoppingList app is a web application meant to help users keep track of their shopping items easily. 

It also enables users to share such lists with other people for example if the shopper and the list compiler are different people.

## Dependencies
1. Bootstrap version 4.0.0-alpha
2. Jquery version 3.2.1
3. popper.js version 1.11.1+
4. Flask version 0.12+
5. Python version 3.5+

## Composition
1. [Wireframes](https://github.com/Tinitto/ShoppingList/tree/master/wireframes) drawn with [Pencil](https://pencil.evolus.vn/)
2. [UML class diagram](https://github.com/Tinitto/ShoppingList/tree/master/designs)
3. [HTML/CSS front end](https://github.com/Tinitto/ShoppingList/tree/master/UI)
4. [Flask App](https://github.com/Tinitto/ShoppingList/tree/master/flask_app)

## How to run flask application
1. Clone the repository to your computer
2. Ensure you have installed the above dependencies into your virtualenv
3. In your terminal, enter the directory ShoppingList/flask_app
4. run the following command to install the app package into your virtualenv (Don't forget the dot at the end)

    ``` pip install --editable . ```

5. To start the app, run the following commands in succession still in the same directory

    ```export FLASK_APP=app```

    ```export FLASK_DEBUG=true ```

    ```flask run ```

    _On windows, use 'set' instead of 'export'_


## How to test the flask appliaction
1. Clone the repository to your computer
2. Ensure you have the dependencies on your system
3. Install nose in your virtualenv using your terminal


    ``` pip install nose```

4. run command in the folder ShoppingList/flask_app/

    ```nosetests test ```

5. Observer the output in your terminal

## To Do
1. Add [TravisCI](https://travis-ci.org/)
2. Link HTML/CSS frontend to the flask app
3. Deploy demo app to Heroku

## Other Details
- Pivotal Tracker board for the project can be found [here](https://www.pivotaltracker.com/n/projects/2092528)


