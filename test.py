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

    for y in range(12):
        for x in range(20):
            spr(1, x * 16, y * 16, (x + y) % 2)

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
    text(str(fps()))
    text(str(d))


retrogine(1280, 720, fullscreen=False)
# retrogine(1280, 720)
