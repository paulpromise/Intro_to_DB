
import mysql.connector


def create_database():
    connection = None
    try:
        # Connect to MySQL server 
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  
            password="password123",  
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error while connecting to MySQL: {err}")

    finally:
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")


if __name__ == "__main__":
    create_database()
