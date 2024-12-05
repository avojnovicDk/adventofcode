from collections import UserList
from typing import Callable


class StringMatrix(UserList):
    def get_char_in_dir(self, x: int, y: int, dir_x: int, dir_y: int, no_of_steps: int = 1) -> str:
        x, y = x + dir_x * no_of_steps, y + dir_y * no_of_steps
        if 0 <= x < len(self) and 0 <= y < len(self[0]):
            return self[x][y]
        
    def count_from_starting(self, starting_char: str, count: Callable) -> int:
        return sum(
            count(self, x, y)
            for x in range(len(self))
            for y in range(len(self[0]))
            if self[x][y] == starting_char
        )