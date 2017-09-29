from retrogine.lib import *


@update
def update(delta):
    pass


@draw
def draw():
    cls()
    spr(0, 30, 30)
    spr(0, 50, 30)


retrogine(1000, 750, 16, 16, show_fps=True, enable_os_mouse=True, desired_fps=60)
