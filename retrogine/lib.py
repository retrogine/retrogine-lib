from typing import Callable, Tuple
import retrogine.data_loader as data_loader
from pygame.rect import Rect
from pyglet.clock import Clock
import pygame
import sys

_default_color = (0, 0, 0)
_update: Callable = None
_draw: Callable = None
_screen = None
_debug_font: pygame.font.Font = None
_last_debug_pos: Tuple = (0, 0)
_clock: Clock
_update_rate: int

(_sprites, _palettes) = data_loader.load_data_file('test.data')


def retrogine(
        window_width: int,
        window_height: int,
        update_rate: int = 30
):
    global _screen
    global _debug_font
    global _clock
    global _last_debug_pos
    global _update_rate
    _update_rate = update_rate

    pygame.init()

    _debug_font = pygame.font.SysFont("monospace", 15)

    size = window_width, window_height

    _screen = pygame.display.set_mode(size)

    _clock = Clock()
    _clock.schedule_interval(_update, 1 / update_rate)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        _last_debug_pos = (0, -_debug_font.get_height())
        _draw()
        pygame.display.flip()
        _clock.tick()
        # print(_clock.get_fps())


def fps() -> int:
    global _clock
    return int(_clock.get_fps())


def spr(sprite_number: int, x: int, y: int, palette_number=0):
    sprite = _sprites.get(sprite_number)
    surface = sprite.get_image(_palettes[palette_number])
    _screen.blit(surface, Rect(x, y, 16, 16))


def text(txt: str, color: Tuple = (255, 255, 255), position: Tuple = None):
    global _last_debug_pos
    if not position:
        position = (_last_debug_pos[0], _last_debug_pos[1] + _debug_font.get_height() + 1)
    _last_debug_pos = position

    label = _debug_font.render(str(txt), 1, color)
    _screen.blit(label, position)


def cls(color=_default_color):
    _screen.fill(color)


def update(func: Callable):
    global _update
    _update = func
    return func


def draw(func: Callable):
    global _draw
    _draw = func
    return func
