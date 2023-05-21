import os
SECRET_KEY = '#d#JeqTTW\nilK\\7m\x0bv#\tj~#H'

# Database initialization
if os.environ.get('DATABASE_URL') is None:
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'mercapp.db')
else:
    # need to change postgres to postgresql in DATABASE_URL
    SQLALCHEMY_DATABASE_URI = 'postgresql://gchlevlsvlfrma:ed468281d60c9a32fe34591476aad8629da336bca86ff94fceeedc5caa662ff0@ec2-52-54-200-216.compute-1.amazonaws.com:5432/d5m3ne4dcin0ue'

