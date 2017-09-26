from microbit import *

uart.init(baudrate=9600, bits=8, parity=None, stop=1, *, tx=None, rx=None)
uart.write("Test")
