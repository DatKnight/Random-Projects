from random import randint
from microbit import *

field = [
    "00000:",
    "00000:",
    "00000:",
    "00000:"
    ]
player = 2
fruit = [0,0,0]
fruits = [[0,0],[0,0],[0,0]]
score = 0
count = 0

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
    row = field[y]
    half1 = row[0:x]
    half2 = row[x + 1:6]
    fin = half1 + val + half2
    field[y] = fin

def drawPlayer():
    global player
    changePixel(player,3,"9")

def moveRight():
    global player
    if player != 4:
        changePixel(player,3,"0")
        player += 1
        changePixel(player,3,"9")

def moveLeft():
    global player
    if player != 0:
        changePixel(player,3,"0")
        player -= 1
        changePixel(player,3,"9")

def activateFruit(fruitNum):
    if fruit[fruitNum] != 1:
        fruit[fruitNum] = 1
        x = randint(0,4)
        y = 0
        fruits[fruitNum][0] = x
        fruits[fruitNum][1] = y
        changePixel(x,y,"9")

def deactivateFruit(fruitNum):
    if fruit[fruitNum] != 0:
        fruit[fruitNum] = 0
        x = fruits[fruitNum][0]
        y = fruits[fruitNum][1]
        changePixel(x,y,"0")
        fruits[fruitNum][0] = 0
        fruits[fruitNum][1] = 0

def down(fruitNum):
    global fruits
    if fruit[fruitNum] == 1:
        x = fruits[fruitNum][0]
        y = fruits[fruitNum][1]
        changePixel(x,y,"0")
        fruits[fruitNum][1] = y + 1
        y += 1
        changePixel(x,y,"9")

"""
0 = Fruit not at player level,
1 = fruit missed player,
2 = player caught fruit
"""
def checkFruit(fruitNum):
    global fruits
    global player
    if fruit[fruitNum] == 1:
        x = fruits[fruitNum][0]
        y = fruits[fruitNum][1]
        if y == 3:
            if x == player:
                return 2
            else:
                return 1
        else:
            return 0

def freeFruit():
    ret = False
    for x in range(0,3):
        if fruit[x] == 0:
            ret = x
            break
    return ret
      
def printScreen():
    print(field[0])
    print(field[1])
    print(field[2])
    print(field[3])
    print(convertBin(score) + ":")

def printLED():
    img = Image(field[0] +
                field[1] +
                field[2] +
                field[3] +
                convertBin(score) + ":")

    display.show(img)

def main():
    global count
    global score
    while True:
        drawPlayer()
        printLED()
        

        if button_a.is_pressed():
            moveLeft()
        elif button_b.is_pressed():
            moveRight()

        if count == 10:
            for fruitNum in range(0,3):
                down(fruitNum)
                printLED()
                result = checkFruit(fruitNum)
                if result == 1 or result == 2:
                    if result == 2:
                        score += 1
                    deactivateFruit(fruitNum)
            free = freeFruit()
            if type(free) == int:
                activateFruit(free)
            count = 0
            
        count += 1
        sleep(90)
        
main()
