class BaseException(Exception):
    def __init__(self, message):
        super(BaseException, self).__init__(message)


class DataParserException(BaseException):
    def __init__(self, message):
        super(DataParserException, self).__init__(message)


class InvalidSpriteSizeException(BaseException):
    def __init__(self, message):
        super(InvalidSpriteSizeException, self).__init__(message)


class InvalidSpriteValueException(BaseException):
    def __init__(self, message):
        super(InvalidSpriteValueException, self).__init__(message)


class NoSpriteException(BaseException):
    def __init__(self, message):
        super(NoSpriteException, self).__init__(message)

class NoPaletteException(BaseException):
    def __init__(self, message):
        super(NoPaletteException, self).__init__(message)
