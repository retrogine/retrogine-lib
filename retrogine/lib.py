from typing import List, Callable

import pyglet
from pyglet.window import FPSDisplay

from retrogine.data_loader import load_data_file, NoSpriteException, NoPaletteException


pyglet.gl.glEnable(pyglet.gl.GL_TEXTURE_2D)
pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MAG_FILTER, pyglet.gl.GL_NEAREST)

(sprites, palettes) = load_data_file('test.data')

_window: pyglet.window.Window = None
_number_cols = -1
_number_rows = -1
_show_fps = False
_desired_fps: int
_fps_display: FPSDisplay = None
_update: Callable = None
_draw: Callable = None


def retrogine(
        window_width: int,
        window_height: int,
        number_columns: int = 16,
        number_rows: int = 15,
        fullscreen=False,
        show_fps: bool = False,
        desired_fps: int = 30,
        enable_os_mouse: bool = False
):
    global _window
    global _number_cols
    global _number_rows
    global _show_fps
    global _desired_fps
    global _fps_display

    _window = pyglet.window.Window(width=window_width, height=window_height, resizable=False, fullscreen=fullscreen)

    if not enable_os_mouse:
        _window.set_exclusive_mouse()

    _number_cols = number_columns
    _number_rows = number_rows
    _show_fps = show_fps
    _desired_fps = desired_fps
    if show_fps:
        # _fps_display = FPSDisplay(_window)
        _fps_display = pyglet.clock.ClockDisplay()

    pyglet.clock.schedule_interval(_update, 1 / 60.0)

    @_window.event
    def on_draw():
        global _to_blit
        _draw()

        if show_fps:
            _fps_display.draw()

    pyglet.app.run()


def spr(sprite_number: int, x: int, y: int, palette_number=0):
    if sprite_number not in sprites:
        raise NoSpriteException('No sprite for id: {}'.format(sprite_number))
    if len(palettes) <= palette_number:
        raise NoPaletteException('No palette for index: {}'.format(palette_number))

    sprite = sprites[sprite_number]
    image = sprite.get_image(palettes[palette_number])
    image.blit(x, y, 0, 16, 16)


def cls():
    _window.clear()


def update(func: Callable):
    global _update
    _update = func
    return func


def draw(func: Callable):
    global _draw
    _draw = func
    return func
