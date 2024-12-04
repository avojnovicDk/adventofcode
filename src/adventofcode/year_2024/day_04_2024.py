from typing import Callable

from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_file_path, get_input


def _get_char_in_dir(lines: list[str], x: int, y: int, dir_x: int, dir_y: int, no_of_steps: int = 1) -> str:
        x, y = x + dir_x * no_of_steps, y + dir_y * no_of_steps
        if 0 <= x < len(lines) and 0 <= y < len(lines[0]):
            return lines[x][y]


def _count_from_starting(lines: list[str], starting_char: str, count: Callable) -> int:
    return sum(
        count(lines, x, y)
        for x in range(len(lines))
        for y in range(len(lines[0]))
        if lines[x][y] == starting_char
    )


@register_solution(2024, 4, 1)
def part_one(input_file_path: str) -> int:
    frame = (
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1),
    )

    count = lambda lines, x, y: sum(
        1
        for dir_x, dir_y in frame
        if (_get_char_in_dir(lines, x, y, dir_x, dir_y, 3) == "S"
            and _get_char_in_dir(lines, x, y, dir_x, dir_y, 2) == "A"
            and _get_char_in_dir(lines, x, y, dir_x, dir_y) == "M"
        )
    )
    
    return _count_from_starting(get_input(input_file_path), "X", count)


@register_solution(2024, 4, 2)
def part_two(input_file_path: str) -> int:
    crosses = (
        ((-1, -1), (1,  1),),
        ((-1,  1), (1, -1),),
    )

    count = lambda lines, x, y: 1 if all(
        set(_get_char_in_dir(lines, x, y, dir_x, dir_y) for dir_x, dir_y in cross) == {"M", "S"}
        for cross in crosses
    ) else 0
    
    return _count_from_starting(get_input(input_file_path), "A", count)


if __name__ == '__main__':
    input_file_path = get_input_file_path(2024, 4)
    part_one(input_file_path)
    part_two(input_file_path)
