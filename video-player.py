from threading import Timer
import mplayer, asyncio, evdev
#from pynput import keyboard

"""
Clark Dever - clarkdever@gmail.com
12/10/2018

mplayer -list-properties will provide you a list of available properties
mplayer -input cmdlist will provide you a list of commands

IMPORTANT NOTE: The mplayer wrapper used here will only implement commands if there is not a property available that does the same thing

TODO:
1) implement with arcade buttons instead of keylisteners
"""

#initialize all the things
player1Path = '/dev/input/event4'
player2Path = '/dev/input/event5'
player1 = evdev.InputDevice(player1Path)
player2 = evdev.InputDevice(player2Path)
#p = mplayer.Player()
#p.loadfile('sharks.mp4')
#p.fullscreen = True #make it fullscreen
#p.ontop = True #place our video layer on top
#p.pause()  #unpause the file, it loads paused
#p.osdlevel = 0 #turn off on screen display
#print('file name:', p.path, "\n", 'clip length:', p.length)


def play_clip(position, duration):
    """Plays a clip starting at position for duration
    This is really hacky - please tell me how to do it correctly.
    """
    print('play_clip()')
    try:
        if t is not None: #if a timer exists, cancel the timer before creating a new one
            t.cancel()
            t = Timer(duration, pause)
            p.time_pos = position
            t.start()
    except NameError: #this is the first time this method has been called, create a timer
        global t 
        t = Timer(duration, pause)
        p.time_pos = position
        t.start()


def pause():
    """Pauses play"""
    try:
        p.pause()
        print('pause() fired by play_clip Timer')
    except:
        print('Pause Failed')
        
def on_press(device, event):
    """
    executes program flow based on keypresses
    print('length: ', p.length)
    print('time_pos: ', p.time_pos)
    print('percent_pos: ', p.percent_pos)
    """
    try:
        if device.path == player1Path:
            if event.code == 298:
                p.time_pos = p.time_pos - 10
            elif event.code == 299:
                p.time_post = p.time_pos + 10
        else:
            print('Player 2')
        
    except AttributeError:
        print('special key {0} pressed'.format(
            event.code))

async def print_events(device):
    async for event in device.async_read_loop():
        if event.type == evdev.ecodes.EV_KEY:
            #print(evdev.categorize(event))
            print(event.code, device.path)
            on_press(device, event)

for device in player1, player2:
    asyncio.ensure_future(print_events(device))

loop = asyncio.get_event_loop()
loop.run_forever()
