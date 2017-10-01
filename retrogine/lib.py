from typing import Callable, Tuple
import retrogine.data_loader as data_loader
from pygame.surface import Surface
from pygame.rect import Rect
from pyglet.clock import Clock
import pygame
import sys

_default_color = (0, 0, 0)
_update: Callable = None
_draw: Callable = None
_real_screen: Surface = None
_screen: Surface = None
_debug_font: pygame.font.Font = None
_last_debug_pos: Tuple = (0, 0)
_clock: Clock
_update_rate: int

(_sprites, _palettes) = data_loader.load_data_file('test.data')


def retrogine(
        window_width: int,
        window_height: int,
        tiles_wide: int = 16,
        tiles_tall: int = 15,
        update_rate: int = 30,
        fullscreen: bool = False
):
    global _real_screen
    global _screen
    global _debug_font
    global _clock
    global _last_debug_pos
    global _update_rate
    _update_rate = update_rate

    flags = pygame.DOUBLEBUF | pygame.HWSURFACE
    if fullscreen:
        flags |= pygame.FULLSCREEN

    pygame.init()

    _debug_font = pygame.font.SysFont("monospace", 15)

    size = window_width, window_height

    _real_screen = pygame.display.set_mode(size, flags)
    _screen = Surface((tiles_wide * 16, tiles_tall * 16))
    scale_size = (window_width - (window_width % 16), window_height - (window_height % 16))
    screen_offset = ((window_width % 16) / 2, (window_height % 16) / 2)

    _clock = Clock()
    _clock.schedule_interval(_update, 1 / update_rate)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        _last_debug_pos = (0, -_debug_font.get_height())
        _draw()

        # _real_screen.blit(_screen, (0, 0))
        # rect = Rect((0, 0), )
        _real_screen.fill((255, 0, 0))
        _real_screen.blit(pygame.transform.scale(_screen, scale_size), screen_offset)

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

    label = _debug_font.render(str(txt), 0, color)
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
