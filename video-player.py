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
1) implement with arcade buttons instead of keylisteners
"""

#initialize all the things
p = mplayer.Player()
p.loadfile('sharks.mp4')
p.fullscreen = True #make it fullscreen
p.ontop = True #place our video layer on top
p.pause()  #unpause the file, it loads paused
p.osdlevel = 0 #turn off on screen display
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
        elif key.char=='p':
            print('toggle pause')
            p.pause()
        elif key.char=='z':
            print('data dump')
            print('path: ', p.path)
            #print('stream_pos: ', p.stream_pos)
            #print('stream_start: ', p.stream_start)
            #print('stream_end: ', p.stream_end)
            #print('stream_length: ', p.stream_length)
            #print('stream_time_pos: ', p.stream_time_pos)
            print('length: ', p.length)
            print('time_pos: ', p.time_pos)
            print('percent_pos: ', p.percent_pos)
        elif key.char=='q':
            print('Sharks!')
            play_clip(5.75, 2)
            #p.time_pos = 5.75
        elif key.char=='w':
            print('Tiger Shark!')
            play_clip(20.55, 2)
            #p.time_pos = 20.55
        elif key.char=='e':
            print('Blue Fin Shark!!')
            #p.time_pos = 35
            play_clip(35, 2)
        elif key.char=='r':
            print('Thresher Shark!')
            #p.time_pos = 51
            play_clip(51, 2)
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
