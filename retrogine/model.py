from typing import List, Dict

import pyglet
from pyglet.image import ImageData

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
    def __init__(self, data: List[int]):
        if len(data) != 16*16:
            raise InvalidSpriteSizeException('sprite should be exactly 16x16')
        self.data = data
        self._cache: Dict[str, ImageData] = {}

    def _apply_palette(self, palette: DataPalette):
        result = []
        for datum in self.data:
            color = palette.data[datum]
            result.insert(0, color.alpha)
            result.insert(0, color.blue)
            result.insert(0, color.green)
            result.insert(0, color.red)
        return bytes(result)

    def get_image(self, palette: DataPalette) -> ImageData:
        if palette.palette_number in self._cache:
            return self._cache[palette.palette_number]

        raw_data = self._apply_palette(palette)

        texture = pyglet.image.Texture.create(16, 16)
        image = texture.get_image_data()
        image.set_data('RGBA', 4 * image.width, raw_data)

        self._cache[palette.palette_number] = image
        return image
