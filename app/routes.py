from app import flask_app

# Define the routes and their view functions
@flask_app.route('/')
@flask_app.route('/index')
def index():
    return "Hello, Engr. Adam Abdulkareem"
