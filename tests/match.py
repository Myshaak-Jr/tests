class Color:
    r: int
    g: int
    b: int

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    __match_args__: tuple = ("r", "g", "b")

    def __format__(self, format_spec: str) -> str:
        return format_spec.replace("%r", f"{self.r}").replace("%g", f"{self.g}").replace("%b", f"{self.b}").replace("%x", f"#{self.r:0>2x}{self.g:0>2x}{self.b:0>2x}").replace("%X", f"#{self.r:0>2X}{self.g:0>2X}{self.b:0>2X}")

def ctrl(color: Color) -> None:
    match color:
        case Color(0, 0, 0):
            print("Color is black")
        case Color(255, 255, 255):
            print("Color is white")
        case Color(r, g, b) if r == g == b:
            print("Color is gray")
        case Color(r, 0, 0):
            print(f"Color is red ({r = :0>2x})")
        case Color(0, g, 0):
            print(f"Color is red ({g = :0>2x})")
        case Color(0, 0, b):
            print(f"Color is red ({b = :0>2x})")
            