from microbit import *
from random import randint

count = 0
fruitlist = [[0,0,0],[0,0,0],[0,0,0]]
score = 0
player = 2
field = ["00000:",
         "00000:",
         "00000:",
         "00900:"]

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

def changePixel(x,y,val):
    fin = ""
    start = field[y]
    for i in range(0,5):
        if i == x:
            fin += val
        else:
            fin += start[i]
    return fin

def down():
    changePixel(fruitlist[0][0],fruitlist[0][1],"0")
    fruitlist[0][1] += 1
    changePixel(fruitlist[0][0],fruitlist[0][1],"9")

def movePlayer(position):
    field[3] = "00000:"
    field[3] = changePixel(player,3,"9")

def drawScreen():
    x = convertBin(score)

    img = Image(field[0] +
                field[1] +
                field[2] +
                field[3] +
                x + ":")

    display.show(img)

changePixel(0,0,"9")

while True:

    drawScreen()
    
    if button_a.is_pressed() and player != 0:
        player -= 1
        movePlayer(player)
    elif button_b.is_pressed() and player != 4:
        player += 1
        movePlayer(player)
        
    if count == 5:
        down()
        if fruitlist[0][1] == 4:
            changePixel(fruitlist[0][0],fruitlist[0][1],"0")
            fruitlist[0][0] = 0
            fruitlist[0][1] = 0
            fruitlist[0][2] = 0
            changePixel(fruitlist[0][0],fruitlist[0][1],"9")
    
    count += 1
    sleep(200)
