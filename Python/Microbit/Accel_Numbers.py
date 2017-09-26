from microbit import *

middle = Image("36963:"
               "36963:"
               "36963:"
               "36963:"
               "36963:")

left = Image("69630:"
             "69630:"
             "69630:"
             "69630:"
             "69630:")

h_left = Image("96300:"
               "96300:"
               "96300:"
               "96300:"
               "96300:")

right = Image("03696:"
              "03696:"
              "03696:"
              "03696:"
              "03696:")

h_right = Image("00369:"
                "00369:"
                "00369:"
                "00369:"
                "00369:")


while True:
    reading = accelerometer.get_x()

    if reading > 300 and reading < 600:
        display.show(right)
    elif reading > 600:
        display.show(h_right)
    elif reading < -300 and reading > -600:
        display.show(left)
    elif reading < -600:
        display.show(h_left)
    else:
        display.show(middle)

        
