from retrogine.lib import *

p_x = 0
p_y = 0
d = 0
palette = 0
was_down = False


@update
def update(delta):
    global was_down
    global p_x
    global p_y
    global d
    global palette
    d = delta

    if btn(Buttons.UP):
        p_y = p_y - 1
    if btn(Buttons.DOWN):
        p_y = p_y + 1

    if btn(Buttons.LEFT):
        p_x = p_x - 1
    if btn(Buttons.RIGHT):
        p_x = p_x + 1

    if btn(Buttons.A):
        if not was_down:
            was_down = True
            palette = palette + 1
    else:
        if was_down:
            was_down = False


@draw
def draw():
    global p_x
    cls()

    # for y in range(12):
    #     for x in range(20):
    #         spr(1, x * 16, y * 16, (x + y) % 2)

    spr(0, 100, 100, (palette + 0) % 2)
    spr(0, 120, 100, (palette + 1) % 2)
    spr(0, 140, 100, (palette + 0) % 2)
    spr(0, 160, 100, (palette + 1) % 2)
    spr(0, 180, 100, (palette + 0) % 2)
    spr(0, 200, 100, (palette + 1) % 2)
    spr(1, p_x, p_y, (palette + 0) % 2)
    debug(str(fps()))
    debug(str(d))
    debug(str(btns()))
    debug("UP:{} DOWN:{} LEFT:{} RIGHT:{}".format(btn(Buttons.UP), btn(Buttons.DOWN), btn(Buttons.LEFT), btn(Buttons.RIGHT)))
    debug("A:{} B:{} X:{} Y:{}".format(btn(Buttons.A), btn(Buttons.B), btn(Buttons.X), btn(Buttons.Y)))
    debug("L1:{} L2:{} R1:{} R2:{}".format(btn(Buttons.L1), btn(Buttons.L2), btn(Buttons.R1), btn(Buttons.R2)))
    debug("Start:{} Select:{}".format(btn(Buttons.START), btn(Buttons.SELECT)))


retrogine(1280, 720, fullscreen=False)
# retrogine(1280, 720)
