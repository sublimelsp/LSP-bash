from enum import Enum, IntEnum as IntEnum, IntFlag as IntFlag

class StrEnum(str, Enum):
    """
        Naive polyfill for Python 3.11's StrEnum.

        See https://docs.python.org/3.11/library/enum.html#enum.StrEnum
        """
    __format__ = ...
    __str__ = ...
