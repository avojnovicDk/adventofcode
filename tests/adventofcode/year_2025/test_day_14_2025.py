import os
from adventofcode.year_2025.day_14_2025 import part_one, part_two


DIR_NAME, _ = os.path.split(os.path.abspath(__file__))


def test_part_one():
    assert part_one(f"{DIR_NAME}/inputs/day_14.txt") == 'x'


def test_part_two():
    assert part_two(f"{DIR_NAME}/inputs/day_14.txt") == 'x'
