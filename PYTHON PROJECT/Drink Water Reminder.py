
import time
import win32com.client 
from datetime import datetime
print("Select 1 min next time an present to future:")
T = input("Enter your start study time (HH:MM):")

print("Reminder set for :", T)

while True:

    current_time = datetime.now().strftime('%H:%M')

    if current_time == T:

        speaker = win32com.client.Dispatch("SAPI.SpVoice")

        speaker.Speak('Stop Your Work Please Drink Water')

        break

    time.sleep(1)
