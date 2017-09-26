from microbit import *

up = Image("09990"
           "90009"
           "90009"
           "90009"
           "09990")

down = Image("09990"
             "99999"
             "99999"
             "99999"
             "09990")

left = Image("00900:"
             "09000:"
             "99999:"
             "09000:"
             "00900:")

right = Image("00900:"
              "00090:"
              "99999:"
              "00090:"
              "00900:")

forward = Image("00900"
                "09090"
                "90009"
                "00000"
                "00000")

back = Image("00000"
             "00000"
             "90009"
             "09090"
             "00900")

level = Image("00000:"
              "00000:"
              "99999:"
              "00000:"
              "00000:")

while True:
    reading = accelerometer.get_x()
    string = str(reading)
    display.scroll(string)
    """
    if reading > 60:
        display.scroll(reading)
    elif reading < -60:
        display.scroll(reading)
    else:
        display.show(level)
    """
        
