import pyembedded
from pyembedded.rfid_module.rfid import RFID

# Assuming you have set up your RFID reader correctly
rfid_reader = pyembedded.RFID()

try:
    # Read data from the RFID reader
    data = rfid_reader.read()
    
    # If data is in bytes, decode it using the appropriate encoding
    decoded_data = data.decode('latin1')  # Replace 'latin1' with the correct encoding if necessary
    print(decoded_data)

except UnicodeDecodeError as e:
    print(f"Error decoding data: {e}")
