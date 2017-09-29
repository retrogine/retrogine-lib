from typing import Tuple

from retrogine.exceptions import *
from retrogine.model import *


def load_data_file(path) -> Tuple[Dict[int, DataSprite], List[DataPalette]]:
    state = None
    version = None

    palettes = []
    sprites = {}

    current_sprite_number: int = None
    current_sprite = []

    with open(path, mode='r') as data_file:
        for line in data_file:
            line = line.rstrip()
            if state is None:
                if not line.startswith('retrogine data '):
                    raise DataParserException("expected header to start with 'retrogine data ' and then a version")
                state = "[header]"
                version = line.split(' ')[-1]
            if line.startswith('['):
                if state == '[sprites]' or len(current_sprite) > 0:
                    if current_sprite_number is None:
                        raise DataParserException("sprites must have an id specified")
                    sprites[current_sprite_number] = DataSprite(current_sprite_number, current_sprite)
                    current_sprite = []
                    current_sprite_number = None

                state = line
            else:
                if state == '[palettes]':
                    pal_colors = line.split(' ')
                    length = len(pal_colors)
                    if length != 16:
                        raise DataParserException('palettes should have exactly 16 colors but had: {}'.format(length))

                    colors = []
                    for pal_color in pal_colors:
                        color_data = [int(x) for x in pal_color.split(',')]
                        length = len(color_data)
                        if length != 4:
                            raise DataParserException('palette color values should have exactly four elements (RGBA) but had: {}'.format(length))

                        color = Color(color_data[0], color_data[1], color_data[2], color_data[3])
                        colors.append(color)

                    palette = DataPalette(len(palettes), colors)
                    palettes.append(palette)
                elif state == '[sprites]':
                    if line.startswith('id='):
                        current_sprite_number = int(line.split('=', 2)[1])
                    else:
                        split = line.split(' ')
                        if len(split) != 16:
                            raise InvalidSpriteSizeException('sprite should be exactly 16 wide')

                        for number in split:
                            value = int(number)
                            if value < 0 or value > 15:
                                raise InvalidSpriteValueException('sprite values must be between 0 and 15 inclusive')
                            current_sprite.append(value)

    if len(current_sprite) > 0:
        if current_sprite_number is None:
            raise DataParserException("sprites must have an id specified")
        sprites[current_sprite_number] = DataSprite(current_sprite_number, current_sprite)

    print("Loaded Version " + version)
    return sprites, palettes


if __name__ == '__main__':
    (sprites, palettes) = load_data_file('../test.data')
    print(sprites[0].apply_palette(palettes[0]))
