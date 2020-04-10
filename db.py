import pymysql
con = pymysql.connect('localhost', 'root',
    'chawsu', 'center')

with con:

    cur = con.cursor()
    cur.execute("SELECT VERSION()")

    version = cur.fetchone()

    print("Database version: {}".format(version[0]))

with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM dname")

    rows = cur.fetchall()

    for row in rows:
        print("{0} {1}".format(row[0], row[1]))
