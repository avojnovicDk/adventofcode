from collections import Counter
from typing import Iterable

from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_file_path, yield_lines


def _split_lines_into_cols_of_ints(lines: Iterable[str]):
    col1, col2 = list(), list()

    for line in lines:
        v1, v2 = line.split()
        col1.append(int(v1))
        col2.append(int(v2))

    return col1, col2


@register_solution(2024, 1, 1)
def part_one(input_file_path: str) -> int:
    col1, col2 = _split_lines_into_cols_of_ints(yield_lines(input_file_path))
    return sum(abs(b - a) for a, b in zip(sorted(col1), sorted(col2)))


@register_solution(2024, 1, 2)
def part_two(input_file_path: str) -> int:
    col1, col2 = list(), list()
    for line in yield_lines(input_file_path):
        v1, v2 = line.split()
        col1.append(int(v1))
        col2.append(int(v2))
    
    col1, col2 = Counter(col1), Counter(col2)
    
    return sum(n * count * col2[n] for n, count in col1.items())


if __name__ == '__main__':
    input_file_path = get_input_file_path(2024, 1)
    part_one(input_file_path)
    part_two(input_file_path)
