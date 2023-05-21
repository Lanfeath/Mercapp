from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField, SelectField, TextAreaField, DecimalField, DateField, HiddenField, \
    SubmitField, FileField, PasswordField
from wtforms.validators import DataRequired, Length
from flask_login import UserMixin
from flask import url_for, redirect

from .views import app, login_manager

# Create database connection object
db = SQLAlchemy(app)


@login_manager.user_loader
def load_user(user_id):
    return Usertable.query.get(user_id)


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('index'))


class Usertable(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(30), nullable=False)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    picture = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    promotion = db.Column(db.Integer, nullable=True)
    unit = db.Column(db.String(50), nullable=False)

    def __init__(self, title, description, price, picture, category, promotion, unit):
        self.title = title
        self.description = description
        self.price = price
        self.picture = picture
        self.category = category
        self.promotion = promotion
        self.unit = unit


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


class AddProductForm(FlaskForm):
    id_field = HiddenField()
    title = StringField('Nom du produit:', validators=[DataRequired(), Length(2, 40)])
    category = SelectField('Catégorie associée:',
                           choices=[],
                           validators=[DataRequired()])
    description = TextAreaField('Description du produit:', validators=[DataRequired()])
    price = DecimalField('Prix du produit:', places=2, validators=[DataRequired()])
    unit = SelectField('Unité:',
                       choices=[('€/Kg'), ('€')],
                       validators=[DataRequired()])
    picture = FileField("Selectionner votre image", validators=[DataRequired()])  # IMAGE
    submit = SubmitField("Envoyer")


class AddPromotiontForm(FlaskForm):
    percentage = DecimalField('% de promotion:', validators=[DataRequired()])
    start_date = DateField('Date de début de la promotion:', validators=[DataRequired()])
    end_date = DateField('Date de fin de la promotion:', validators=[DataRequired()])
    submit = SubmitField("Envoyer")


class LoginForm(FlaskForm):
    login = StringField("Nom d'utilisateur :", validators=[DataRequired()])
    password = PasswordField('Mot de passe:', validators=[DataRequired()])
    submit = SubmitField("Se connecter")


class SelectCategory(FlaskForm):
    categories = SelectField('Trier par catégorie:',
                           choices=[],
                           validators=[DataRequired()])
    submit = SubmitField("Envoyer")


@app.cli.command()
def init_db():
    db.create_all()