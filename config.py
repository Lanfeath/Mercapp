import os
SECRET_KEY = '#d#JeqTTW\nilK\\7m\x0bv#\tj~#H'

# Database initialization
if os.environ.get('DATABASE_URL') is None:
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'mercapp.db')
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']