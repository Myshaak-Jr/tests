import re
from typing import Any


class Field(object):
    def __init__(self) -> None:
        self._field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    
    def __setitem__(self, index: list[int, int], obj: str, /) -> None:
        x, y = index
        self._field[y][x] = obj
    
    def __getitem__(self, index: list[int, int], /) -> str:
        x, y = index
        return self._field[y][x]

    def __str__(self) -> str:
        return "\n".join(["\n".join(a) for a in zip([f" {' | '.join(b)} " for b in self._field], ["---+---+---", "---+---+---", ""])])