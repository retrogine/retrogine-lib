from retrogine.lib import *

p_x = 0
p_y = 0
d = 0


@update
def update(delta):
    global p_x
    global p_y
    global d
    d = delta

    if btn(Buttons.UP):
        p_y = p_y - 1
    if btn(Buttons.DOWN):
        p_y = p_y + 1

    if btn(Buttons.LEFT):
        p_x = p_x - 1
    if btn(Buttons.RIGHT):
        p_x = p_x + 1


@draw
def draw():
    global p_x
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
    spr(0, p_x, p_y, 1)
    debug(str(fps()))
    debug(str(d))
    debug(str(btns()))
    debug("UP:{} DOWN:{} LEFT:{} RIGHT:{}".format(btn(Buttons.UP), btn(Buttons.DOWN), btn(Buttons.LEFT), btn(Buttons.RIGHT)))
    debug("A:{} B:{} X:{} Y:{}".format(btn(Buttons.A), btn(Buttons.B), btn(Buttons.X), btn(Buttons.Y)))
    debug("L1:{} L2:{} R1:{} R2:{}".format(btn(Buttons.L1), btn(Buttons.L2), btn(Buttons.R1), btn(Buttons.R2)))
    debug("Start:{} Select:{}".format(btn(Buttons.START), btn(Buttons.SELECT)))


retrogine(1280, 720, fullscreen=False)
# retrogine(1280, 720)
