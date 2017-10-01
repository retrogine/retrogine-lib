from retrogine.lib import *
import retrogine.button_masks as button_masks

p_x = 0
p_y = 0
d = 0


@update
def update(delta):
    global p_x
    global p_y
    global d
    d = delta

    if btn(button_masks.UP):
        p_y = p_y - 1
    if btn(button_masks.DOWN):
        p_y = p_y + 1

    if btn(button_masks.LEFT):
        p_x = p_x - 1
    if btn(button_masks.RIGHT):
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
    text(str(fps()))
    text(str(d))
    text(str(btns()))
    text("UP:{} DOWN:{} LEFT:{} RIGHT:{}".format(btn(button_masks.UP), btn(button_masks.DOWN), btn(button_masks.LEFT),
                                                 btn(button_masks.RIGHT)))


retrogine(1280, 720, fullscreen=False)
# retrogine(1280, 720)
