from PyQt5 import QtWidgets, QtCore
import sys
from PyQt5 import QtTest
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow

from ui.RFID_App import Ui_MainWindow
import serial
import time
import pandas as pd
from datetime import datetime


excel_file = "C:\Python\RFID\RFID_Data.xlsx"



# Replace 'COM12' with your COM port, e.g., 'COM4', '/dev/ttyUSB0', etc.
COM_PORT = 'COM3'
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

def find_and_print_row_pandas(excel_file, search_string,self):
    try:
        df = pd.read_excel(excel_file)
    except FileNotFoundError:
        print("File not found")
        return

    matching_row = df[df[df.columns[0]] == search_string]
    if not matching_row.empty:
        row_values = matching_row.values[0]
        print(row_values)
        
        self.ui.Plate.setText(row_values[3])
        self.ui.Name.setText(str(row_values[1]) + " " + str(row_values[2]))
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.ui.Time.setText(current_time)
        
    else:
        print("String not found")
        self.ui.Name.setText("No Data")
        self.ui.Plate.setText("No Data")
        self.ui.Time.setText("No Data")

class APP(QMainWindow, Ui_MainWindow):
    tag_detected = QtCore.pyqtSignal(str)
    def __init__(self):
        
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        

        self.rfid_reader = RFIDReader()
        self.rfid_reader.tag_detected.connect(self.update_line_edit)
        self.rfid_reader.start()

    def update_line_edit(self, tag_id):
        self.ui.RFID_scan.setText(tag_id)
        find_and_print_row_pandas(excel_file, tag_id,self)

def main():
    app = QApplication(sys.argv)
    main_window = APP()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

