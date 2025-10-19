#!/usr/bin/python3
"""
A simple Python script to create the 'alx_book_store' database in MySQL.
If the database already exists, the script will not fail.
"""

import mysql.connector

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password_here"  # Replace with your MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create database (won’t fail if it already exists)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error: Unable to connect or create database. Details: {err}")

    finally:
        # Close the cursor and connection properly
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
