import sqlite3

conn = sqlite3.connect("db_mercapp.db")
cursor = conn.cursor()

# # insert a record into the administrator table in the db_mercapp database
cursor.execute("""ALTER TABLE product 
                RENAME COLUMN id TO product_id;"""
               )
# save data
conn.commit()