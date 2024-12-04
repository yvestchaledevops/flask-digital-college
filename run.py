from app import create_app,db
from flask_migrate import Migrate
# Create the Flask app instance
app = create_app()
migrate = Migrate(app, db)

if __name__ == '__main__':
    # Run the app in debug mode (only for development)
    app.run(debug=True)
