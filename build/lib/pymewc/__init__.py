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

def hello():
    print("Hello world, The package is properly installed version = 0.0.7.4")

