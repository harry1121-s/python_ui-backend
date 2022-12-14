import serial 
from serial.tools import list_ports
VID = ["10C4", "00"]
PID = ["EA60", "00"]
port = ["Device-1", 'Device-2']
class DAC_Control:
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

    def dacWrite(self, deviceID, dacID, value):
#         Frame Format: FF00 + dacID(8bits) + data + AAFF
        frame = str(dacID) + str(value)
        device = serial.Serial(port[deviceID], baudrate = self.BAUD)

        if device.in_waiting:
            try:
                data = device.readLine()
                print(data)
            except:
                print("COM PORT Error!")
                quit()

        byte = device.write(frame.encode())
        print(byte, " bytes written to COM PORT")
        readBack = device.readline()
        print(readBack)
        device.close()
        return 1 if byte>1 else 0

    def getAvailableDevices(self):
        return port
    