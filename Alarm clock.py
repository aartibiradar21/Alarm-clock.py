#  import required module
# from playsound import playsound
  
# for playing note.wav file
# playsound('/home/aarti/Downloads/ringtone.aarti')
# print('playing sound using  playsound')

import datetime
from playsound import playsound


import datetime
from playsound import playsound

# for playing note.wav file
# playsound('/home/alpana/Downloads/alarm')
# print('playing sound using playsound')
Alarmhour=int(input("Enter hour: "))
Alarmmin=int(input("Enter the min: "))
AlarmAm=input("am/pm: ")

if AlarmAm=="pm":
    Alarmhour+=12
elif AlarmAm=="am":
    Alarmhour-=12

while True:
    if Alarmhour==datetime.datetime.now().hour and Alarmmin==datetime.datetime.now().minute:
        print('playing sound using playsound')
        print("playing....")
        playsound('/home/aarti/Downloads/ringtone.aarti')
        break








