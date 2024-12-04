import os
from adventofcode.year_2024.day_04_2024 import part_one, part_two


DIR_NAME, _ = os.path.split(os.path.abspath(__file__))


def test_part_one():
    assert part_one(f"{DIR_NAME}/inputs/day_04_pt1_a.txt") == 4
    assert part_one(f"{DIR_NAME}/inputs/day_04_pt1_b.txt") == 18


def test_part_two():
    assert part_two(f"{DIR_NAME}/inputs/day_04_pt2_a.txt") == 1
    assert part_two(f"{DIR_NAME}/inputs/day_04_pt2_b.txt") == 9
