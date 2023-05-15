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
                  (id INTEGER PRIMARY KEY, 
                  title TEXT not null, 
                  description TEXT not null, 
                  price FLOAT not null,
                   picture TEXT not null, 
                   category TEXT not null, 
                   promotion FLOAT)
               """)

# create a table
cursor.execute("""CREATE TABLE promotion
                  (id_promotion INT, start_date DATE, end_date DATE, percentage FLOAT)
               """)

# create a table
cursor.execute("""CREATE TABLE category
                  (category TEXT)
               """)