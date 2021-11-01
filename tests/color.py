import re
from typing import Tuple
from pipe import permutations


__all__ = ["Color"]

colors = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "gray": (127, 127, 127),
    "red": (255, 0, 0),
    "orange": (255, 127, 0),
    "yellow": (255, 255, 0),
    "chartreuse": (127, 255, 0),
    "green": (0, 255, 0),
    "spring": (0, 255, 127),
    "cyan": (0, 255, 255),
    "azure": (0, 127, 255),
    "blue": (0, 0, 255),
    "violet": (127, 0, 255),
    "magenta": (255, 0, 255),
    "rose": (255, 0, 127)
}

class Color:
    def __init__(self, *args) -> None:
        match args:
            case (r, g, b):
                self.r = r
                self.g = g
                self.b = b
            case (color,):
                self.r, self.g, self.b = colors[color.lower()]

    def __getattr__(self, attr):
        if tuple(attr) not in list("rgb" | permutations) + list("rgb" | permutations(2)):
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{attr}'")
        return tuple(getattr(self, color) for color in attr)

    def __setattr__(self, attr: str, values: tuple):
        if tuple(attr) not in list("rgb" | permutations) + list("rgb" | permutations(2)):
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{attr}'")
        return tuple(setattr(self, color, value) for color, value in zip(list(attr), values))

    @staticmethod
    def _setter(func):
        def inner(self, value: int):
            match value:
                case int(v) if 0 <= v < 256:
                    func(self, value)
                case int():
                    raise ValueError(f"Value must be integer in range 0 to 255, got {value}")
                case _:
                    raise ValueError(f"Expected int, not ({type(value)})")
        inner.__name__ = func.__name__
        return inner

    @property
    def r(self) -> int:
        return self._r

    @r.setter
    @_setter
    def r(self, value: int) -> None:
        self._r = value

    @property
    def g(self) -> int:
        return self._g
    
    @g.setter
    @_setter
    def g(self, value: int) -> None:
        self._g = value

    @property
    def b(self) -> int:
        return self._b

    @b.setter
    @_setter
    def b(self, value: int) -> None:
        self._b = value

    __match_args__: tuple = ("r", "g", "b")

    def __format__(self, format_spec: str) -> str:
        if re.search("%[rgbx]", format_spec) is None:
            match format_spec:
                case "x":
                    return f"{self:%x}"
                case "r":
                    return f"{self.r}"
                case "g":
                    return f"{self.g}"
                case "b":
                    return f"{self.b}"
                case "":
                    return str(self)
                case _:
                    raise ValueError(f"Invalid format specifier: {format_spec}")

        return format_spec.replace("%r", f"{self.r}").replace("%g", f"{self.g}").replace("%b", f"{self.b}").replace("%x", f"#{self.r:0>2x}{self.g:0>2x}{self.b:0>2x}").replace("%X", f"#{self.r:0>2X}{self.g:0>2X}{self.b:0>2X}")

    def __rshift__(self, count):
        for _ in range(count):
            match self:
                case Color(255, g, 0) if g < 255:
                    self.g += 1
                case Color(r, 255, 0) if 0 < r <= 255:
                    self.r -= 1
                case Color(0, 255, b) if b < 255:
                    self.b += 1
                case Color(0, g, 255) if 0 < g <= 255:
                    self.g -= 1
                case Color(r, 0, 255) if r < 255:
                    self.r += 1
                case Color(255, 0, b) if 0 < b <= 255:
                    self.b -= 1
    
    def __lshift__(self, count):
        for _ in range(count):
            match self:
                case Color(255, 0, b) if b < 255:
                    self.b += 1
                case Color(r, 0, 255) if 0 < r <= 255:
                    self.r -= 1
                case Color(0, g, 0) if g < 255:
                    self.g += 1
                case Color(0, 255, b) if 0 < b <= 255:
                    self.b -= 1
                case Color(r, 255, 0) if r < 255:
                    self.r += 1
                case Color(255, g, 0) if 0 < g <= 255:
                    self.g -= 1

    def __str__(self) -> str:
        match self:
            case Color(0, 0, 0):
                return "black"
            case Color(255, 255, 255):
                return "white"
            case Color(r, g, b) if r == g == b:
                return "gray"
            case Color(255, g, b) if abs(g - b) < 64:
                return "red"
            case Color(255, g, 0) if abs(127 - g) < 64:
                return "orange"
            case Color(r, g, 0) if abs(r - g) < 64:
                return "yellow"
            case Color(r, 255, 0) if abs(127 - r) < 64:
                return "chartreuse"
            case Color(r, 255, b) if abs(r - b) < 64:
                return "green"
            case Color(0, 255, b) if abs(127 - b) < 64:
                return "spring"
            case Color(0, g, b) if abs(g - b) < 64:
                return "cyan"
            case Color(0, g, 255) if abs(127 - g) < 64:
                return "azure"
            case Color(r, g, 255) if abs(r - g) < 64:
                return "blue"
            case Color(r, 0, 255) if abs(127 - r) < 64:
                return "violet"
            case Color(r, 0, b) if abs(r - b) < 64:
                return "magenta"
            case Color(255, 0, b) if abs(127 - b) < 64:
                return "rose"
            case Color():
                raise NotImplementedError(f"Color {self:x} is not supported yet.")
    
    def __repr__(self):
        return f"Color({self:r=%r, g=%g, b=%b})"
