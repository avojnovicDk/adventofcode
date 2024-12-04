from typing import Callable
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_file_path, get_input


def _get_char_in_dir(lines: list[str], x: int, y: int, dir_x: int, dir_y: int):
        x, y = x + dir_x, y + dir_y
        if 0 <= x < len(lines) and 0 <= y < len(lines[0]):
            return lines[x][y]


class XmasCounter:
    def __init__(self, starting_char: str, count: Callable):
        self.starting_char = starting_char
        self.count = count

    def __call__(self, lines: list[str]):
        return sum(
            self.count(lines, x, y)
            for x in range(len(lines))
            for y in range(len(lines[0]))
            if lines[x][y] == self.starting_char
        )


@register_solution(2024, 4, 1)
def part_one(input_file_path: str):
    frame = (
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1),
    )

    count = lambda lines, x, y: sum(
        1
        for dir_x, dir_y in frame
        if (
            _get_char_in_dir(lines, x, y, dir_x, dir_y) == "M"
            and _get_char_in_dir(lines, x + dir_x, y + dir_y, dir_x, dir_y) == "A"
            and _get_char_in_dir(lines, x + 2 * dir_x, y + 2 * dir_y, dir_x, dir_y) == "S"
        )
    )
    
    return XmasCounter("X", count)(get_input(input_file_path))


@register_solution(2024, 4, 2)
def part_two(input_file_path: str):
    crosses = (
        ((-1, -1), (1,  1),),
        ((-1,  1), (1, -1),),
    )

    count = lambda lines, x, y: 1 if all(
        set(_get_char_in_dir(lines, x, y, dir_x, dir_y) for dir_x, dir_y in cross) == {"M", "S"}
        for cross in crosses
    ) else 0
    
    return XmasCounter("A", count)(get_input(input_file_path))


if __name__ == '__main__':
    input_file_path = get_input_file_path(2024, 4)
    part_one(input_file_path)
    part_two(input_file_path)
