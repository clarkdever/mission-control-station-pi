import mplayer

p = mplayer.Player()
p.loadfile('sample.mp4')
p.fullscreen = True
p.time_pos = 40
p.play()
p.quit()
