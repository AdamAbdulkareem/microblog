from flask import Flask
from config import Config

# Create the Flask application instance
flask_app = Flask(__name__)
flask_app.config.from_object(Config)

# Import the routes module
from app import routes
