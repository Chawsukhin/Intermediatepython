
import pymysql # Create a custom context manager object
class MyDatabase(object): # Receive parameters and create database connection objects
    def __init__(self, host, port, user, passwd, database):
        self.__db = pymysql.Connection(host, port, user, passwd, database, charset='utf8')
# Return database connection object
    def __enter__(self):
        return self.__db

    # Close database connection
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__db.close()
    def main():
        with MyDatabase('localhost', 3306, 'root', 'chawsu', 'center') as db:
            cur = db.cursor()
            cur.execute("SELECT * FROM dname")
            result = cur.fetchall()
            for i in result:
                print(i)
                cur.close()
                if __name__ == '__main__': main()
