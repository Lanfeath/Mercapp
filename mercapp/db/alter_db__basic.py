# Establish connection to MySQL database
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database = "geeks"
)

#getting the cursor by cursor() method
mycursor = db.cursor()

query = "ALTER TABLE persons RENAME COLUMN PersonID TO Emp_Id;"
mycursor.execute(query)

# close the Connection
db.close()
