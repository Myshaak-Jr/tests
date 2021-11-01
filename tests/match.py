class Color:
    def __init__(self, r: int, g: int, b: int):
        self._r = r
        self._g = g
        self._b = b

    @staticmethod
    def _setter(func):
        def inner(self, value: int):
            match value:
                case v if type(v) == int and 0 <= v < 256:
                    func(self, value)
                case int():
                    raise ValueError(f"Value must be integer in range 0 to 255, got {value}")
                case _:
                    raise ValueError(f"Expected int, not ({type(value)})")
        inner.__name__ = func.__name__
        return inner

    @property
    def r(self):
        return self._r

    @r.setter
    @_setter
    def r(self, value):
        self._r = value

    @property
    def g(self, value):
        return self._g
    
    @g.setter
    @_setter
    def g(self):
        self._g = value

    @property
    def b(self):
        return self._b

    @b.setter
    @_setter
    def b(self, value):
        self._b = value

    __match_args__: tuple = ("_r", "_g", "_b")

    def __format__(self, format_spec: str) -> str:
        return format_spec.replace("%r", f"{self.r}").replace("%g", f"{self.g}").replace("%b", f"{self.b}").replace("%x", f"#{self.r:0>2x}{self.g:0>2x}{self.b:0>2x}").replace("%X", f"#{self.r:0>2X}{self.g:0>2X}{self.b:0>2X}")

def nextColor(color: Color):
    match color:
        case Color(255, g, 0) if g < 255:
            color.g += 1
        case Color(r, 255, 0) if 0 < r <= 255:
            color.r -= 1
        case Color(0, 255, b) if b < 255:
            color.b += 1
        case Colot(0, g, 255) if 0 < g <= 255:
            color.g -= 1
        case Color(r, 0, 255) if r < 255:
            color.r += 1
        case Color(255, 0, b) if 0 < b <= 255:
            color.b -= 1

def ctrl(color: Color) -> None:
    match color:
        case Color(0, 0, 0):
            print("Color is black.")
        case Color(255, 255, 255):
            print("Color is white.")
        case Color(r, g, b) if r == g == b:
            print("Color is gray.")
        case Color(r, 0, 0):
            print(f"Color is red. ({color:%x})")
        case Color(0, g, 0):
            print(f"Color is green. ({color:%x})")
        case Color(0, 0, b):
            print(f"Color is blue. ({color:%x})")
        case Color():
            print(f"Color is a random color. ({color:%x})")
        case _:
            raise ValueError(f"Expected instance of Color, not {type(color)}")

