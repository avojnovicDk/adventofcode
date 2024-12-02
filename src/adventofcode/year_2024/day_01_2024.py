from collections import Counter
from typing import Iterable

from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_file_path, yield_lines


def _split_into_cols(lines: Iterable[str]) -> tuple[list[int]]:
    left, right = list(), list()

    for line in lines:
        v1, v2 = line.split()
        left.append(int(v1))
        right.append(int(v2))

    return left, right


@register_solution(2024, 1, 1)
def part_one(input_file_path: str) -> int:
    left, right = _split_into_cols(yield_lines(input_file_path))

    return sum(abs(r - l) for l, r in zip(sorted(left), sorted(right)))


@register_solution(2024, 1, 2)
def part_two(input_file_path: str) -> int:
    left, right = map(Counter, _split_into_cols(yield_lines(input_file_path)))
    
    return sum(n * count * right[n] for n, count in left.items())


if __name__ == '__main__':
    input_file_path = get_input_file_path(2024, 1)
    part_one(input_file_path)
    part_two(input_file_path)
