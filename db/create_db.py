# create_database.py
import sqlite3

conn = sqlite3.connect("db_mercapp.db")
cursor = conn.cursor()

# create a table
cursor.execute("""CREATE TABLE administrator
                  (id_admin INT, login TEXT, password TEXT)
               """)

# create a table
cursor.execute("""CREATE TABLE product
                  (id_product INT, title TEXT, description TEXT, price FLOAT,
                   picture TEXT, category TEXT, id_promotion INT)
               """)

# create a table
cursor.execute("""CREATE TABLE promotion
                  (id_promotion INT, start_date DATE, end_date DATE, percentage FLOAT)
               """)

# create a table
cursor.execute("""CREATE TABLE category
                  (category TEXT)
               """)