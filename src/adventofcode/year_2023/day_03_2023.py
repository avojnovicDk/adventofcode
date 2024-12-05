import re
from typing import Generator, Optional

from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_file_path, get_input
from adventofcode.util.string_matrix import StringMatrix

        
def _return_direction(lines: StringMatrix, x: int, y: int, dir_y: int) -> str:
    result = ""
    while True:
        new_char = lines.get_char_in_dir(x, y, 0, dir_y)
        if new_char is None or not new_char.isnumeric():
            return result[::dir_y]
        result += new_char
        y += dir_y

        
def _yield_surrounding_numbers(lines: StringMatrix, x: int, y: int) -> Generator[str, None, None]:
    for x in (x - 1, x, x + 1):
        line = _return_direction(lines, x, y, -1) + lines[x][y] + _return_direction(lines, x, y, 1)
        yield from (n for n in line.replace("*", ".").split(".") if n)


def _yield_gear_ratios(lines: StringMatrix, x: int, y: int) -> int:
    part_numbers = list()
    for s in _yield_surrounding_numbers(lines, x, y):
        if len(part_numbers) == 2:
            return 0
        part_numbers.append(int(s))
    if len(part_numbers) == 2:
        return part_numbers[0] * part_numbers[1]
    return 0


def _get_chars_around_substring(lines: StringMatrix, x: int, y1: int, y2: int) -> str:
    chars = [
        lines.get_char_in_dir(x, y1, 0, -1),
        lines.get_char_in_dir(x, y2, 0, 0),
    ]
    for y in range(y1 - 1, y2 + 1):
        chars.append(lines.get_char_in_dir(x, y, -1, 0))
        chars.append(lines.get_char_in_dir(x, y, 1, 0))
    return "".join(c for c in chars if c is not None)


def _check_is_part_number(lines: StringMatrix, x: int, y1: int, y2: int) -> bool:
    for c in _get_chars_around_substring(lines, x, y1, y2):
        if c and not c.isnumeric() and c != ".":
            return True
    return False


@register_solution(2023, 3, 1)
def part_one(input_file_path: str) -> int:
    lines = StringMatrix(get_input(input_file_path))

    return sum(
        int(m.group())
        for x, line in enumerate(lines)
        for m in re.finditer(r"\d+", line)
        if _check_is_part_number(lines, x, m.start(0), m.end(0))
    )


@register_solution(2023, 3, 2)
def part_two(input_file_path: str) -> int:
    lines = StringMatrix(get_input(input_file_path))
    return lines.count_from_starting("*", _yield_gear_ratios)


if __name__ == '__main__':
    input_file_path = get_input_file_path(2023, 3)
    part_one(input_file_path)
    part_two(input_file_path)
