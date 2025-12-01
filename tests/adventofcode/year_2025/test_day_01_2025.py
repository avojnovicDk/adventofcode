import os
from adventofcode.year_2025.day_01_2025 import part_one, part_two


DIR_NAME, _ = os.path.split(os.path.abspath(__file__))


def test_part_one():
    assert part_one(f"{DIR_NAME}/inputs/day_01.txt") == 3


def test_part_two():
    assert part_two(f"{DIR_NAME}/inputs/day_01.txt") == 6
