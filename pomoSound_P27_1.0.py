import time
import winsound

# Below is code that supports the playback of .wav files
######################### 
# import os
# def soundAlert():
#     os.system("start FILE_PATH_HERE")
#########################

def soundAlert():
    winsound.Beep(600, 200)
    winsound.Beep(400, 200)
    winsound.Beep(600, 300)
    winsound.Beep(400, 300)
    winsound.Beep(600, 400)
    winsound.Beep(400, 400)
    winsound.Beep(600, 600)
    winsound.Beep(400, 2000)
def pomoTimer(timeVal, soundOpt):
    countTime = timeVal * 60
    for i in range(0, (int(countTime))):
        time.sleep(1)
        countMin = int(countTime / 60)
        countSec = int(countTime % 60)
        print countMin, ":", countSec
        countTime -= 1
        if soundOpt:
            if int(i % 2) == 0:
                winsound.Beep(1100, 10)
            else:
                winsound.Beep(1000, 10)
    soundAlert()
    raw_input("Press Enter to continue...")

def pomodoro():
    workTime = 25
    pauseTime = float(input("Break time?: "))
    breakTime = float(input("Long break time?: "))
    breakFreq = int(input("Work sessions until long break?: "))
    while True:
        for i in range(0, (breakFreq - 1)):
            pomoTimer(workTime, True)
            pomoTimer(pauseTime, False)
        pomoTimer(workTime, True)
        pomoTimer(breakTime, False)


pomodoro()

