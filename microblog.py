from app import flask_app, db
from app.models import User, Post

@flask_app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, "Post": Post}

# Run the Flask application
if __name__ == '__main__':
    flask_app.run(debug=True)