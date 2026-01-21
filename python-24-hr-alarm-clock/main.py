import datetime
import time
import sys
import threading

stop_event = threading.Event()

def alarm_sound():
    try:
        import winsound
        while not stop_event.is_set():
            winsound.Beep(1000, 800)
    except:
        while not stop_event.is_set():
            sys.stdout.write('\a')
            sys.stdout.flush()
            time.sleep(1)

# ---------- INPUT ----------
date_input = input("Enter date (DD/MM/YYYY): ")
time_input = input("Enter time (HH:MM:SS): ")

day, month, year = map(int, date_input.split("/"))
hour, minute, second = map(int, time_input.split(":"))

alarm_time = datetime.datetime(year, month, day, hour, minute, second)

print("\nAlarm set for:", alarm_time)
print("Waiting...\n")

# ---------- WAIT UNTIL ALARM TIME ----------
while datetime.datetime.now() < alarm_time:
    time.sleep(1)

print("⏰ ALARM! (Stops after 5 seconds or any key)")

# ---------- START ALARM THREAD ----------
alarm_thread = threading.Thread(target=alarm_sound)
alarm_thread.start()

# ---------- STOP CONDITIONS ----------
def auto_stop():
    time.sleep(5)
    stop_event.set()

timer_thread = threading.Thread(target=auto_stop)
timer_thread.start()

input()                 # user presses any key + Enter
stop_event.set()        # stops alarm immediately

# ---------- CLEAN EXIT ----------
alarm_thread.join()
timer_thread.join()

print("Alarm stopped. Program exiting.")
sys.exit(0)
