from playsound import playsound
import time
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0
    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1
        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60
        print(f"{CLEAR_AND_RETURN}Time left: {minutes_left:02d}:{seconds_left:02d}")
    playsound("alarm.mp3")
    print("\n⏰ Time's up!")

minutes = int(input("How many minutes to wait:"))
seconds = int(input("Ho many seconds to wait: "))
total_time = minutes * 60 + seconds


alarm(total_time)