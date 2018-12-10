from threading import Timer
import mplayer
from pynput import keyboard

"""
Clark Dever - clarkdever@gmail.com
12/10/2018

mplayer -list-properties will provide you a list of available properties
mplayer -input cmdlist will provide you a list of commands

IMPORTANT NOTE: The mplayer wrapper used here will only implement commands if there is not a property available that does the same thing

TODO:
1) Test on pi to see if mplayer loads videos fast enough
2) Figure out how to pause after a duration if it's not
2.1) If pausing after duration, reset time after each button press
3) implement with arcade buttons instead of keylisteners
"""

p = mplayer.Player()
p.loadfile('sample.mp4')
p.fullscreen = True
p.ontop = True
print('pause: ', p.pause)
p.pause = True
print('pause: ', p.pause)
print('file name:', p.path, "\n", 'clip length:', p.length)


def play_clip(position, duration):
    """Plays a clip starting at position for duration"""
    print('play_clip()')
    try:
        t = Timer(duration, p.pause())
        p.time_pos = position
        t.start()
    except:
        print('Play_Clip Exception {0} , {1}')

def pause():
    """Pauses play"""
    print('pause()')
    try:
        p.pause()
        print('Pause()')
    except:
        print('Pause Failed')
        
def on_press(key):
    """
    executes program flow based on keypresses
    """
    try:
        if key.char=='a':
            p.quit()
            quit()
        elif key.char=='s':
            print('load sharks.mp4')
            p.loadfile("sharks.mp4")
            p.fullscreen = True
        elif key.char=='d':
            print('load sample.mp4')
            p.loadfile("sample.mp4")
            p.fullscreen = True
        elif key.char=='f':
            p.fullscreen = not p.fullscreen
        else:
            print('alphanumeric key {0} pressed'.format(
                key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))

    if key == keyboard.Key.esc:
        # Stop listener so you can kill things from python console
        return False

# Collect events until released by hitting ESC
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
