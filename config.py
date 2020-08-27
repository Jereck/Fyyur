import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
# Replaced my actual password with <password> to hide my super secret password
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:<password>@localhost:5432/fyyur'
SQLALCHEMY_TRACK_MODIFICATIONS = False