import os
from adventofcode.year_2024.day_18_2024 import _part_one, _part_two


DIR_NAME, _ = os.path.split(os.path.abspath(__file__))


def test_part_one():
    assert _part_one(f"{DIR_NAME}/inputs/day_18.txt", 7, 12) == 22


def test_part_two():
    assert _part_two(f"{DIR_NAME}/inputs/day_18.txt", 7) == 6 + 1j
