import os
from adventofcode.year_2024.day_15_2024 import part_one, part_two


DIR_NAME, _ = os.path.split(os.path.abspath(__file__))


def test_part_one():
    assert part_one(f"{DIR_NAME}/inputs/day_15.txt") == 10092


def test_part_two():
    assert part_two(f"{DIR_NAME}/inputs/day_15.txt") == 9021
