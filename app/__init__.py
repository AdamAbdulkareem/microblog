from flask import Flask

# Create the Flask application instance
flask_app = Flask(__name__)

# Import the routes module
from app import routes
