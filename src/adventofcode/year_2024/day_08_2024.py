from collections import defaultdict
from itertools import combinations
from typing import Generator
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_file_path, get_input


def _common(input_file_path: str, antinodes_generator: Generator[tuple[int, int], None, None]) -> Generator[tuple[int, int], None, None]:
    antennas = defaultdict(list)
    lines = get_input(input_file_path)
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c != ".":
                antennas[c].append((i, j))

    for positions in antennas.values():
        for p1, p2 in combinations(positions, r=2):
            dx, dy = p2[0] - p1[0], p2[1] - p1[1]
            yield from antinodes_generator(p1[0], p1[1], dx, dy, len(lines), len(lines[0]))


def _yield_d_2d_antinodes(x: int, y: int, dx: int, dy: int, max_x: int, max_y: int) -> Generator[tuple[int, int], None, None]:
        for n in ((x - dx, y - dy), (x + 2 * dx, y + 2 * dy)):
            if 0 <= n[0] < max_x and 0 <= n[1] < max_y:
                yield n


def _yield_d_antinodes(x: int, y: int, dx: int, dy: int, max_x: int, max_y: int) -> Generator[tuple[int, int], None, None]:
    old_x, old_y = x, y
    while 0 <= x < max_x and 0 <= y < max_y:
        yield (x, y)
        x, y = x - dx, y - dy

    x, y = old_x + dx, old_y + dy
    while 0 <= x < max_x and 0 <= y < max_y:
        yield (x, y)
        x, y = x + dx, y + dy


@register_solution(2024, 8, 1)
def part_one(input_file_path: str) -> int:
    return len(set(_common(input_file_path, _yield_d_2d_antinodes)))


@register_solution(2024, 8, 2)
def part_two(input_file_path: str) -> int:
    return len(set(_common(input_file_path, _yield_d_antinodes)))


if __name__ == '__main__':
    input_file_path = get_input_file_path(2024, 8)
    part_one(input_file_path)
    part_two(input_file_path)
