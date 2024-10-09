from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton, QMessageBox, QVBoxLayout, QTabWidget

import sys
from PyQt5 import QtTest
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow

from ui.RFID_App3 import Ui_MainWindow
import serial
import time
import pandas as pd
from datetime import datetime
import mysql.connector

# Replace 'COM12' with your COM port, e.g., 'COM4', '/dev/ttyUSB0', etc.
COM_PORT = 'COM12'
BAUD_RATE = 9600  # Set the baud rate according to your RFID reader's specifications
READ_TIMEOUT = 1  # Timeout in seconds
CLEAR_INTERVAL = 5  # Interval to clear the seen_tags set in seconds

class RFIDReader(QtCore.QThread):
    tag_detected = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(RFIDReader, self).__init__(parent)
        self.seen_tags = set()
        self.last_clear_time = time.time()
        self.ser = serial.Serial(COM_PORT, BAUD_RATE, timeout=READ_TIMEOUT)

    def run(self):
        while True:
            # Check if it's time to clear the seen_tags set
            if time.time() - self.last_clear_time > CLEAR_INTERVAL:
                self.seen_tags.clear()
                self.last_clear_time = time.time()

            # Read RFID tag
            tag_id = self.read_rfid_tag()
            if tag_id and tag_id not in self.seen_tags:
                # Add the new tag to the set
                self.seen_tags.add(tag_id)
                # Emit the signal with the new unique RFID tag
                self.tag_detected.emit(tag_id)

    def read_rfid_tag(self):
        """Reads an RFID tag and returns its UID as a hexadecimal string."""
        start_time = time.time()
        byte_data = bytearray()

        while time.time() - start_time < READ_TIMEOUT:
            if self.ser.in_waiting > 0:
                byte_data.extend(self.ser.read(1))
                if len(byte_data) >= 3:  # We only need the first 3 bytes (6 hex characters)
                    break

        if byte_data:
            # Take only the first 3 bytes (6 hex characters)
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

def save_to_RegDatabase(host, user, password, database, table, name, rfid, plate,self):
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
            query_insert = f"INSERT INTO {table} (name, rfid, plate, time) VALUES (%s, %s, %s, %s)"
            cursor.execute(query_insert, (name, rfid, plate, current_time))
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
        # Ensure the database and table exist
        create_regdatabase_and_table_if_not_exists(host, user, password, 'rfid_registrations', 'rfid_registrations_table1')
        create_logdatabase_and_table_if_not_exists(host, user, password, 'vehicle_records', 'vehicle_records_table1')
        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database='rfid_registrations'
        )

        cursor = connection.cursor()

        # Check if the RFID already exists
        query_check = f"SELECT * FROM {'rfid_registrations_table1'} WHERE rfid = %s"
        cursor.execute(query_check, (rfid,))
        existing_row = cursor.fetchone()

        if existing_row:
            saveData=True
            id, name, rfid, plate_number, date_time = existing_row
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.ui.vplate.setText(plate_number)
            self.ui.vname.setText(name)
            self.ui.vtime.setText(current_time)
            
        else:
            saveData=False
            print("String not found")
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.ui.vname.setText("No Data")
            self.ui.vplate.setText("No Data")
            self.ui.vtime.setText(current_time)

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


#save to logs database
    if saveData==True:
        try:
            # Establish a connection to the MySQL database
            connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database='vehicle_records'
            )
            cursor = connection.cursor()
            
            current_time = self.ui.vtime.text()
            plate = self.ui.vplate.text()
            name = self.ui.vname.text()
        
            # Prepare the SQL query to insert the row
            query_insert = f"INSERT INTO {'vehicle_records_table1'} (name, rfid, plate, time) VALUES (%s, %s, %s, %s)"
            cursor.execute(query_insert, (name, rfid, plate, current_time))
            connection.commit()

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
        self.ui.pushButton.clicked.connect(self.check_password)
        self.ui.tabWidget.currentChanged.connect(self.on_tab_change)

    def on_tab_change(self, index):
        if index == 0:
            #self.scan_and_log()
            print("Tab 1 is selected. Running function for Tab 1.")
        elif index == 1:
            #self.ui.pushButton.clicked.connect(self.check_password)
            print("Tab 2 is selected. Running function for Tab 2.")
        
    def scan_and_log(self):
        self.rfid_reader = RFIDReader()
        self.rfid_reader.tag_detected.connect(self.update_line_edit)
        self.rfid_reader.start()

    def update_line_edit(self, tag_id):
        self.ui.RFID_scan.setText(tag_id)

      
        tag_id= self.ui.vrfid.text()
        scan_from_RegDatabase_and_log(
                host='localhost',
                user='root',
                password='',  # Replace with your password if set, otherwise leave it blank
                rfid = tag_id,
                self = self
                )
        
    def check_password(self):
        correct_password = "123"  # Replace with the actual correct password
        user_input = self.ui.password.text()
        
        if user_input == correct_password:
            if self.ui.rname_2.text()==''or  self.ui.rplate.text() =='' or self.ui.rrfid.text()=='':
                QMessageBox.warning(self, 'Password Input', 'Some inputs are blank!')
            else:
                save_to_RegDatabase(
                host='localhost',
                user='root',
                password='',  # Replace with your password if set, otherwise leave it blank
                database='rfid_registrations',
                table='rfid_registrations_table1',
                name= self.ui.rname_2.text(),
                rfid= self.ui.rrfid.text(),
                plate= self.ui.rplate.text(),
                self = self
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