import mysql.connector
from mysql.connector import Error

def create_database():
    
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='ishimwe2K3@'
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            # Create database
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully.")
    
    except Error as e:
        print(f"Error: Unable to connect or create database. Details: {e}")

    finally:
        if "cursor" in locals() and cursor:
            cursor.close()
        if "connection" in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()