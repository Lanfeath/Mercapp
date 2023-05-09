from flask_sqlalchemy import SQLAlchemy

from .views import app

# Create database connection object
db = SQLAlchemy(app)


class Administrator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(30), nullable=False)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    picture = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(50), nullable=True)
    promotion = db.Column(db.Integer, nullable=True)

    def __init__(self, title, description, price, picture, category, promotion):
        self.title = title
        self.description = description
        self.price = price
        self.picture = picture
        self.category = category
        self.promotion = promotion


class Promotion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    percentage = db.Column(db.Float, nullable=False)

    def __init__(self, start_date, end_date, percentage):
        self.start_date = start_date
        self.end_date = end_date
        self.percentage = percentage


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)

    def __init__(self, title):
        self.title = title

