import mysql.connector

class Database:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def create_user(self, username, password):
        sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
        self.cursor.execute(sql, (username, password))
        self.connection.commit()

    def find_user(self, username):
        sql = "SELECT * FROM users WHERE username = %s"
        self.cursor.execute(sql, (username,))
        return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.connection.close()