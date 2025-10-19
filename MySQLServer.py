
import mysql.connector
from mysql.connector import errorcode

try:
    # Connect to MySQL server (adjust user and password as needed)
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password"  # Replace with your actual MySQL root password
    )

    cursor = connection.cursor()

    # Attempt to create the database
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Clean up: close cursor and connection
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()