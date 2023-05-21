import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash

conn = sqlite3.connect("mercapp.db")
cursor = conn.cursor()
#
# # #rename column of table promotion
# cursor.execute("""ALTER TABLE promotion
#                 RENAME COLUMN promotion TO percentage;"""
#                )
# # save data
# conn.commit()


# # insert multiple records using the more secure "?" method
#
# categories = [('0','Aucune'),
#               ('1','Fruits'),
#               ('3','Légumes'),
#               ('4','Cosmétiques')]
# cursor.executemany("INSERT INTO category VALUES (?,?)",categories)
# conn.commit()

# insert multiple records using the more secure "?" method
pasword_admin= generate_password_hash("iM4Dm1N")
pasword_test= generate_password_hash("test")

admin = [('0','admin',pasword_admin ),
         ('1','test', pasword_test)]

cursor.executemany("INSERT INTO user VALUES (?,?,?)",admin)
conn.commit()

# hashed_password = generate_password_hash("test")
# print(check_password_hash(hashed_password, "test"))
# print(hashed_password)
