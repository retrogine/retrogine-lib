from typing import List, Dict

import pygame
import pygame.surface

from retrogine.exceptions import InvalidSpriteSizeException


class Color:
    def __init__(self, red: int, green: int, blue: int, alpha: int):
        if red < 0 or red > 255 or green < 0 or green > 255 or blue < 0 or blue > 255 or alpha < 0 or alpha > 255:
            raise Exception("red, green, blue, alpha values must be between 0 and 255 inclusive")
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha


class DataPalette:
    def __init__(self, palette_number, data: List[Color]):
        self.palette_number = palette_number
        if len(data) != 16:
            raise Exception("Palette must have exactly 16 colors")
        self.data = data


class DataSprite:
    def __init__(self, number: int, data: List[int]):
        if len(data) != 16 * 16:
            raise InvalidSpriteSizeException('sprite should be exactly 16x16 ({}) but was {}'.format(16*16, len(data)))
        self.data: List[int] = data
        self._cache: Dict[str, pygame.surface.Surface] = {}
        self._number: int = number

    def get_image(self, palette: DataPalette) -> pygame.surface.Surface:
        if palette.palette_number in self._cache:
            return self._cache[palette.palette_number]

        surface = pygame.Surface((16, 16)).convert_alpha()
        count = 0
        for datum in self.data:
            x = int(count % 16)
            y = int(count / 16)

            color = palette.data[datum]
            surface.set_at((x, y), pygame.Color(color.red, color.green, color.blue, color.alpha))

            count += 1

        self._cache[palette.palette_number] = surface
        return surface
