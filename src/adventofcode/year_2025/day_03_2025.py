from functools import reduce

from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_file_path, yield_lines


def _get_largest_joltage(pair, z):
    x, y = pair
    return max(pair) + (z if y > x or z > y else y)


@register_solution(2025, 3, 1)
def part_one(input_file_path: str):
    return sum(
        map(
            int,
            (
                reduce(
                    _get_largest_joltage,
                    line.strip(),
                    '00'
                )
                for line in yield_lines(input_file_path)
            )
        )
    )


def _get_max_joltage(line):
    joltage, safe, keep = "", line[:-11], line[-11:]
    for _ in range(12):
        d = max(safe)
        joltage += d
        safe = safe.split(d, 1)[1]
        if keep:
            safe += keep[0]
            keep = keep[1:]

    return int(joltage)


@register_solution(2025, 3, 2)
def part_two(input_file_path: str):
    return sum(
        _get_max_joltage(line.strip())
        for line in yield_lines(input_file_path)
    )


if __name__ == '__main__':
    input_file_path = get_input_file_path(2025, 3)
    part_one(input_file_path)
    part_two(input_file_path)
