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

    for j in range(16):
        spr(1, j * 16, 0, j % 2)
        spr(1, j * 16, 14*16, j % 2)

    for j in range(15):
        spr(1, 0, j * 16, j % 2)
        spr(1, 15 * 16, j * 16, (j+1) % 2)

    spr(1, 16, 0, 1)
    spr(1, 32, 0, 0)
    spr(1, 48, 0, 1)
    spr(0, 100, 100, 0)
    spr(0, 120, 100, 0)
    spr(0, 140, 100, 0)
    spr(0, 160, 100, 0)
    spr(0, 180, 100, 0)
    spr(0, 200, 100, 0)
    spr(0, 80 + i, 100, 1)
    text(fps())
    text(d)


retrogine(1280, 720)
