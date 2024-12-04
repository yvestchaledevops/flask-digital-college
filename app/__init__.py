from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Load configuration
    
    app.config.from_object('config.Config')

    # Initialize extensions
    db.init_app(app)

    # Import and register routes
    with app.app_context():
        from .routes import main_bp  # Import your Blueprint (or routes.py)
        app.register_blueprint(main_bp)
        from .routes import admin_bp
        app.register_blueprint(admin_bp)
    
    # Import models to register them with the app
    with app.app_context():
        from .models import RetourFormation

    return app
