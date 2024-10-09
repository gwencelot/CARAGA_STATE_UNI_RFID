
import pandas as pd
import serial
import time

excel_file = "C:\Python\RFID\RFID_Data.xlsx"
search_string = "ABC123"



def find_and_print_row_pandas(excel_file, search_string):
  """
  Finds a string in the first column of an Excel file and prints the entire row using Pandas.

  Args:
    excel_file: The path to the Excel file.
    search_string: The string to search for.
  """

  try:
    df = pd.read_excel(excel_file)
  except FileNotFoundError:
    print("File not found")
    return

  matching_row = df[df[df.columns[0]] == search_string]
  if not matching_row.empty:
    print(matching_row)
  else:
    print("String not found")

def scan_serial_for_string(port, baudrate, search_string):
  """Scans the specified serial port for the given search string.

  Args:
    port: The serial port to connect to (e.g., '/dev/ttyUSB0').
    baudrate: The baud rate of the serial port.
    search_string: The string to search for.

  Returns:
    True if the string is found, False otherwise.
  """

  with serial.Serial(port, baudrate, timeout=1) as ser:
    while True:
      line = ser.readline().decode('utf-8').rstrip()
      if search_string in line:
        print(f"Found: {line}")
        return True

      time.sleep(0.1)  # Adjust sleep time as needed

  return False
""""
find_and_print_row_pandas(excel_file, search_string)
"""
if __name__ == "__main__":
  port = '/dev/ttyUSB0'  # Replace with your serial port
  baudrate = 9600
  search_string = "your_search_string"

  if scan_serial_for_string(port, baudrate, search_string):
    print("String found")
  else:
    print("String not found")
