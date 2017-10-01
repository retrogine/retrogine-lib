from typing import Callable
import retrogine.data_loader as data_loader
from pygame.rect import Rect
import pygame.time
import pygame
import sys

_default_color = (0, 0, 0)
_update: Callable = None
_draw: Callable = None
_screen = None

(_sprites, _palettes) = data_loader.load_data_file('test.data')


def retrogine(
        window_width: int,
        window_height: int
):
    global _screen
    pygame.init()

    size = window_width, window_height

    _screen = pygame.display.set_mode(size)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        _update(clock.tick())
        _draw()
        pygame.display.flip()


def spr(sprite_number: int, x: int, y: int, palette_number=0):
    sprite = _sprites.get(sprite_number)
    surface = sprite.get_image(_palettes[palette_number])
    _screen.blit(surface, Rect(x, y, 16, 16))


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
