# Practical example of API rest with Python, Flask, SQLAlchemy and SQLite

## Basic exercise of a crud with Python

This exercise is a basic example of a crud with *Python, flask and SQLite*, it is an **API** to save, query, update, and delete a list of users, the goal of this **API** will be to become in a ***Fake users generator*** service, there are currently only 3 endpoints for the methods, *GET*, *POST*, *PUT*

### Install the project

To install the project after cloning it, you must start a virtual environment in which you must add all the necessary installations and, obviously, have Python 3 installed.

### Dependencies

The dependencies that will need to be installed to run the application correctly are:
- flask
-flask-sqlalchemy
-flask-marshmallow
- marshmallow-sqlalchemy

SQLite will be used as the database, which already comes in the Python packages, so there is no need to install anything else

The command to install all dependencies with pip will be

~~~
pip install flask flask-sqlalchemy flask-marshmallow masrshmallow-sqlalchemy
~~~

### Start the app

To run the app, once all dependencies are installed, run the following command from the project folder

~~~
 pyhton3 app.py
~~~

This runs the app on ***localhost:5000***

### Add a user

To add a user, a JSON object must be sent to the following endpoint through the *POST* method

~~~
/user
~~~

The object must contain the following:

~~~
{
    "name": "string",
    "additionalName": "string",
    "lastName": "string",
    "secondLastName": "string",
    "age": 0,
    "birthDate": "string"
}
~~~

### Query existing users

To consult the existing users, a *GET* request must be made to the following endpoint:

~~~
/users
~~~

Which will respond with a list of users in the following format

~~~
[
    {
        "name": "string",
        "additionalName": "string",
        "lastName": "string",
        "secondLastName": "string",
        "age": 0,
        "birthDate": "string"
    }
]
~~~

### Query a single user

To query a single user, a *GET* request must be made to the following endpoint:

~~~
/user/{id}
~~~

Where ***{id}*** is replaced by the ID of the user to query

### Update a user

To update a user, a *PUT* request must be made to the following endponit:

~~~
/user/{id}
~~~

Where ***{id}*** is replaced by the ID of the user to be updated, a JSON object must also be sent with the new user data in the following format:

~~~
{
    "name": "string",
    "additionalName": "string",
    "lastName": "string",
    "secondLastName": "string",
    "age": 0,
    "birthDate": "string"
}
~~~