import mysql.connector # type: ignore
from mysql.connector import Error # type: ignore

try:
    connection = mysql.connector.connect(
        host="localhost",
        user= "root",
        password = "8@HairLine@8"
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")

finally:
    if 'cursor' in locals():
        cursor.close()

    if 'connection' in locals() and connection.is_connected():
        connection.close()