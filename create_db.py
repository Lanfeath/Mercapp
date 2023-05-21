# create_database.py
import sqlite3

conn = sqlite3.connect("mercapp.db")
cursor = conn.cursor()

# create a table
cursor.execute("""CREATE TABLE user
                  (id INTEGER PRIMARY KEY, 
                  login TEXT not null, 
                  password TEXT not null)
               """)

# create a table
cursor.execute("""CREATE TABLE product
                  (id INTEGER PRIMARY KEY, 
                  title TEXT not null, 
                  description TEXT not null, 
                  price FLOAT not null,
                  picture TEXT not null, 
                  category TEXT not null, 
                  promotion FLOAT,
                  unit TEXT not null)
               """)

# create a table
cursor.execute("""CREATE TABLE promotion
                  (id INTEGER PRIMARY KEY,
                   start_date DATE not null,
                   end_date DATE not null,
                   percentage FLOAT not null)
               """)

# create a table
cursor.execute("""CREATE TABLE category
                  (id INTEGER PRIMARY KEY,
                  title TEXT not null)
               """)