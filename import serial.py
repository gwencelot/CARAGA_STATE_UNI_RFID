import serial
import time

# Replace 'COM12' with your COM port, e.g., 'COM4', '/dev/ttyUSB0', etc.
COM_PORT = 'COM12'
BAUD_RATE = 9600  # Set the baud rate according to your RFID reader's specifications
READ_TIMEOUT = 1  # Timeout in seconds
CLEAR_INTERVAL = 5  # Interval to clear the seen_tags set in seconds

def read_rfid_tag(serial_connection):
    """Reads an RFID tag and returns its UID as a hexadecimal string."""
    start_time = time.time()
    byte_data = bytearray()

    while time.time() - start_time < READ_TIMEOUT:
        if serial_connection.in_waiting > 0:
            byte_data.extend(serial_connection.read(1))
            if len(byte_data) >= 3:  # We only need the first 3 bytes (6 hex characters)
                break

    if byte_data:
        # Take only the first 3 bytes (6 hex characters)
        hex_tag = ''.join(f'{byte:02X}' for byte in byte_data[:3])
        return hex_tag.upper()

    return None

def main():
    seen_tags = set()
    ser = None
    last_clear_time = time.time()

    try:
        # Initialize the serial connection with a timeout
        ser = serial.Serial(COM_PORT, BAUD_RATE, timeout=READ_TIMEOUT)
        print(f"Connected to {COM_PORT} at {BAUD_RATE} baud rate.")

        while True:
            # Check if it's time to clear the seen_tags set
            if time.time() - last_clear_time > CLEAR_INTERVAL:
                seen_tags.clear()
                last_clear_time = time.time()
                print("Cleared seen_tags set.")

            # Read RFID tag
            tag_id = read_rfid_tag(ser)
            if tag_id and tag_id not in seen_tags:
                # Add the new tag to the set
                seen_tags.add(tag_id)
                # Print the new unique RFID tag
                print(f"RFID tag ID: {tag_id}")

    except serial.SerialException as e:
        print(f"Error: {e}")

    finally:
        if ser and ser.is_open:
            ser.close()
            print("Serial connection closed.")

if __name__ == "__main__":
    main()
