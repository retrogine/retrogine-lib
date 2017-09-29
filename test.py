from retrogine.lib import *

i = 0

@update
def update(delta):
    pass


@draw
def draw():
    global i
    i = i + 1
    i = i % 140
    cls()
    spr(0, 100, 100, 0)
    spr(0, 120, 100, 0)
    spr(0, 140, 100, 0)
    spr(0, 160, 100, 0)
    spr(0, 180, 100, 0)
    spr(0, 200, 100, 0)
    spr(0, 80 + i, 100, 1)



retrogine(1000, 750, 16, 16, show_fps=True, enable_os_mouse=True, desired_fps=60)
