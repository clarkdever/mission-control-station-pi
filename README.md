# mission-control-station-pi
A python application for raspberry pi that executes commands based on keypresses from the zero delay arcade usb found in many MAME joystick packages



- button-action.py - Deprecated - used to unit test buttons when I was first wiring up MCS
- button-mapper.py - Deprecated - Prints any input from the gamepads when you press buttons and move the sticks
- multi-controller.py - button-mapper - now works with multiple keypads
- video-player.py - This is the application that runs on the MCS Jr and plays videos based on inputs

## Installing the systemd service
To launch mcs-jr on boot, copy [mcs-jr.service] to `/etc/systemd/system/` and execute the following commands:
```
sudo systemctl enable mcs-jr.service
sudo reboot
```

This will add it as a service that launches on boot. The service will automatically try to relaunch if it crashes.
