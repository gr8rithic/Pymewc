from os import error
import time

print("Thanks for using pymewc to record any issue mail to gr8rithic@gmail.com")
time.sleep(1)
print('----------------------------------------------------------------------------------------------------')
time.sleep(1)
print("You can also get in touch with me on github link https://github.com/gr8rithic/")
time.sleep(1)
print('----------------------------------------------------------------------------------------------------')
time.sleep(1)
print('Get connected via LinkedIn https://www.linkedin.com/in/rithic-hariharan-8902b4199/')
time.sleep(1)
print('----------------------------------------------------------------------------------------------------')
time.sleep(1)
print('Visit my postfolio https://gr8rithic.github.io/')
time.sleep(1)
print('----------------------------------------------------------------------------------------------------')
time.sleep(1)
print()
print("Setting up the environment")
time.sleep(3)



def serial():
    com_port = input("Enter the com-port(Com4 or /dev/ttyACM0 on Windows and Unix based respectively)")
    baud_rate = int(input("Enter the baud rate as specified in the .ino file"))
    import serial  
    try:
        ser = serial.Serial(com_port, baud_rate)  
    except error:
        print("Check the usb port is mentioned correctly or usb is connected properly")

    while(1):
        try:
            x = (ser.readline().strip())            
            print("Check the usb port is mentioned correctly or usb is connected properly")
            y = (x.decode('utf-8'))       
            print(y)                      

        except UnicodeDecodeError:
            continue        




def scope():
    from pyfirmata2 import Arduino
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    
    com_port = input("Enter the com-port(Com4 or /dev/ttyACM0 on Windows and Unix based respectively)")
    baud_rate = int(input("Enter the baud rate as specified in the .ino file"))
    
    class RealtimePlotWindow:

        def __init__(self):
            self.fig, self.ax = plt.subplots()
            self.plotbuffer = np.zeros(500)
            self.line, = self.ax.plot(self.plotbuffer)
            self.ax.set_ylim(0, 1.5)
            self.ringbuffer = []
            self.ani = animation.FuncAnimation(self.fig, self.update, interval=100)

        def update(self, data):
            self.plotbuffer = np.append(self.plotbuffer, self.ringbuffer)
            self.plotbuffer = self.plotbuffer[-500:]
            self.ringbuffer = []
            self.line.set_ydata(self.plotbuffer)
            return self.line,

        def addData(self, v):
            self.ringbuffer.append(v)

    realtimePlotWindow = RealtimePlotWindow()
    samplingRate = 100
    def callBack(data):
        realtimePlotWindow.addData(data)

    board = Arduino(com_port)
    board.samplingOn(1000 / samplingRate)
    board.analog[0].register_callback(callBack)
    board.analog[0].enable_reporting()
    plt.show()
    board.exit()
    print("The process has been terminated")              


def blink():
    import pyfirmata2
    import time


    pin = int(input("Enter the digital pin you want to make to blink"))
    delay_sec = int(input("Enter the delay you want between the blink"))  


    com_port = input("Enter the com-port(Com4 or /dev/ttyACM0 on Windows and Unix based respectively)")
    baud_rate = int(input("Enter the baud rate as specified in the .ino file"))

    board = pyfirmata2.Arduino(com_port)

    while True:
        board.digital[pin].write(1)  
        time.sleep(delay_sec)
        board.digital[pin].write(0)  
        time.sleep(delay_sec)


def hello():
    print("Hello world, The package is properly installed version = 0.1.3")

