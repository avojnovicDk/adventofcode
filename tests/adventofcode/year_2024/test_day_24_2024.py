import os
from adventofcode.year_2024.day_24_2024 import part_one, part_two


DIR_NAME, _ = os.path.split(os.path.abspath(__file__))


def test_part_one():
    assert part_one(f"{DIR_NAME}/inputs/day_24.txt") == 4
    assert part_one(f"{DIR_NAME}/inputs/day_24_2nd.txt") == 2024


def test_part_two():
    assert part_two(f"{DIR_NAME}/inputs/day_24_pt2.txt") == 'z00,z01,z02,z05'
