import pymysql as sql

class Database:
    def __init__(self, host, user, password, database):
        self.connection = sql.connect(host=host, user=root, password=Harshit#8955, database="prectice" )
        self.cursor = self.connection.cursor()

    def execute_query(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
            return self.cursor.fetchall()
        except sql.Error as e:
            print(f"Error executing query: {e}")
            return None

    def close(self):
        self.cursor.close()
        self.connection.close()