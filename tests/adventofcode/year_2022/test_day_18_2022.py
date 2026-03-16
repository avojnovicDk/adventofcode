import os
from adventofcode.year_2022.day_18_2022 import part_one, part_two


DIR_NAME, _ = os.path.split(os.path.abspath(__file__))


def test_part_one():
    assert part_one(f"{DIR_NAME}/inputs/day_18.txt") == 64


def test_part_two():
    assert part_two(f"{DIR_NAME}/inputs/day_18.txt") == 58

def test_part_two_neighbour_airpockets():
    assert part_two(f"{DIR_NAME}/inputs/day_18_a.txt") == 70
