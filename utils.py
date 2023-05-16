import random
import sqlite3 as sql

from Mercapp.models import User, Product, Promotion, Category


def find_admin(login):
    admin = User.query.filter_by(login=login).first()
    return admin


def get_all_products():
    products = Product.query.all()
    return products


def get_all_categories():
    categories = Category.query.all()
    return categories


def find_product(product_id):
    product = Product.query.filter_by(id=product_id).first()
    return product


def get_promotions():
    promotions = Promotion.query.all()
    return promotions
