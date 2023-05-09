import random

from Mercapp.models import Administrator, Product, Promotion

def find_admin(login):
    admin = Administrator.query.filter(Administrator.login == Administrator[login]).all()
    return admin


def get_all_products():
    products = Product.query.all()
    return products


def find_product(product_id):
    products = Product.query.filter(Product.id == Product[product_id]).all()
    return products


def find_promotion(promotion_id):
    promotion = Promotion.query.filter(Promotion.id == Promotion[promotion_id]).all()
    return promotion