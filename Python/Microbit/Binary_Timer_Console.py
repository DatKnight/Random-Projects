from time import sleep

counting = True
time = ["seconds","minutes","hours","days","weeks"]
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

    print(binary[4])
    print(binary[3])
    print(binary[2])
    print(binary[1])
    print(binary[0])

    if time[0] == 60:
        time[0] = 0
        time[1] += 1
            
    if time[1] == 60:
        time[1] = 0
        time[2] += 1
            
    if time[2] == 24:
        time[2] = 0
        time[3] += 1
            
    if time[2] == 7:
        time[3] = 0
        time[4] += 1

    sleep(1)
    time[0] += 1
