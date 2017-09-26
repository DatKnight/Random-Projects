from random import randint
from time import sleep

"""Sets initial values for global variables such as
the player's starting position,a place to store the
field data, and the initial score"""
count = 0
fruitlist = [[0,0,0],[0,0,0],[0,0,0]]
score = 0
player = 2
field = ["00000:",
         "00000:",
         "00000:",
         "00900:"]

"""Function to convert an intenger into a 5-bit binary number to display on the bottom of the LED matrix"""
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

"""Function to change the signal strength to a single pixel of a given xy value"""
def changePixel(x,y,val):
    fin = ""
    start = field[y]
    for i in range(0,5):
        if i == x:
            fin += val
        else:
            fin += start[i]
    field[y] = fin

"""Function to 'activate' a fruit, placing it on the field"""
def activate(fruit,x):
    fruitlist[fruit][2] = 1
    fruitlist[fruit][0] = x
    changePixel(fruitlist[fruit][0],0,"9")

"""Function to 'deactivate' a fruit and remove it from the field"""
def deactivate(fruit):
    changePixel(fruitlist[fruit][0],fruitlist[fruit][1],"0")
    fruitlist[fruit][0] = 0
    fruitlist[fruit][1] = 0
    fruitlist[fruit][2] = 0

"""Function to find the first deactivated fruit in the list, and return its reference if found"""
def freeFruit():
    for x in range(0,3):
        if fruitlist[x][2] == 0:
            return x
            break
    return False

"""
def moveDown():
    for fruit in range(0,2):
        if fruitlist[fruit][2] == 1 and fruitlist[fruit][1] != 3:
            changePixel(fruitlist[fruit][0],fruitlist[fruit][1],"0")
            fruitlist[fruit][1] += 1
            changePixel(fruitlist[fruit][0],fruitlist[fruit][1],"9")
        elif fruitlist[fruit][2] == 1 and fruitlist[fruit][1] == 3:
            if player == fruitlist[fruit][1]:
                score += 1
            deactivate(fruit)
"""

"""Function to move all fruit down the screen by one pixel, detect if the player has missed/caught a fruit and increment the score if necessary"""
def moveDown():
    global score
    for fruit in range(0,3):
        if fruitlist[fruit][2] == 1:
            if fruitlist[fruit][1] != 3:
                changePixel(fruitlist[fruit][0],fruitlist[fruit][1],"0")
                fruitlist[fruit][1] += 1
                changePixel(fruitlist[fruit][0],fruitlist[fruit][1],"9")
            if fruitlist[fruit][1] == 3:
                if player == fruitlist[fruit][0]:
                    score += 1
                deactivate(fruit)

"""Function to move the player avatar to a specific x coordindate"""        
def movePlayer(position):
    field[3] = "00000:"
    changePixel(player,3,"9")

def drawScreen():
    x = convertBin(score)
    
    print(field[0])
    print(field[1])
    print(field[2])
    print(field[3])
    print(x + ":")
    print("")

""""Main while loop to process game events and trigger necessary functions"""
while True:
    
    drawScreen()

    if count == 5:
        moveDown()
        free = freeFruit()
        ran = randint(0,10)
        if type(free) == int:
            activate(free,randint(0,4))
        count = 0
        
    movePlayer(player)
    count += 1
    sleep(0.2)
