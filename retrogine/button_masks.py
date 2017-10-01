from typing import Dict

import pygame

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