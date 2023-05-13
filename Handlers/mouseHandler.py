import serial
import serial.tools.list_ports
import time
import sys
from termcolor import colored


class Mouse:
    def __init__(self, COM_PORT):
        self.COM_PORT = COM_PORT
        self.serial_port = serial.Serial()
        self.serial_port.baudrate = 115200
        self.serial_port.timeout = 1
        self.serial_port.port = self.find_serial_port()
        try:
            self.serial_port.open()
        except serial.SerialException:
            print(colored('[ERROR]', 'red'), colored('Colorant is already open or com port in use by another app. Close Colorant and other apps before retrying.', 'white'))
            time.sleep(10)
            sys.exit()

    def find_serial_port(self):
        port = next((port for port in serial.tools.list_ports.comports() if self.COM_PORT in port.description), None)
        if port is not None:
            return port.device
        else:
            print(colored('[ERROR]', 'red'), colored('Unable to find the specified com port. Please check its connection and try again.', 'white'))
            time.sleep(10)
            sys.exit()

    def move(self, x, y):
        self.serial_port.write(f'M{x},{y}\n'.encode())

    def click(self):
        self.serial_port.write(b'C\n')
        
    def close(self):
        self.serial_port.close()

    def __del__(self):
        self.close()
