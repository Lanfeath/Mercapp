import os

from .views import app

# app = Flask(__name__)

app.secret_key = "UxeifO_xxT9jAHbHqme_jQ"


# Localisation of file to save images
upload = './Mercapp/static/temp/'
app.config['UPLOAD'] = upload

# Connect sqlalchemy to app
# models.db.db.init_apppython