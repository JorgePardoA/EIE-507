import serial
import time

class Comunicacion_Serial:
    def __init__(self, puerto='/dev/ttyACM0', baud=9600, timeout=1):
        self.puerto = puerto
        self.baud = baud
        self.timeout = timeout
        self.conexion = serial.Serial(port=self.puerto, baudrate=self.baud, timeout=self.timeout)
        self.datos_guard=[]

    def leer_serial(self):
        while True:
            if self.conexion.in_waiting > 0:
                datos= self.conexion.readline().decode('ascii').rstrip()
                return datos
    def treinta_seg(self):
        self.datos_guard=[]
        while True:
            for i in range(2):
                datos1=self.leer_serial()
                self.datos_guard.append(datos1)
                time.sleep(30)
                if i==1:
                    suma=0
                    for j in range(len(self.datos_guard)):
                        suma=suma+float(self.datos_guard[j])
                    sum10=suma/len(self.datos_guard)
                    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                    with open("/home/pi/ficheroEjercicio1.3.txt","a") as f:
                        f.write(f"[{timestamp}] {sum10}\n")
                    print(f"[{timestamp}] {sum10}")
                    sum10=0
                    self.datos_guard = []


if __name__ == '__main__':
    serial_communication = Comunicacion_Serial()
    serial_communication.treinta_seg()


