from retrogine.lib import *

i = 0
d = 0


@update
def update(delta):
    global i
    global d
    d = delta
    i = i + 1
    i = i % 140


@draw
def draw():
    global i
    cls()
    spr(0, 0, 0, 0)
    spr(0, 100, 100, 0)
    spr(0, 120, 100, 0)
    spr(0, 140, 100, 0)
    spr(0, 160, 100, 0)
    spr(0, 180, 100, 0)
    spr(0, 200, 100, 0)
    spr(0, 80 + i, 100, 1)
    text(fps())
    text(d)


retrogine(1000, 750)
