import os

# Database initialization
if os.environ.get('DATABASE_URL') is None:
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'mercapp.db')
else:
    # need to change postgres to postgresql in DATABASE_URL
    # Check if the URL database is already in the good format: with Postgresql instead of just postgres
    if os.environ.get('DATABASE_URL').find('postgresql') != -1:
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("postgres", "postgresql")
    else:
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
