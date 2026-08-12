
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

l = ["Ram", "Raj", "Ajay"]

for name in l:
    speaker.Speak(f"shoutout to {l, name}")   
    print(l)

print("The Successfully Executed!")    