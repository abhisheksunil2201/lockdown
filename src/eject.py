import wmi
import time
import threading
from encryption import encrypt_files


def detect_eject():
    c = wmi.WMI()
    while True:
        for usb in c.Win32_PnPEntity(ConfigManagerErrorCode=0):
            if 'USB Mass Storage Device' in str(usb):
                print("Pendrive inserted")
                # You initiate encryption here
        time.sleep(2)  # Adjust the polling interval as needed


if __name__ == "__main__":
    eject_thread = threading.Thread(target=detect_eject)
    eject_thread.daemon = True
    eject_thread.start()

    # Keep the script running
    while True:
        pass
