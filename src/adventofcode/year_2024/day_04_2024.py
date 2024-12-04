from typing import Callable, NamedTuple
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_file_path, get_input


class Direction(NamedTuple):
    x: int
    y: int


def _get_char_in_direction(lines: list[str], x: int, y: int, direction: Direction):
        x, y = x + direction.x, y + direction.y
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
    frame = tuple(
        Direction(*d) for d in
        (
            (-1, -1), (-1, 0), (-1, 1),
            ( 0, -1),          ( 0, 1),
            ( 1, -1), ( 1, 0), ( 1, 1),
        )
    )

    count = lambda lines, x, y: sum(
        1
        for direction in frame
        if (
            _get_char_in_direction(lines, x, y, direction) == "M"
            and _get_char_in_direction(lines, x + direction.x, y + direction.y, direction) == "A"
            and _get_char_in_direction(lines, x + 2 * direction.x, y + 2 * direction.y, direction) == "S"
        )
    )
    
    return XmasCounter("X", count)(get_input(input_file_path))


@register_solution(2024, 4, 2)
def part_two(input_file_path: str):
    crosses = (
        (Direction(x=-1, y=-1), Direction(x=1, y= 1)),
        (Direction(x=-1, y= 1), Direction(x=1, y=-1))
    )

    count = lambda lines, x, y: 1 if all(
        set(_get_char_in_direction(lines, x, y, direction) for direction in cross) == {"M", "S"}
        for cross in crosses
    ) else 0
    
    return XmasCounter("A", count)(get_input(input_file_path))


if __name__ == '__main__':
    input_file_path = get_input_file_path(2024, 4)
    part_one(input_file_path)
    part_two(input_file_path)
