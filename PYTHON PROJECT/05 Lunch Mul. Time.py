import time
import win32com.client
from datetime import datetime

print("_______LUNCH_REMINDER_________")

T1 = input("Enter first reminder time (HH:MM): ")
T2 = input("Enter second reminder time (HH:MM): ")
T3 = input("Enter third reminder time (HH:MM): ")

reminders = [T1, T2, T3]

print("\nReminders set for:")

print("1.", T1)
print("2.", T2)
print("3.", T3)

speaker = win32com.client.Dispatch("SAPI.SpVoice")

print("\nReminder program is running...")

while len(reminders) > 0:

    current_time = datetime.now().strftime("%H:%M")

    if current_time in reminders:

        print("Reminder:", current_time)

        for i in range(5):
            i = i + 1
            print("Voices:", i)

            speaker.Speak("Stop your work. Please drink water.")

        reminders.remove(current_time)

    time.sleep(1)

print("\nAll 3 reminders completed.")
