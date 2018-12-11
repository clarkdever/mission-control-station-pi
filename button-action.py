import evdev
from evdev import InputDevice, categorize, ecodes
import os

#creates object 'gamepad' to access data
gamepad = InputDevice('/dev/input/event4')

#button code variables (change to suit your device)
greenBtn = 298
#prints out device info at start
print(gamepad)

#loop and filter by event code and print the mapped label
for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        if event.value == 1:
            if event.code == greenBtn:
                print("Green Button Pressed")
                os.system("omxplayer /opt/vc/src/hello_pi/hello_video/test.h264")