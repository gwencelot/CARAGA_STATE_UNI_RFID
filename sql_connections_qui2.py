from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton, QMessageBox, QVBoxLayout, QTabWidget

import sys
from PyQt5 import QtTest
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow

from ui.RFID_App5 import Ui_MainWindow
import serial
import time
import pandas as pd
from datetime import datetime
import mysql.connector

# Replace 'COM12' with your COM port,
COM_PORT = 'COM4'
BAUD_RATE = 9600  # Set the baud rate according to your RFID reader's specifications
READ_TIMEOUT = 1  # Timeout in seconds
CLEAR_INTERVAL = 5  # Interval to clear the seen_tags set in seconds

class RFIDReader(QtCore.QThread):
    tag_detected = QtCore.pyqtSignal(str)

    def __init__(self, ser, parent=None):
        super(RFIDReader, self).__init__(parent)
        self.ser = ser
        self.seen_tags = set()
        self.last_clear_time = time.time()
        
    def run(self):
        while True:
            if time.time() - self.last_clear_time > CLEAR_INTERVAL:
                self.seen_tags.clear()
                self.last_clear_time = time.time()

            tag_id = self.read_rfid_tag()
            if tag_id and tag_id not in self.seen_tags:
                self.seen_tags.add(tag_id)
                self.tag_detected.emit(tag_id)

    def read_rfid_tag(self):
        start_time = time.time()
        byte_data = bytearray()

        while time.time() - start_time < READ_TIMEOUT:
            if self.ser.in_waiting > 0:
                byte_data.extend(self.ser.read(1))
                if len(byte_data) >= 3:  # We only need the first 3 bytes (6 hex characters)
                    break

        if byte_data:
            hex_tag = ''.join(f'{byte:02X}' for byte in byte_data[:3])
            return hex_tag.upper()

        return None

def create_regdatabase_and_table_if_not_exists(host, user, password, database, table):
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
            idnumber VARCHAR(255) NOT NULL,
            rfid VARCHAR(255) NOT NULL,
            plate VARCHAR(255) NOT NULL,
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

def create_logdatabase_and_table_if_not_exists(host, user, password, database, table):
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
            idnumber VARCHAR(255) NOT NULL,
            rfid VARCHAR(255) NOT NULL,
            plate VARCHAR(255) NOT NULL,
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

def save_to_RegDatabase(host, user, password, database, table, name, idnumber, rfid, plate,self):
    try:
        # Ensure the database and table exist
        create_regdatabase_and_table_if_not_exists(host, user, password, database, table)
        
        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        cursor = connection.cursor()

        # Check if the RFID already exists
        query_check = f"SELECT * FROM {table} WHERE rfid = %s"
        cursor.execute(query_check, (rfid,))
        existing_row = cursor.fetchone()

        if existing_row:
            print("RFID already exists in the database")
            QMessageBox.information(self, 'Password Input','RFID already exists in the database!')
        else:
            # Get current time
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Prepare the SQL query to insert the row
            query_insert = f"INSERT INTO {table} (name, idnumber, rfid, plate, time) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query_insert, (name, idnumber, rfid, plate, current_time))
            connection.commit()
            QMessageBox.information(self, 'Password Input','Password is correct! Data Saved!')
            print("Data saved successfully")


    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def scan_from_RegDatabase_and_log(host, user, password, rfid, self):
    try:

        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database='rfid_registrations'
        )

        cursor = connection.cursor()

        # Check if the RFID already exists
        query_check = "SELECT name, idnumber, rfid, plate FROM rfid_registrations_table1 WHERE rfid = %s"
        cursor.execute(query_check, (rfid,))
        existing_row = cursor.fetchone()
        
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if existing_row:
            name, idnumber, rfid, plate_number = existing_row
            self.ui.vplate.setText(plate_number)
            self.ui.vname.setText(name)
            self.ui.vidnumber.setText(idnumber)
            self.ui.vtime.setText(current_time)
            save_data = True
        else:
            self.ui.vname.setText("No Data")
            self.ui.vplate.setText("No Data")
            self.ui.vidnumber.setText("No Data")
            self.ui.vtime.setText(current_time)
            save_data = False

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

    if save_data:
        try:
            # Reuse the same connection for the logs database

            connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database='vehicle_records'
            )
            cursor = connection.cursor()

            # Prepare the SQL query to insert the log entry
            query_insert = """
                INSERT INTO vehicle_records_table1 (name, idnumber, rfid, plate, time)
                VALUES (%s, %s, %s, %s, %s )
            """
            cursor.execute(query_insert, (name, idnumber, rfid, plate_number, current_time))
            connection.commit()

            # Fetch the latest 10 records
            query = """
                SELECT rfid, name, idnumber, plate, time
                FROM vehicle_records_table1
                WHERE rfid = %s
                ORDER BY time DESC
                LIMIT 10
            """
            cursor.execute(query, (rfid,))
            records = cursor.fetchall()

            # Update tableWidget with records
            self.ui.tableWidget.setRowCount(len(records))
            for row, record in enumerate(records):
                for col, value in enumerate(record):
                    item = QtWidgets.QTableWidgetItem(str(value))
                    self.ui.tableWidget.setItem(row, col, item)

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    

