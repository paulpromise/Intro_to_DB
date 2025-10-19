#!/usr/bin/env python3
"""
MySQLServer.py
A simple Python script to create the 'alx_book_store' database in MySQL.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    try:
        # Connect to MySQL server (update user and password as needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",          # Change to your MySQL username
            password="yourpassword"  # Change to your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close the connection properly
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
