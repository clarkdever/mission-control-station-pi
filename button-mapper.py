#import Event Devices libraries
import evdev
from evdev import InputDevice, categorize, ecodes

#creates an object called 'gamepad' 
gamepad = InputDevice('/dev/input/event4')

#prints out device info at start
print(gamepad)

#have evdev poll the gamepad and print out button press information 
for event in gamepad.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
        print(evdev.categorize(event))