class APP(QMainWindow, Ui_MainWindow):
    tag_detected = QtCore.pyqtSignal(str)
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        layout = QVBoxLayout()
        
        # Initialize the serial connection once
        self.ser = serial.Serial(COM_PORT, BAUD_RATE, timeout=READ_TIMEOUT)

        create_regdatabase_and_table_if_not_exists(host = 'localhost', user = 'root', password ='', database = 'rfid_registrations', table = 'rfid_registrations_table1')
        create_regdatabase_and_table_if_not_exists(host = 'localhost', user = 'root', password ='', database = 'vehicle_records', table = 'vehicle_records_table1')
        
        # Create an RFIDReader instance, passing the serial connection
        self.rfid_reader = RFIDReader(self.ser)
        self.rfid_reader.tag_detected.connect(self.update_line_edit)

        self.ui.register_button.clicked.connect(self.check_password)
        self.ui.tabWidget.currentChanged.connect(self.on_tab_change)

    def on_tab_change(self, index):
        self.ui.tableWidget.clearContents()  # Clear the contents of the table
        
        if True:
            if index == 0:
                self.rfid_reader.start()  # Start the RFID reader when Tab 1 is selected
                tag_id = self.ui.vrfid.text()
                self.scan_and_log(tag_id)
                print("Tab 1 is selected. Running function for Tab 1.")
            elif index == 1:
                print("Tab 2 is selected. Running function for Tab 2.")
                self.rfid_reader.quit()  # Stop the RFID reader when Tab 2 is selected

    def scan_and_log(self, tag_id):
        # Implement the logic you want to perform when Tab 1 is selected
        self.update_line_edit(tag_id)

    def update_line_edit(self, tag_id):
        self.ui.vrfid.setText(tag_id)
        self.ui.tableWidget.clearContents()

        scan_from_RegDatabase_and_log(
            host='localhost',
            user='root',
            password='',  # Replace with your password if set, otherwise leave it blank
            rfid=tag_id,
            self=self
        )
        
    def check_password(self):
        correct_password = "123"  # Replace with the actual correct password
        user_input = self.ui.password.text()
        
        if user_input == correct_password:
            if self.ui.rname_2.text() == '' or self.ui.rplate.text() == '' or self.ui.rrfid.text() == '':
                QMessageBox.warning(self, 'Password Input', 'Some inputs are blank!')
            else:
                save_to_RegDatabase(
                    host='localhost',
                    user='root',
                    password='',  # Replace with your password if set, otherwise leave it blank
                    database='rfid_registrations',
                    table='rfid_registrations_table1',
                    name=self.ui.rname_2.text(),
                    idnumber=self.ui.ridnumber.text(),
                    rfid=self.ui.rrfid.text(),
                    plate=self.ui.rplate.text(),
                    self=self
                )
        else:
            QMessageBox.warning(self, 'Password Input', 'Password is incorrect.')

            
def main():
    app = QApplication(sys.argv)
    main_window = APP()
    main_window.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()