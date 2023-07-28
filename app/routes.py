from flask import render_template
from app import flask_app


# Define the routes and their view functions
@flask_app.route('/')
@flask_app.route('/index')
def index():
    user = {"username" : "Engr. Abdulkareem"}
    posts = [
        {
            'author': {'username': 'Adam'},
            'body': 'Beautiful day in Ibadan'
        },
        {
            'author': {'username': 'Dare'},
            'body': 'The Avengers movie was so cool'
        }
    ]
    
    return render_template('index.html', title = "Home",user=user, posts=posts)
