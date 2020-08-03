import mplayer, evdev

# Joystics
pl1 = evdev.InputDevice('/dev/input/by-path/platform-3f980000.usb-usb-0:1.5:1.0-event-joystick')
pl2 = evdev.InputDevice('/dev/input/by-path/platform-3f980000.usb-usb-0:1.3:1.0-event-joystick')
 
# Initialize video
p = mplayer.Player()
p.loadfile("ChildrensMCS.mp4")
p.fullstrceen = True
p.loop = 0
p.osdlevel = 0 # Disables on-screen UI

scrub_speed = 5 # How many seconds skipping ahead/back
playhead = p.time_pos
playhead_dirty = False
vid_length = p.length

# Player inputs
stick = {
        'UP': 297,
        'DOWN': 296,
        'LEFT': 299,
        'RIGHT': 298,
        'LWHITE': 290,
        'LBLACK': 288,
        'GREEN': 291,
        'YELLOW': 289,
        'BLUE': 292,
        'RED': 293,
        'RWHITE': 294,
        'RBLACK': 295
        }

# Dictionary of clips
clips = {
        'Solar System': {
            'start': 0,
            'length': 232
            },
        'Mission Control': {
            'start': 233,
            'length': 62
            },
        'Orbital Mechanics': {
            'start': 294,
            'length': 148
            },
        'Apollo 8 Launch': {
            'start': 442,
            'length': 221
            },
        'STS Launch': {
            'start': 654,
            'length': 136
            },
        'STS Landing': {
            'start': 789,
            'length': 53
            },
        'Insight Landing': {
            'start': 852,
            'length': 142
            },
        'Moon Rocks': {
            'start': 994,
            'length': 55
            },
        'ISS': {
            'start': 1049,
            'length': 51
            },
        'Baby Shark': {
            'start': 1100,
            'length': 95
            },
        'Minions Babarang': {
            'start': 1196,
            'length': 39
            },
        'Minions Happy': {
            'start': 1235,
            'length': 233
            },
        'Moana - You\'re Welcome': {
            'start': 1467,
            'length': 164
            },
        'Be Our Guest': {
            'start': 1631,
            'length': 209
            },
        'Ho Hey': {
            'start': 1840,
            'length': 160
            },
        'Hakuna Matata': {
            'start': 2001,
            'length': 230
            },
        'Moana - How Far I\'ll Go': {
            'start': 2231,
            'length': 151
            },
        'Under The Sea': {
            'start': 2382,
            'length': 197
            },
        'Whistle While You Work': {
            'start': 2581,
            'length': 216
            },
        'Let It Go': {
            'start': 2795,
            'length': 220
            },
        'Dad': {
            'start': 3051,
            'length': 15
            }
        }


clip_end = clips['Solar System']['length']


def scrub(val):
    global playhead
    global playhead_dirty
    global vid_length
    if playhead is None or vid_length is None:
        return # mplayer's time_pos is None when spinning up the process/loading the video
    x = playhead + val
    if x < 0: 
        playhead = vid_length + x
    if x > vid_length:
        playhead = 0 + (x - vid_length)
    else:
        playhead += val 
    playhead_dirty = True


def pause():
    p.pause()


def play_clip(clip):
    global playhead
    global playhead_dirty
    global clip_end
    try:
        playhead = clips[clip]['start']
        playhead_dirty = True
    except:
        print("Error playing clip", clip)

def print_btn(btn):
    print(btn.name)

def poll_input():
    ev1 = pl1.read_one()
    ev2 = pl2.read_one()
    #if ev1 is not None:
    while True:
        ev1 = pl1.read_one()
        if ev1 is None:
            break # No more input, so break out of the loop
        # Do player 1 stuff here
        if ev1.type == 1 and ev1.value == 1: # Button Input
            if ev1.code == stick['LEFT']:
                scrub(-scrub_speed)
            if ev1.code == stick['RIGHT']:
                scrub(scrub_speed)
            if ev1.code == stick['UP']:
                pause()
            if ev1.code == stick['DOWN']:
                play_clip('Solar System')
            if ev1.code == stick['LWHITE']:
                play_clip('Mission Control')
            if ev1.code == stick['GREEN']:
                play_clip('Orbital Mechanics')
            if ev1.code == stick['BLUE']:
                play_clip('Apollo 8 Launch')
            if ev1.code == stick['RWHITE']:
                play_clip('STS Launch')
            if ev1.code == stick['LBLACK']:
                play_clip('STS Landing')
            if ev1.code == stick['YELLOW']:
                play_clip('Insight Landing')
            if ev1.code == stick['RED']:
                play_clip('Moon Rocks')
            if ev1.code == stick['RBLACK']:
                play_clip('ISS')
    while True:
        ev2 = pl2.read_one()
        if ev2 is None:
            break
        # Do player 2 stuff here
        if ev2.type == 1 and ev2.value == 1:
            if ev2.code == stick['LEFT']:
                play_clip('Baby Shark')
            if ev2.code == stick['RIGHT']:
                play_clip('Minions Babarang')
            if ev2.code == stick['UP']:
                play_clip('Minions Happy')
            if ev2.code == stick['DOWN']:
                play_clip('Moana - You\'re Welcome')
            if ev2.code == stick['LWHITE']:
                play_clip('Be Our Guest')
            if ev2.code == stick['GREEN']:
                play_clip('Ho Hey')
            if ev2.code == stick['BLUE']:
                play_clip('Hakuna Matata')
            if ev2.code == stick['RWHITE']:
                play_clip('Moana - How Far I\'ll Go')
            if ev2.code == stick['LBLACK']:
                play_clip('Under The Sea')
            if ev2.code == stick['YELLOW']:
                play_clip('Whistle While You Work')
            if ev2.code == stick['RED']:
                play_clip('Let It Go')
            if ev2.code == stick['RBLACK']:
                play_clip('Dad')


while True:
    if not p.fullscreen:
        p.fullscreen = True
    poll_input()
    if vid_length is None:
        vid_length = p.length
    if playhead_dirty:
        p.time_pos = playhead
        playhead_dirty = False
    else:
        playhead = p.time_pos

