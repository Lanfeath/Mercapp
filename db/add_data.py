# add_data.py

import sqlite3

conn = sqlite3.connect("db_mercapp.db")
cursor = conn.cursor()

# # insert a record into the administrator table in the db_mercapp database
cursor.execute("""INSERT INTO category
                  VALUES ('cosmetiques')"""
               )
# save data
conn.commit()

# insert multiple records using the more secure "?" method
# admins = [('1', 'admin', '4Dm1N'),
#           ('2', 'admin2', '4Dm1N2')]
# cursor.executemany("INSERT INTO administrator VALUES (?,?,?)", admins)
# conn.commit()
#
# # insert multiple records using the more secure "?" method
# products = [('1', 'banana', 'venez gouter nos super bananes du Pérou','5.5','./temp/banane.jpg', 'fruits','none'),
#             ('2', 'poivrons', 'nos poivrons de production locale','3.0','./temp/poivrons.jpg','legumes','1'),
#             ('3', 'hugo boss', 'le parfum qui les fera toutes craquer','55.5','./temp/parfum_hugo.jpg','cosmetique','2'),]
# cursor.executemany("INSERT INTO product VALUES (?,?,?,?,?,?,?)", products)
# conn.commit()
#
# # insert multiple records using the more secure "?" method
# promotions = [('1', '08/05/2023', '18/05/2023', '0.3'),
#               ('2', '01/04/2023', '13/05/2023', '0.2')]
# cursor.executemany("INSERT INTO promotion VALUES (?,?,?,?)", promotions)
# conn.commit()

# insert multiple records using the more secure "?" method
# categories = ['fruits',
#               'legumes',
#               'cosmetiques']
# cursor.executemany("INSERT INTO category VALUES (?)", categories)
# conn.commit()
