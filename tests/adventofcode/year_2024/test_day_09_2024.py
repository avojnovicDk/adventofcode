import os
from adventofcode.year_2024.day_09_2024 import part_one, part_two


DIR_NAME, _ = os.path.split(os.path.abspath(__file__))


def test_part_one():
    assert part_one(f"{DIR_NAME}/inputs/day_09.txt") == 1928


def test_part_one_more_than_10():
    assert part_one(f"{DIR_NAME}/inputs/day_09_more_than_10.txt") == 763


def test_part_two():
    assert part_two(f"{DIR_NAME}/inputs/day_09.txt") == 2858
