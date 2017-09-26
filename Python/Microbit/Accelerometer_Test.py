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

left = Image("00900"
             "09000"
             "90000"
             "09000"
             "00900")

right = Image("00900"
              "00090"
              "00009"
              "00090"
              "00900")

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

pics = [[left,right],[forward,back],[up,down]]

def largest(x,y,z):
    if isnegative(x) = True:
        x1 = x * -1
    if isnegative(y) = True:
        y1 = y * -1
    if isnegative(z) = True:
        z1 = z * -1

    if x1 > y1:
        if x1 > z1:
            return 0,x
        else:
            return 2,z
    else:
        if y1 > z1:
            return 1,y

def isnegative(x):
    if str(x[0]) = "-":
        return 0
    else:
        return 1

while True:
    readingx = accelerometer.get_x()
    readingy = accelerometer.get_y()
    readingz = accelerometer.get_z()

    xyz = largest(readingx,readingy,readingz)
    sign = isnumber(xyz[1])
        
    if xyz[1] > 20:
        display.show(pics[0][sign])
    
        
