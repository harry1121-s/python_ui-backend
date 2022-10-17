import serial 
import time
from serial.tools import list_ports
VID = ["10C4", "00"]
PID = ["EA60", "00"]
port = ["Device-1", 'Device-2']
class ADC_READ:
    def __init__(self, BAUD):
        self.BAUD = BAUD
        device_list = list_ports.comports()
        for device in device_list:
            if(device.vid != None or device.pid != None):
#                 print(('{:04X}'.format(device.vid)))
                if ('{:04X}'.format(device.vid) == VID[0] and '{:04X}'.format(device.pid) == PID[0]):
#                 if (device.vid == VID[0] and device.pid == PID[0]):
#                     print("Hello")
                    port[0] = device.device
                    print(port[0])
                elif ('{:04X}'.format(device.vid) == VID[1] and '{:04X}'.format(device.pid) == PID[1]):
                    port[1] = device.device
                else:
                    port[0] = None
                    port[1] = None
    
    def adcRead(self, deviceID, adcID):
        device = serial.Serial(port[deviceID], baudrate = self.BAUD)
        x = 0
        f = open('/Users/harryrpo1/Desktop/SPD-ENV/spd_UI/logger-data/logger.txt', 'a', encoding = 'utf-8')
        y = 0
        while(1):
            try:
                if(y == 0):
                    byte = device.write(str(255).encode())
                    y = 1
                input_frame = device.readline()
                decoded_bytes = float(input_frame[0:len(input_frame)-2].decode("utf-8"))
                print(decoded_bytes)
                # f.write(decoded_bytes)
                x = x+1
                if(x==200):
                    x = 0
                    time.sleep(0.01)
                    byte = device.write(str(255).encode())
                    continue
            except:
                f.close()
                print("Keyboard Interrupt")
                break
        

            