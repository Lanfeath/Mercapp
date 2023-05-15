import random
import sqlite3 as sql

from Mercapp.models import User, Product, Promotion


def find_admin(login):
    admin = User.query.filter_by(login=login).first()
    return admin


def get_all_products():
    products = Product.query.all()
    return products


def find_product(product_id):
    product = Product.query.filter_by(Product.id == product_id).first()
    return product


def find_promotion(promotion_id):
    promotion = Promotion.query.filter(Promotion.id == Promotion[promotion_id]).all()
    return promotion

def add_data(title, content):
  try:
    # Connecting to database
    con = sql.connect('shot_database.db')
    # Getting cursor
    c =  con.cursor()
    # Adding data
    c.execute("INSERT INTO Shots (title, content) VALUES (%s, %s)" %(title, content))
    # Applying changes
    con.commit()
  except:
    print("An error has occured")
