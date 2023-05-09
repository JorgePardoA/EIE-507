import serial
import time

class Comunicacion_Serial:
    def __init__(self, puerto='/dev/ttyACM0', baud=9600, timeout=1):
        self.puerto = puerto
        self.baud = baud
        self.timeout = timeout
        self.conexion = serial.Serial(port=self.puerto, baudrate=self.baud, timeout=self.timeout)

    def leer_serial(self):
        while True:
            if self.conexion.in_waiting > 0:
                datos= self.conexion.readline().decode('ascii').rstrip()
                print(datos)

if __name__ == '__main__':
    serial_communication = Comunicacion_Serial()
    serial_communication.leer_serial()
