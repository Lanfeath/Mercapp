import os
from flask import Flask, render_template, redirect, url_for


from .views import app
from . import models

app.secret_key = "UxeifO_xxT9jAHbHqme_jQ"


# Localisation of file to save images
upload = './Mercapp/static/temp/'
app.config['UPLOAD'] = upload

# Connect sqlalchemy to app
# models.db_mercapp.db.init_app(app)

# @app.cli.command()
# def init_db():
# models.init_db()
