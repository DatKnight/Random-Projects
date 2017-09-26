from microbit import *

score = 0

def convertBin(num):
    binary = [16,8,4,2,1]
    fin = ""
    for x in binary:
        if (num - x) >= 0:
            fin += "9"
            num = num - x
        else:
            fin += "0"
    return fin

while True:
    x = convertBin(score)

    img = Image("00000:"
                "00000:"
                "00000:"
                "00000:" +
                x + ":")

    display.show(img)

    if button_a.is_pressed():
        score -= 1
    elif button_b.is_pressed():
        score += 1

    sleep(200)
