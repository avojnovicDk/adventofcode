import os
from adventofcode.year_2024.day_07_2024 import part_one, part_two


DIR_NAME, _ = os.path.split(os.path.abspath(__file__))


def test_part_one():
    assert part_one(f"{DIR_NAME}/inputs/day_07.txt") == 3749


def test_part_two():
    assert part_two(f"{DIR_NAME}/inputs/day_07.txt") == 11387
