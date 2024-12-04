import os

class Config:
    # General Configuration
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_secure_key'

    # MySQL Database Configuration
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://root:mysql@localhost/digital_college"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
