from playsound import playsound
import time

#This gives instructions to clean the terminal

CLEAR = "\033[2J"

#This gives instructions for the cursor to return to the beginning
CLEAR_AND_RETURN = "\033[H"


def alarm(seconds):
    time_elapsed = 0
    
    print(CLEAR)
    
    while time_elapsed < seconds:
        time.sleep(1) #Wait for a second before continuing so that the alarm doesn't go off immediately
        time_elapsed += 1
        
        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60
        
        print(f"{CLEAR_AND_RETURN}La alarma sonará en: {minutes_left:02d}:{seconds_left:02d}")
    
    playsound("my_alarm.mp3")
    
minutes = int(input("How many minutes for the alarm to play: "))
seconds = int(input("How many seconds for the alarm to play: "))
total_seconds = minutes * 60 + seconds
      
alarm(total_seconds)

