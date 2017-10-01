from typing import Callable, Tuple, Dict
import retrogine.data_loader as data_loader
from pygame.surface import Surface
from pygame.rect import Rect
from pyglet.clock import Clock
import pygame
import sys


class ButtonMasks:
    UP = 1
    DOWN = 2
    LEFT = 4
    RIGHT = 8
    A = 16
    B = 32
    X = 64
    Y = 128
    TRIGGER_L1 = 256
    TRIGGER_L2 = 512
    TRIGGER_R1 = 1024
    TRIGGER_R2 = 2048
    START = 4096
    SELECT = 8192
    MENU = 16384

    key_codes: Dict[int, int] = {
        pygame.K_UP: UP,
        pygame.K_DOWN: DOWN,
        pygame.K_LEFT: LEFT,
        pygame.K_RIGHT: RIGHT,
        pygame.K_w: A,
        pygame.K_s: B,
        pygame.K_e: X,
        pygame.K_d: Y,
        pygame.K_q: TRIGGER_L1,
        pygame.K_a: TRIGGER_L2,
        pygame.K_r: TRIGGER_R1,
        pygame.K_f: TRIGGER_R1,
        pygame.K_RETURN: START,
        pygame.K_BACKSLASH: START,
        pygame.K_ESCAPE: MENU
    }


_default_color = (0, 0, 0)
_update: Callable = None
_draw: Callable = None
_real_screen: Surface = None
_screen: Surface = None
_debug_font: pygame.font.Font = None
_debug_surface: Surface = None
_last_debug_pos: Tuple = (0, 0)
_clock: Clock
_update_rate: int
_keys_down: int = 0

(_sprites, _palettes) = data_loader.load_data_file('test.data')


def retrogine(
        window_width: int,
        window_height: int,
        tiles_wide: int = 20,
        tiles_tall: int = 12,
        scale_size: int = 4,
        update_rate: int = 30,
        fullscreen: bool = False
):
    global _real_screen
    global _screen
    global _debug_font
    global _debug_surface
    global _clock
    global _last_debug_pos
    global _update_rate
    global _keys_down
    _update_rate = update_rate

    flags = pygame.DOUBLEBUF | pygame.HWSURFACE
    if fullscreen:
        flags |= pygame.FULLSCREEN

    pygame.init()
    pygame.mouse.set_visible(False)

    _debug_font = pygame.font.SysFont("monospace", 15)

    size = window_width, window_height

    _real_screen = pygame.display.set_mode(size, flags)
    _debug_surface = Surface(size).convert_alpha()

    _screen = Surface((tiles_wide * 16, tiles_tall * 16))
    scale_size = (tiles_wide * 16 * scale_size, tiles_tall * 16 * scale_size)
    x_off = (window_width - scale_size[0]) / 2
    if x_off < 0:
        x_off = 0
    y_off = (window_height - scale_size[1]) / 2
    if y_off < 0:
        y_off = 0
    screen_offset = (x_off, y_off)

    _clock = Clock()
    _clock.schedule_interval(_update, 1 / update_rate)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_game()
                else:
                    if event.key in ButtonMasks.key_codes:
                        retro_button_code = ButtonMasks.key_codes[event.key]
                        _keys_down |= retro_button_code
            elif event.type == pygame.KEYUP:
                if event.key in ButtonMasks.key_codes:
                    retro_button_code = ButtonMasks.key_codes[event.key]
                    _keys_down &= ~retro_button_code

        _draw()

        _real_screen.fill((0, 255, 0))
        _real_screen.blit(pygame.transform.scale(_screen, scale_size), screen_offset)
        _real_screen.blit(_debug_surface, (0, 0))

        pygame.display.flip()
        _clock.tick()


def quit_game():
    pygame.quit()
    sys.exit()


def btns():
    global _keys_down
    return _keys_down


def btn(key_id: int):
    global _keys_down
    return _keys_down & key_id == key_id


def fps() -> int:
    global _clock
    return int(_clock.get_fps())


def spr(sprite_number: int, x: int, y: int, palette_number=0):
    sprite = _sprites.get(sprite_number)
    surface = sprite.get_image(_palettes[palette_number])
    _screen.blit(surface, Rect(x, y, 16, 16))


def debug(txt: str, color: Tuple = (255, 255, 255), position: Tuple = None):
    global _last_debug_pos
    if not position:
        position = (_last_debug_pos[0], _last_debug_pos[1] + _debug_font.get_height() + 1)
    _last_debug_pos = position

    label = _debug_font.render(txt, 0, color)
    _debug_surface.blit(label, position)


def cls(color=_default_color):
    global _last_debug_pos

    _screen.fill(color)
    _last_debug_pos = (0, -_debug_font.get_height())
    _debug_surface.fill((0, 0, 0, 0))


def update(func: Callable):
    global _update
    _update = func
    return func


def draw(func: Callable):
    global _draw
    _draw = func
    return func
