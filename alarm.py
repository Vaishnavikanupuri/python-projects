from playsound import playsound
import time
def alarm(seconds):
    time_passed=0
    while time_passed<seconds:
        time.sleep(1)
        time_passed+=1
        time_left=seconds-time_passed
        minutes_left=time_left//60
        seconds_left=time_left%60
        print(f"{minutes_left}:{seconds_left}")
    playsound(r"D:\python\ringtone-58761.mp3")

alarm(10)