import os
from adventofcode.year_2024.day_14_2024 import _part_one, part_two


DIR_NAME, _ = os.path.split(os.path.abspath(__file__))


def test_part_one():
    assert _part_one(f"{DIR_NAME}/inputs/day_14.txt", 11, 7) == 12


def test_part_two():
    assert part_two(f"{DIR_NAME}/inputs/day_14.txt") == 'x'
