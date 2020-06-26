"""Initialize Flask app"""
from flask import Flask

def create_app():
    """Construct core Flask application with embedded Dash app. """
    app = Flask(__name__)    

    with app.app_context():
        # Import Flask routes
        from . import routes
        # Import Dash application
        from .plotydash.dashboard import create_dashboard
        app = create_dashboard(app)

        return app