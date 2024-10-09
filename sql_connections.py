import mysql.connector
from datetime import datetime
from PyQt5 import QtWidgets, QtCore
import sys

def create_database_and_table_if_not_exists(host, user, password, database, table):
    connection = None
    try:
        # Establish a connection to the MySQL server
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        cursor = connection.cursor()

        # Check if the database exists, if not, create it
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
        
        # Use the newly created or existing database
        cursor.execute(f"USE {database}")
        
        # Check if the table exists, if not, create it
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            rfid VARCHAR(255) NOT NULL,
            time DATETIME NOT NULL
        )
        """)
        connection.commit()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

def save_to_database(host, user, password, database, table, name, rfid):
    try:
        # Ensure the database and table exist
        create_database_and_table_if_not_exists(host, user, password, database, table)

        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        cursor = connection.cursor()

        # Get current time
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Prepare the SQL query to insert the row
        query = f"INSERT INTO {table} (name, rfid, time) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, rfid, current_time))
        connection.commit()

        print("Data saved successfully")



    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def find_and_print_row_mysql(host, user, password, database, table, column, search_string):
    try:
         # Ensure the database and table exist
        create_database_and_table_if_not_exists('localhost', 'root', '', 'rfid_testings', 'rfid_testings_table1')

        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database=database
        )

        cursor = connection.cursor()

        # Prepare the SQL query to search for the row
        query = f"SELECT * FROM {table} WHERE {column} = %s"
        cursor.execute(query, (search_string,))

        # Fetch the matching row
        matching_row = cursor.fetchone()

        if matching_row:
            print(matching_row)
            """
            self.ui.Plate.setText(matching_row[3])
            self.ui.Name.setText(f"{matching_row[1]} {matching_row[2]}")
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.ui.Time.setText(current_time)
            """
        else:
            print("String not found") 
            """
            self.ui.Name.setText("No Data")
            self.ui.Plate.setText("No Data")
            self.ui.Time.setText("No Data")
            """
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        """
        self.ui.Name.setText("No Data")
        self.ui.Plate.setText("No Data")
        self.ui.Time.setText("No Data")
        """

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def main():  
      
      user_input  = input("Please enter a string: ")
      print("You entered:", user_input )
      find_and_print_row_mysql(
        host='localhost',
        user='root',
        password='',
        database='rfid_testings',
        table='rfid_testings_table1',
        column='rfid',
        search_string=user_input ,
          
    )
      """
      save_to_database(
            host='localhost',
            user='root',
            password='',  # Replace with your password if set, otherwise leave it blank
            database='rfid_testings',
            table='rfid_testings_table1',
            name='fred2',
            rfid='a2',
            
        )
      """
   

   

if __name__ == "__main__":
    while True:
        main()