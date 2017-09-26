from microbit import *

count = 0
counting = True
#seconds,minutes,hours,days,weeks
time = [0,0,0,0,0]
binary = ["","","","",""]

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

    for x in range(0,5):
        binary[x] = convertBin(time[x])

    img = Image(binary[4] + ":" +
                binary[3] + ":" +
                binary[2] + ":" +
                binary[1] + ":" +
                binary[0] + ":")

    display.show(img)

    if button_a.is_pressed() or button_b.is_pressed():
        if counting == True:
            counting = False
        else:
            counting == True

    if counting == True and count == 5:
        time[0] += 1
        
        if time[0] == 32:
            time[0] = 0
            time[1] += 1
            
        if time[1] == 32:
            time[1] = 0
            time[2] += 1
            
        if time[2] == 32:
            time[2] = 0
            time[3] += 1
            
        if time[2] == 32:
            time[3] = 0
            time[4] += 1

        count = 0

    sleep(200)
    count += 1
