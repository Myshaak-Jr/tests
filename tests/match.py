from typing import Tuple


Color = Tuple[int, int, int]

class Tractor:
    color: Color
    def __init__(self, color: Color) -> None:
        self.color = color


def controlColor(tractor: Tractor) -> None:
    match tractor:
        case Tractor((0, 0, 0)):
            print("Tractor is black.")
        case Tractor((255, 255, 255)):
            print("Tractor is white.")
        case Tractor((r, g, b)) if r == g == b:
            print("Tractor is gray.")
        case Tractor((r, g, b)) if g == b == 0:
            print("Tractor is red.")
        case Tractor((r, g, b)) if r == b == 0:
            print("Tractor is green.")
        case Tractor((r, g, b)) if r == g == 0:
            print("Tractor is blue.")