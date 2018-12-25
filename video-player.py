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
player1Path = '/dev/input/event5'
player2Path = '/dev/input/event2'
player1 = evdev.InputDevice(player1Path)
player2 = evdev.InputDevice(player2Path)
p = mplayer.Player()
p.loadfile('ChildrensMCS.mp4')
p.fullscreen = True #make it fullscreen
p.ontop = True #place our video layer on top
p.pause()  #unpause the file, it loads paused
p.osdlevel = 0 #turn off on screen display
#print('file name:', p.path, "\n", 'clip length:', p.length)


def play_clip(position, duration):
    """Plays a clip starting at position for duration
    This is really hacky - please tell me how to do it correctly.
    """
    print('play_clip(' + str(position) + ', ' + str(duration) + ')')
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
        if device.path == player1Path: #Left Controllers
            #Joystick
            if event.code == 298:
                #Joystick Left
                print('scrub left:',p.time_pos)
                p.time_pos = float(p.time_pos) - 2
            elif event.code == 299:
                #Joystick Right
                print('scrub right:',p.time_pos)
                p.time_pos = float(p.time_pos) + 2
            elif event.code == 297:
                #Joystick Up
                print('pause:',p.time_pos)
                p.pause()
            elif event.code == 296:
                #Joystick Down
                print('Solar System')
                play_clip(0, 232)
            elif event.code == 288:
                #Left Shoulder - White
                print('Mission Control')
                play_clip(233, 62)
            elif event.code == 291:
                #Green
                print('Orbital Mechanics')
                play_clip(294, 148)
            elif event.code == 292:
                #Blue
                print('Apollo 8 Launch')
                play_clip(442, 221)
            elif event.code == 294:
                #Right Shoulder - White
                print('STS Launch')
                play_clip(653, 136)
            elif event.code == 289:
                #Left Trigger - Black
                print('STS Landing')
                play_clip(789, 53)
            elif event.code == 290:
                #Yellow
                print('Insight Landing')
                play_clip(852, 142)
            elif event.code == 293:
                #Red
                print('Moon Rocks')
                play_clip(944, 55)
            elif event.code == 295:
                #Right Trigger - Black
                print('ISS')
                play_clip(1049, 51)
            else:
                print('Do Nothing')  
        else: #right joysticks
            print('Player 2')
            if event.code == 299:
                #Joystick Left
                print('Baby Shark')
                play_clip(1100, 95)
            elif event.code == 296:
                #Joystick Right
                print('Minions Babarang')
                play_clip(1195, 39)
            elif event.code == 298:
                #Joystick Up
                print('Minions Happy')
                play_clip(1234, 233)
            elif event.code == 297:
                #Joystick Down
                print('Moana You\'re Welcome')
                play_clip(1467, 164)
            elif event.code == 289:
                #Left Shoulder - White
                print('Be Our Guest')
                play_clip(1631, 209)
            elif event.code == 291:
                #Green
                print('Ho Hey')
                play_clip(1840, 160)
            elif event.code == 293:
                #Blue
                print('Hakuna Matata')
                play_clip(2001, 230)
            elif event.code == 295:
                #Right Shoulder - White
                print('Moana - How Far I\'ll Go')
                play_clip(2231, 151)
            elif event.code == 288:
                #Left Trigger - Black
                print('Under The Sea')
                play_clip(2382, 197)
            elif event.code == 290:
                #Yellow
                print('Whistle While You Work')
                play_clip(2581, 216)
            elif event.code == 292:
                #Red
                print('Let It Go')
                play_clip(2795, 220)
            elif event.code == 294:
                #Right Trigger - Black
                print('Dad')
                play_clip(3051, 15)
            else:
                print('Do Nothing')  
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
