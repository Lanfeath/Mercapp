import sqlite3


def get_cursor():
    conn = sqlite3.connect("db_mercapp.db")
    return conn.cursor()


def select_all_records_by_category(cursor, id_promotion):
    sql = "SELECT * FROM product WHERE id_product=?"
    cursor.execute(sql, [id_promotion])
    print(cursor.fetchall())  # or use fetchone()
    print("\nHere is a listing of the products if the id promotion is: " + id_promotion + "\n")
    for row in cursor.execute("SELECT rowid, * FROM product ORDER BY rowid"):
        print(row)


def select_using_like(cursor, text):
    print("\nLIKE query results:\n")
    sql = f"""
    SELECT * FROM product
    WHERE title LIKE '{text}%'"""
    cursor.execute(sql)
    print(cursor.fetchall())


if __name__ == '__main__':
    cursor = get_cursor()
    select_all_records_by_category(cursor,
                                   id_promotion='1')
    select_using_like(cursor, text='poivrons')
