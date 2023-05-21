import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash

conn = sqlite3.connect("mercapp.db")
cursor = conn.cursor()

# insert categories records

categories = [('0', 'Aucune'),
              ('1', 'Fruits'),
              ('3', 'Légumes'),
              ('4', 'Cosmétiques')]
cursor.executemany("INSERT INTO category VALUES (?,?)", categories)
conn.commit()

# insert admin records
pasword_admin = generate_password_hash("iM4Dm1N")
pasword_test = generate_password_hash("test")

admin = [('0', 'admin', pasword_admin),
         ('1', 'test', pasword_test)]

cursor.executemany("INSERT INTO user VALUES (?,?,?)", admin)
conn.commit()

