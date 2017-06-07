import time
import winsound

# Below is code that supports the playback of .wav files
######################### 
# import os
# def soundAlert():
#     os.system("start c:/Users/Luke/OneDrive/Documents/python_scripts/Pomodoro/8bit.wav")
#########################

def soundAlert():
    winsound.Beep(600, 200)
    winsound.Beep(400, 200)
    winsound.Beep(600, 200)
def pomoTimer(timeVal):
    countTime = timeVal * 60
    for i in range(0, (int(countTime))):
        time.sleep(1)
        countMin = int(countTime / 60)
        countSec = int(countTime % 60)
        print(countMin, ":", countSec, sep='')
        countTime -= 1
        if int(i % 2) == 0:
            winsound.Beep(1100, 45)
        else:
            winsound.Beep(1000, 45)
    soundAlert()
    input("Press Enter to continue...")


def pomodoro():
    workTime = 25
    pauseTime = float(input("Break time?: "))
    breakTime = float(input("Long break time?: "))
    breakFreq = int(input("Work sessions until long break?: "))
    while True:
        for i in range(0, (breakFreq - 1)):
            pomoTimer(workTime)
            pomoTimer(pauseTime)
        pomoTimer(workTime)
        pomoTimer(breakTime)


pomodoro()
